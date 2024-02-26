import glob
import os
import re
from typing import Tuple
from urllib import parse
from urllib.parse import urlparse

import requests
import logging
from public import covert_config
from youDaoNoteApi import YoudaoNoteApi
import time
import oss2
from oss2.credentials import (
    EnvironmentVariableCredentialsProvider,
    CredentialsProvider,
    Credentials,
)

REGEX_IMAGE_URL = re.compile(r'!\[.*?\]\((.*?note\.youdao\.com.*?)\)')
REGEX_ATTACH = re.compile(r'\[(.*?)\]\(((http|https)://note\.youdao\.com.*?)\)')
MARKDOWN_SUFFIX = '.md'
NOTE_SUFFIX = '.note'
# 有道云笔记的图片地址
# IMAGES = 'images'
IMAGES = 'attachments'
# 有道云笔记的附件地址
ATTACH = 'attachments'
CONFIG_PATH = 'config.json'


class PullImages():
    def __init__(self, youdaonote_api=None, smms_secret_token: str = None, is_relative_path: bool = None):
        self.youdaonote_api = youdaonote_api
        self.smms_secret_token = smms_secret_token
        self.is_relative_path = is_relative_path  # 是否使用相对路径
        if not self.smms_secret_token and not self.is_relative_path:
            self.load_config()
        if not self.youdaonote_api:
            self.login()

    def migration_ydnote_url(self, file_path):
        """
        迁移有道云笔记文件 URL
        :param file_path:
        :return:
        """

        stats = os.stat(file_path)
        if stats.st_size == 0:
            logging.error(f"{file_path} {stats.st_size}")
            return

        with open(file_path, 'rb') as f:
            content = f.read().decode('utf-8')

        # 图片
        image_urls = REGEX_IMAGE_URL.findall(content)
        if len(image_urls) > 0:
            logging.info('正在转换有道云笔记「{}」中的有道云图片链接...'.format(file_path))
        for index, image_url in enumerate(image_urls):
            image_path = self._get_new_image_path(file_path, image_url, index)
            if image_url == image_path:
                continue
            # 将绝对路径替换为相对路径，实现满足 Obsidian 格式要求
            # 将 image_path 路径中 images 之前的路径去掉，只保留以 images 开头的之后的路径
            if self.is_relative_path and IMAGES in image_path:
                image_path = image_path[image_path.find(IMAGES):]

            image_path = self.url_encode(image_path)
            content = content.replace(image_url, image_path)

        # 附件
        attach_name_and_url_list = REGEX_ATTACH.findall(content)
        if len(attach_name_and_url_list) > 0:
            logging.info('正在转换有道云笔记「{}」中的有道云附件链接...'.format(file_path))
        for attach_name_and_url in attach_name_and_url_list:
            attach_url = attach_name_and_url[1]
            attach_path = self._download_attach_url(file_path, attach_url, attach_name_and_url[0])
            if not attach_path:
                continue
            # 将 attach_path 路径中 attachments 之前的路径去掉，只保留以 attachments 开头的之后的路径
            if self.is_relative_path:
                attach_path = attach_path[attach_path.find(ATTACH):]
            content = content.replace(attach_url, attach_path)

        with open(file_path, 'wb') as f:
            f.write(content.encode())
        return

    def _get_new_image_path(self, file_path, image_url, index) -> str:
        """
        将图片链接转换为新的链接
        :param file_path:
        :param image_url:
        :return: new_image_path
        """
        # 上传smms
        if self.smms_secret_token:
            new_file_url, error_msg = ImageUpload.upload_to_smms(
                youdaonote_api=self.youdaonote_api,
                image_url=image_url,
                smms_secret_token=self.smms_secret_token,
            )
            if not error_msg:
                return new_file_url
        # 上传阿里云
        if self.aliyun_oss:
            new_file_url, error_msg = ImageUpload.upload_to_aliyun(
                youdaonote_api=self.youdaonote_api,
                image_url=image_url,
                **self.aliyun_oss,
            )
            if not error_msg:
                return new_file_url
        logging.info(error_msg)
        image_path = self._download_image_url(file_path, image_url, index)
        return image_path or image_url

    def _download_image_url(self, file_path, url, index) -> str:
        """
        下载文件到本地，返回本地路径
        :param file_path:
        :param url:
        :param attach_name:
        :return:  path
        """
        try:
            response = self.youdaonote_api.http_get(url)
        except requests.exceptions.ProxyError as err:
            error_msg = '网络错误，「{}」下载失败。错误提示：{}'.format(url, format(err))
            logging.info(error_msg)
            return ''

        content_type = response.headers.get('Content-Type')
        file_type = '图片'
        if response.status_code != 200 or not content_type:
            error_msg = '下载「{}」失败！{}可能已失效，可浏览器登录有道云笔记后，查看{}是否能正常加载'.format(url, file_type,
                                                                                                         file_type)
            logging.info(error_msg)
            return ''

        # 默认下载图片到 images 文件夹
        file_dirname = IMAGES
        # 后缀 png 和 jpeg 后可能出现 ; `**.png;`, 原因未知
        content_type_arr = content_type.split('/')
        file_suffix = '.' + content_type_arr[1].replace(';', '') if len(content_type_arr) == 2 else "jpg"
        local_file_dir = os.path.join(os.path.dirname(file_path), file_dirname)

        if not os.path.exists(local_file_dir):
            os.mkdir(local_file_dir)

        file_name = os.path.basename(os.path.splitext(file_path)[0])
        file_name = self._optimize_file_name(file_name)
        # 请求后的真实的URL中才有东西
        realUrl = parse.parse_qs(urlparse(response.url).query)
        real_filename = realUrl.get('filename')
        if real_filename:
            # dict 不为空时，去获取真实文件名称
            read_file_name = real_filename[0]
            file_suffix = '.' + read_file_name.split('.')[-1]
            file_name = os.path.basename(os.path.splitext(file_path)[0]) + '_image_' + str(index) + file_suffix
        else:
            file_name = os.path.basename(os.path.splitext(file_path)[0]) + '_image_' + str(index) + file_suffix

        local_file_path = os.path.join(local_file_dir, file_name)
        # 使md附件或者图片的路径分隔符为"/"
        local_file_path = local_file_path.replace('\\', '/')

        try:
            with open(local_file_path, 'wb') as f:
                f.write(response.content)  # response.content 本身就为字节类型
            logging.debug('已将{}「{}」转换为「{}」'.format(file_type, url, local_file_path))
        except:
            error_msg = '{} {}有误！'.format(url, file_type)
            logging.error(error_msg)
            return ''

        return local_file_path

    def _download_attach_url(self, file_path, url, attach_name=None) -> str:
        """
        下载文件到本地，返回本地路径
        :param file_path:
        :param url:
        :param attach_name:
        :return:  path
        """
        try:
            response = self.youdaonote_api.http_get(url)
        except requests.exceptions.ProxyError as err:
            error_msg = '网络错误，「{}」下载失败。错误提示：{}'.format(url, format(err))
            logging.info(error_msg)
            return ''

        content_type = response.headers.get('Content-Type')
        file_type = '附件'
        if response.status_code != 200 or not content_type:
            error_msg = '下载「{}」失败！{}可能已失效，可浏览器登录有道云笔记后，查看{}是否能正常加载'.format(url, file_type,
                                                                                                         file_type)
            logging.info(error_msg)
            return ''

        file_dirname = ATTACH
        attach_name = self._optimize_file_name(attach_name)
        file_suffix = attach_name
        local_file_dir = os.path.join(os.path.dirname(file_path), file_dirname)

        if not os.path.exists(local_file_dir):
            os.mkdir(local_file_dir)

        local_file_path: str = os.path.join(local_file_dir, file_suffix)
        # 使md附件或者图片的路径分隔符为"/"
        local_file_path = local_file_path.replace('\\', '/')

        try:
            with open(local_file_path, 'wb') as f:
                f.write(response.content)  # response.content 本身就为字节类型
            logging.info('已将{}「{}」转换为「{}」'.format(file_type, url, local_file_path))
        except:
            error_msg = '{} {}有误！'.format(url, file_type)
            logging.info(error_msg)
            return ''

        return local_file_path

    def _optimize_file_name(self, name) -> str:
        """
        优化文件名，替换下划线
        :param name:
        :return:
        """
        # 去除换行符,首尾的空格,文件名有空格识别不出图片
        name = name.strip()
        regex_symbol = re.compile(r'[\\/:\*\?"<>\|、]')  # 符号：\ / : * ? " < > | ( )
        name = regex_symbol.sub('_', name)
        return name

    def login(self):
        self.youdaonote_api = YoudaoNoteApi()
        error_msg = self.youdaonote_api.login_by_cookies()
        if error_msg:
            return '', error_msg

    def load_config(self):
        config_dict, error_msg = covert_config(CONFIG_PATH)
        self.smms_secret_token = config_dict['smms_secret_token']
        self.is_relative_path = config_dict['is_relative_path']
        self.aliyun_oss = config_dict["aliyun_oss"]

    def more_pull_images(self, md_dir: str):
        """遍历文件夹的md文件,拉取md文件有道云的图片和附件

        Args:
            md_dir (str): md文件的目录
        """
        file_path = md_dir + "/**/*.md"
        # 匹配当前目录下所有的txt文件
        file_list = glob.glob(file_path, recursive=True)
        logging.info(file_list)
        for md_file in file_list:
            self.migration_ydnote_url(md_file)

    @classmethod
    def url_encode(cls, path: str):
        """对一些特殊字符url编码
        Args:
            path (str): 
        """
        path = path.replace(' ', '%20')
        return path


