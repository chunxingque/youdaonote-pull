#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os
import platform
import re
import sys
import time
import traceback
import xml.etree.ElementTree as ET
from enum import Enum
from typing import Tuple

import requests
from win32_setctime import setctime

from core import logging_conf
from core.convert import YoudaoNoteConvert
from core.public import covert_config,delete_folder
from core.pull_images import PullImages
from core.youDaoNoteApi import YoudaoNoteApi


class FileActionEnum(Enum):
    CONTINUE = "跳过"
    ADD = "新增"
    UPDATE = "更新"
    
class NoteTypeEnum(Enum):
    MD = 1
    JSON = 2
    XML = 3
    CLIP = 4
    OTHER = 5
    MINDMAP = 6

class YoudaoNotePull(object):
    """
    有道云笔记 Pull 封装
    """

    def __init__(self):
        self.local_root_dir = None    # 本地根目录
        self.youdaonote_api = None
        self.smms_secret_token = None
        self.is_relative_path = None  # 是否使用相对路径
        self.ydnote_dir = ""          # 有道笔记目录
        self.ydnote_dir_list = []     # 有道笔记目录分割列表
        self.load_config()
    
    
    def load_config(self):
        config_dict, error_msg = covert_config()
        if error_msg:
            logging.error(error_msg)
            sys.exit(1)
        # 有道笔记目录
        self.ydnote_dir: str = config_dict['ydnote_dir']
        if self.ydnote_dir:
            self.ydnote_dir_list = self.ydnote_dir.split('/')
        else:
            self.ydnote_dir_list = []
        self.smms_secret_token = config_dict['smms_secret_token']
        self.is_relative_path = config_dict['is_relative_path']
        self.local_root_dir = config_dict['local_dir']
        self.del_spare_file = config_dict['del_spare_file']
        self.del_spare_dir = config_dict['del_spare_dir']

    def get_ydnote_dir_id(self):
        """
        获取有道云笔记根目录
        :return:
        """
        
        self.local_root_dir, error_msg = self._check_local_dir(local_dir = self.local_root_dir)
        if error_msg:
            return '', error_msg
        self.youdaonote_api = YoudaoNoteApi()
        error_msg = self.youdaonote_api.login_by_cookies()
        if error_msg:
            return '', error_msg
        return self._get_ydnote_dir_id()
    
    
    def del_spare_local_file(self, local_dir: str,yd_dir_list: list):
        """
        删除该目录下的本地多余的文件，这些可能是重命名的笔记，被删除的笔记，或者外加的笔记
        :param local_dir: 本地目录
        """
             
        local_files = os.listdir(local_dir)
        
        for file in local_files:
            # 排除不需要的文件
            if file.startswith('.'):
                continue
            
            file_path = os.path.join(local_dir, file).replace('\\', '/')
            if os.path.isfile(file_path) and file not in yd_dir_list:
                os.remove(file_path)
                logging.info(f"删除多余文件：{file_path}")
                
    def del_spare_local_dir(self, local_dir: str,yd_dir_list: list):
        """
        删除该目录下本地多余的目录，这些可能是重命名的目录，被删除的目录，或者外加的目录
        :param local_dir: 本地目录
        """
        exclude_file = ["attachments"]
                
        local_files = os.listdir(local_dir)
        
        for file in local_files:
            # 排除不需要的文件
            if file.startswith('.'):
                continue
            
            if file in exclude_file:
                continue
            
            file_path = os.path.join(local_dir, file).replace('\\', '/')
            if os.path.isdir(file_path) and file not in yd_dir_list:
                delete_folder(file_path)
                logging.info(f"删除多余目录：{file_path}")
                

    def pull_dir_by_id_recursively(self, dir_id, local_dir: str, dir_depth: int=0):
        """
        根据目录 ID 循环遍历下载目录下所有文件
        :param dir_id:
        :param local_dir: 本地目录
        :return: error_msg
        """
        # 目录下所有文件或目录
        yb_dir_file_list = []
        yb_dir_dir_list = []
        
        dir_info = self.youdaonote_api.get_dir_info_by_id(dir_id)
        try:
            entries = dir_info['entries']
        except KeyError:
            raise KeyError('有道云笔记修改了接口地址，此脚本暂时不能使用！请提 issue')
        for entry in entries:
            file_entry = entry['fileEntry']
            id = file_entry['id']
            file_name = file_entry['name']
            # 优化文件名
            file_name = self._optimize_file_name(file_name)
            
            # 判断当前目录是否在要下载
            if self.ydnote_dir_list and file_entry['dir']:
                if len(self.ydnote_dir_list) > dir_depth:
                    if self.ydnote_dir_list[dir_depth] != file_name:
                        continue
                    else:
                        next_dir_depth = dir_depth + 1
                        sub_dir = os.path.join(local_dir, file_name).replace('\\', '/')
                        # 判断本地文件夹是否存在
                        if not os.path.exists(sub_dir):
                            os.mkdir(sub_dir)
                        self.pull_dir_by_id_recursively(id, sub_dir,next_dir_depth)
                        # 其他目录不做处理
                        return None
            
            if file_entry['dir']:
                yb_dir_dir_list.append(file_name)
                next_dir_depth = dir_depth + 1
                sub_dir = os.path.join(local_dir, file_name).replace('\\', '/')
                # 判断本地文件夹是否存在
                if not os.path.exists(sub_dir):
                    os.mkdir(sub_dir)
                self.pull_dir_by_id_recursively(id, sub_dir,next_dir_depth)
            else:
                modify_time = file_entry['modifyTimeForSort']
                create_time = file_entry['createTimeForSort']
                # 判断笔记类型
                note_type = self.judge_type(id,file_name) 
                # 转化为下载文件名
                download_filename,local_filename = self.get_filename(file_name,note_type)
                self._add_or_update_file(id, local_dir,download_filename,local_filename, note_type,modify_time, create_time)
                yb_dir_file_list.append(local_filename)
        
        # 删除本地多余的文件
        if self.del_spare_file:
            self.del_spare_local_file(local_dir, yb_dir_file_list)
        # 删除本地多余的目录
        if self.del_spare_dir:
            self.del_spare_local_dir(local_dir, yb_dir_dir_list)
        

    def _check_local_dir(self, local_dir, test_default_dir=None) -> Tuple[str, str]:
        """
        检查本地文件夹
        :param local_dir: 本地文件夹名（绝对路径）
        :return: local_dir, error_msg
        """
        # 如果没有指定本地文件夹，当前目录新增 youdaonote 目录
        if not local_dir:
            add_dir = test_default_dir if test_default_dir else 'youdaonote'
            # 兼容 Windows 系统，将路径分隔符（\\）替换为 /
            local_dir = os.path.join(os.getcwd(), add_dir)

        # 如果指定的本地文件夹不存在，创建文件夹
        if not os.path.exists(local_dir):
            try:
                os.makedirs(local_dir)
            except:
                return '', '请检查「{}」上层文件夹是否存在，并使用绝对路径！'.format(local_dir)
        local_dir = local_dir.replace('\\', '/')
        return local_dir, ''

    def _get_ydnote_dir_id(self, ydnote_dir: str=None) -> Tuple[str, str]:
        """
        获取指定有道云笔记指定目录 ID
        :param ydnote_dir: 指定有道云笔记指定目录
        :return: dir_id, error_msg
        """
        root_dir_info = self.youdaonote_api.get_root_dir_info_id()
        root_dir_id = root_dir_info['fileEntry']['id']
        # 如果不指定文件夹，取根目录 ID
        if not ydnote_dir:
            return root_dir_id, ''

        dir_info = self.youdaonote_api.get_dir_info_by_id(root_dir_id)
        for entry in dir_info['entries']:
            file_entry = entry['fileEntry']
            if file_entry['name'] == ydnote_dir:
                return file_entry['id'], ''

        return '', '有道云笔记指定顶层目录不存在'
        
    
    def get_filename(self, yb_file_name: str, note_type: str):
        """有道云笔记文件名转换为下载的文件名和最后的本地文件名

        Args:
            yb_file_name (str): _description_

        Returns:
            _type_: _description_
        """
        
        # logging.info(f"{file_name}:{note_type}")
        if yb_file_name.__contains__('\r') or yb_file_name.__contains__('\n'):
            logging.warning(f"注意这个文件名 {yb_file_name}")
            yb_file_name = yb_file_name.replace('\t', '').replace('\n', '')  # 原后缀路径

        if note_type == NoteTypeEnum.JSON:
            download_file_name = f'{os.path.splitext(yb_file_name)[0]}.json'
            local_file_name = f'{os.path.splitext(yb_file_name)[0]}.md'
        elif note_type == NoteTypeEnum.XML:
            download_file_name = f'{os.path.splitext(yb_file_name)[0]}.xml'
            local_file_name = f'{os.path.splitext(yb_file_name)[0]}.md'
        else:
            download_file_name = yb_file_name
            local_file_name = yb_file_name
        
        return download_file_name,local_file_name

    def _add_or_update_file(self, file_id, local_dir,download_filename,local_filename, note_type, modify_time, create_time):
        """
        新增或更新文件
        :param file_id:
        :param file_name:
        :param local_dir:
        :param modify_time:
        :return:
        """
        local_file_path = os.path.join(local_dir, local_filename).replace('\\', '/')
        download_file_path = os.path.join(local_dir, download_filename).replace('\\', '/')
        
        file_action = self._get_file_action(local_file_path, modify_time)
        if file_action == FileActionEnum.CONTINUE:
            return
        # if file_action == FileActionEnum.UPDATE:
        #     # 考虑到使用 f.write() 直接覆盖原文件，在 Windows 下报错（WinError 183），先将其删除
        #     os.remove(local_file_path)
        try:
            self._pull_file(file_id, download_file_path, note_type)
            tip = f"类型：{note_type}"
            logging.info('{}「{}」{}'.format(file_action.value, local_file_path, tip))

            if platform.system() == "Windows":
                setctime(local_file_path, create_time)
            else:
                os.utime(local_file_path, (create_time, modify_time))

        except Exception as error:
            logging.error(
                '{}「{}」失败！请检查文件！错误提示：{}'.format(file_action.value, local_file_path, format(error)), error)

    def judge_type(self, file_id: str, file_name: str) -> NoteTypeEnum:
        """
        判断返回内容类型
        """
        youdao_file_suffix = os.path.splitext(file_name)[1]  # 笔记后缀
        note_type = NoteTypeEnum.OTHER
        if youdao_file_suffix == ".note":
            response = self.youdaonote_api.get_file_by_id(file_id)
            content = response.content[:5]
            if content.startswith(b'{"'):
                note_type = NoteTypeEnum.JSON
            else:            
                is_xml = True if (content == b"<?xml" or response.content[:1] == b"<") else False
                if is_xml:  # xml类型
                    note_type = NoteTypeEnum.XML
                else:
                    logging.warning(f"文件后缀「{youdao_file_suffix}」 {file_name} 不识别，请检查！")
        elif youdao_file_suffix == ".md":
            note_type = NoteTypeEnum.MD
        elif youdao_file_suffix == ".clip":
            note_type = NoteTypeEnum.CLIP
        elif youdao_file_suffix == ".mindmap":
            note_type = NoteTypeEnum.MINDMAP
        else:
            logging.warning(f"文件后缀「{youdao_file_suffix}」 {file_name} 不识别，请检查！")

        return note_type

    def _pull_file(self, file_id, file_path, note_type):
        """
        下载文件
        :param file_id:
        :param file_path:
        :param itype:
        :return:
        """
        # 1、所有的都先下载
        response = self.youdaonote_api.get_file_by_id(file_id)
        with open(file_path, 'wb') as f:
            f.write(response.content)  # response.content 本身就是字节类型
        new_file_path = ""
        
        if note_type == NoteTypeEnum.JSON:
            new_file_path = YoudaoNoteConvert.covert_json_to_markdown(file_path,is_delete=True)
        elif note_type == NoteTypeEnum.MD:
            YoudaoNoteConvert.markdown_filter(file_path)
            new_file_path = file_path
        elif note_type == NoteTypeEnum.XML:
            try:
                new_file_path = YoudaoNoteConvert.covert_xml_to_markdown(file_path)
            except (ET.ParseError, IndexError):
                logging.info(f'{file_path} 笔记应该为 17 年以前新建，格式为 html，将转换为 Markdown ...')
                new_file_path = YoudaoNoteConvert.covert_html_to_markdown(file_path)
            except Exception as e2:
                logging.error(f'{file_path} 笔记转换 MarkDown 失败，将跳过', e2)
    
        # 迁移附件和图片
        file_suffix = os.path.splitext(new_file_path)[1]
        if os.path.exists(new_file_path) and file_suffix == ".md":
            pull_image = PullImages(self.youdaonote_api, self.smms_secret_token, self.is_relative_path)
            pull_image.migration_ydnote_url(new_file_path)

    def _get_file_action(self, local_file_path, modify_time) -> Enum:
        """
        获取文件操作行为
        :param local_file_path:
        :param modify_time:
        :return: FileActionEnum
        """
        # 如果不存在，则下载
        if not os.path.exists(local_file_path):
            return FileActionEnum.ADD

        # 如果已经存在，判断是否需要更新
        # 如果有道云笔记文件更新时间小于本地文件时间，说明没有更新，则不下载，跳过
        if modify_time <= int(os.path.getmtime(local_file_path)):
            logging.debug('此文件「%s」不更新，跳过', local_file_path)
            return FileActionEnum.CONTINUE
        # 同一目录存在同名 md 和 note 文件时，后更新文件将覆盖另一个
        return FileActionEnum.UPDATE

    def _optimize_file_name(self, name) -> str:
        """
        优化文件名，替换特殊符号为下划线
        :param name:
        :return:
        """
        # 替换下划线
        regex_symbol = re.compile(r'[<]')  # 符号： <
        # 删除特殊字符
        del_regex_symbol = re.compile(r'[\\/":\|\*\?#>]')  # 符号：\ / " : | * ? # >
        # 首尾的空格
        name = name.replace('\n', '')
        # 去除换行符
        name = name.strip()
        # 替换一些特殊符号
        name = regex_symbol.sub('_', name)
        name = del_regex_symbol.sub('', name)
        return name