class CustomCredentialsProvider(CredentialsProvider):
    def __init__(self, access_key_id, access_key_secret, security_token):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.security_token = security_token
        if not access_key_id:
            raise KeyError("Access key id should not be null or empty.")
        if not access_key_secret:
            raise KeyError("Secret access key should not be null or empty.")

    def get_credentials(self):
        return Credentials(
            self.access_key_id, self.access_key_secret, self.security_token
        )


class ImageUpload(object):
    """
    图片上传到指定图床
    """

    @staticmethod
    def upload_to_smms(youdaonote_api, image_url, smms_secret_token) -> Tuple[str, str]:
        """
        上传图片到 sm.ms
        :param image_url:
        :param smms_secret_token:
        :return: url, error_msg
        """
        try:
            smfile = youdaonote_api.http_get(image_url).content
        except:
            error_msg = '下载「{}」失败！图片可能已失效，可浏览器登录有道云笔记后，查看图片是否能正常加载'.format(image_url)
            return '', error_msg
        files = {'smfile': smfile}
        upload_api_url = 'https://sm.ms/api/v2/upload'
        headers = {'Authorization': smms_secret_token}

        error_msg = 'SM.MS 免费版每分钟限额 20 张图片，每小时限额 100 张图片，大小限制 5 M，上传失败！「{}」未转换，' \
                    '将下载图片到本地'.format(image_url)
        try:
            res_json = requests.post(upload_api_url, headers=headers, files=files, timeout=5).json()
        except requests.exceptions.ProxyError as err:
            error_msg = '网络错误，上传「{}」到 SM.MS 失败！将下载图片到本地。错误提示：{}'.format(image_url, format(err))
            return '', error_msg
        except Exception:
            return '', error_msg

        if res_json.get('success'):
            url = res_json['data']['url']
            logging.info('已将图片「{}」转换为「{}」'.format(image_url, url))
            return url, ''
        if res_json.get('code') == 'image_repeated':
            url = res_json['images']
            logging.info('已将图片「{}」转换为「{}」'.format(image_url, url))
            return url, ''
        if res_json.get('code') == 'flood':
            return '', error_msg

        error_msg = '上传「{}」到 SM.MS 失败，请检查图片 url 或 smms_secret_token（{}）是否正确！将下载图片到本地'.format(
            image_url, smms_secret_token)
        return '', error_msg

    @staticmethod
    def upload_to_aliyun(youdaonote_api, image_url, **kvargs) -> Tuple[str, str]:
        from urllib.parse import unquote
        try:
            response = youdaonote_api.http_get(image_url)
        except:
            error_msg = "下载「{}」失败！图片可能已失效，可浏览器登录有道云笔记后，查看图片是否能正常加载".format(
                image_url
            )
            return "", error_msg
        try:
            filename = (
                response.headers["Content-Disposition"]
                .split("; ")[1]
                .replace("filename=", "")
                .strip('"')
            )
        except:
            error_msg = "下载「{}」失败！filename解析失败".format(image_url)
            return ("", error_msg)
        filename = str(int(time.time())) + "-" + filename
        originname = unquote(filename)
        content = response.content
        auth = oss2.ProviderAuth(
            CustomCredentialsProvider(
                kvargs["access_key_id"],
                kvargs["access_key_secret"],
                kvargs["security_token"],
            )
        )
        bucket = oss2.Bucket(auth, kvargs["end_point"], kvargs["bucket"])
        result = bucket.put_object(kvargs["dir_path"] + originname, content)
        if result.status != 200:
            logging.warn("上传图片至OSS失败，错误信息：{}".format(result.status))
            return "", "上传图片至OSS失败，错误信息：{}".format(result.status)
        new_url = "https://" + kvargs["bucket"]+ "."+ kvargs["end_point"]+ "/"+ kvargs["dir_path"]+ filename
        logging.info("upload_to_aliyun已将图片「{}」转换为「{}」".format(image_url, new_url))
        return (
            new_url,
            "",
        )

if __name__ == '__main__':
    path = "D:\\obsidian\\obsidian\\其他"
    pull_image = PullImages()
    pull_image.migration_ydnote_url('D:/obsidian/obsidian/其他/test-new.md')
    # pull_image.more_pull_images(path)
    # data = pull_image._optimize_file_name('正 s()ss&&文.jpg')
    # data = pull_image.url_encode(data)
    # logging.info(data)