if __name__ == '__main__':

    logging_conf.init_logging()

    logging.info('\n\n\n')

    start_time = int(time.time())
    try:
        youdaonote_pull = YoudaoNotePull()    
        ydnote_dir_id, error_msg = youdaonote_pull.get_ydnote_dir_id()
        if error_msg:
            logging.info(error_msg)
            sys.exit(1)
        logging.info('正在 pull，请稍后 ...')
        youdaonote_pull.pull_dir_by_id_recursively(ydnote_dir_id, youdaonote_pull.local_root_dir)
    except requests.exceptions.ProxyError as proxyErr:
        logging.info(
            '请检查网络代理设置；也有可能是调用有道云笔记接口次数达到限制，请等待一段时间后重新运行脚本，若一直失败，可删除「cookies.json」后重试')
        traceback.print_exc()
        logging.info('已终止执行')
        sys.exit(1)
    except requests.exceptions.ConnectionError as connectionErr:
        logging.info('网络错误，请检查网络是否正常连接。若突然执行中断，可忽略此错误，重新运行脚本')
        traceback.print_exc()
        logging.info('已终止执行')
        sys.exit(1)
    # 链接错误等异常
    except Exception as err:
        logging.info('其他错误：', format(err))
        traceback.print_exc()
        logging.info('已终止执行')
        sys.exit(1)

    end_time = int(time.time())
    logging.info('运行完成！耗时 {} 秒'.format(str(end_time - start_time)))
