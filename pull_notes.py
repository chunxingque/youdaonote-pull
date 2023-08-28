#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import logging
import os
import re
import sys
import time
import traceback
import xml.etree.ElementTree as ET
from enum import Enum
from typing import Tuple
import requests

from convert import YoudaoNoteConvert
from youDaoNoteApi import YoudaoNoteApi
from pull_images import PullImages
from public import FileActionEnum
from public import covert_config


MARKDOWN_SUFFIX = '.md'
NOTE_SUFFIX = '.note'
CONFIG_PATH = 'config.json'


class YoudaoNotePull(object):
    """
    有道云笔记 Pull 封装
    """
    CONFIG_PATH = 'config.json'

    def __init__(self):
        self.root_local_dir = None  # 本地文件根目录
        self.youdaonote_api = None
        self.smms_secret_token = None
        self.is_relative_path = None  # 是否使用相对路径

    def get_ydnote_dir_id(self):
        """
        获取有道云笔记根目录或指定目录 ID
        :return:
        """
        config_dict, error_msg = covert_config(CONFIG_PATH)
        if error_msg:
            return '', error_msg
        local_dir, error_msg = self._check_local_dir(local_dir=config_dict['local_dir'])
        if error_msg:
            return '', error_msg
        self.root_local_dir = local_dir
        self.youdaonote_api = YoudaoNoteApi()
        error_msg = self.youdaonote_api.login_by_cookies()
        if error_msg:
            return '', error_msg
        self.smms_secret_token = config_dict['smms_secret_token']
        self.is_relative_path = config_dict['is_relative_path']
        return self._get_ydnote_dir_id(ydnote_dir=config_dict['ydnote_dir'])

    def pull_dir_by_id_recursively(self, dir_id, local_dir):
        """
        根据目录 ID 循环遍历下载目录下所有文件
        :param dir_id:
        :param local_dir: 本地目录
        :return: error_msg
        """
        dir_info = self.youdaonote_api.get_dir_info_by_id(dir_id)
        try:
            entries = dir_info['entries']
        except KeyError:
            raise KeyError('有道云笔记修改了接口地址，此脚本暂时不能使用！请提 issue')
        for entry in entries:
            file_entry = entry['fileEntry']
            id = file_entry['id']
            file_name = file_entry['name']
            file_name = self._optimize_file_name(file_name)
            # noteType = file_entry['noteType']
            # orgEditorType = file_entry['orgEditorType']
            if file_entry['dir']:
                sub_dir = os.path.join(local_dir, file_name).replace('\\', '/')
                # 判断本地文件夹是否存在
                if not os.path.exists(sub_dir):
                    os.mkdir(sub_dir)
                self.pull_dir_by_id_recursively(id, sub_dir)
            else:
                modify_time = file_entry['modifyTimeForSort']
                self._add_or_update_file(id, file_name, local_dir, modify_time)


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
            local_dir = os.path.join(os.getcwd(), add_dir).replace('\\', '/')

        # 如果指定的本地文件夹不存在，创建文件夹
        if not os.path.exists(local_dir):
            try:
                os.mkdir(local_dir)
            except:
                return '', '请检查「{}」上层文件夹是否存在，并使用绝对路径！'.format(local_dir)
        return local_dir, ''

    def _get_ydnote_dir_id(self, ydnote_dir) -> Tuple[str, str]:
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

    def _add_or_update_file(self, file_id, file_name, local_dir, modify_time):
        """
        新增或更新文件
        :param file_id:
        :param file_name:
        :param local_dir:
        :param modify_time:
        :return:
        """
        
        youdao_file_suffix = os.path.splitext(file_name)[1]  # 笔记后缀
        note_type = self.judge_type(file_id,youdao_file_suffix)
        # print(f"{file_name}:{note_type}")
        is_note = True if note_type == 1 or note_type == 2 else False
        original_file_path = os.path.join(local_dir, file_name).replace('\\', '/')  # 原后缀路径
        # 生成.md后缀的文件的绝对路径
        local_file_path = os.path.join(local_dir, ''.join([os.path.splitext(file_name)[0], MARKDOWN_SUFFIX])).replace(
            '\\', '/') if is_note else original_file_path
        # 如果有有道云笔记是「note」类型，则提示类型
        tip = f'| 原文件: {file_name} | 类型：{note_type}'
        file_action = self._get_file_action(local_file_path, modify_time)
        if file_action == FileActionEnum.CONTINUE:
            return
        if file_action == FileActionEnum.UPDATE:
            # 考虑到使用 f.write() 直接覆盖原文件，在 Windows 下报错（WinError 183），先将其删除
            os.remove(local_file_path)
        try:
            self._pull_file(file_id, original_file_path, note_type)
            print('{}「{}」{}'.format(file_action.value, local_file_path, tip))
        except Exception as error:
            print('{}「{}」失败！请检查文件！错误提示：{}'.format(file_action.value, original_file_path, format(error)))

    def _judge_is_note(self, file_id, youdao_file_suffix):
        """
        判断是否是 note 类型
        :param file_id:
        :param youdao_file_suffix:
        :return:
        """
        is_note = False
        # 1、如果文件是 .note 类型
        if youdao_file_suffix == NOTE_SUFFIX:
            is_note = True
        # 2、如果文件没有类型后缀，但以 `<?xml` 开头
        if not youdao_file_suffix:
            response = self.youdaonote_api.get_file_by_id(file_id)
            content = response.content[:5]
            is_note = True if content == b"<?xml" else False
        return is_note
    
    # def judge_type(self, noteType: int, orgEditorType: int) -> int:
    #     """
    #     判断返回内容
    #     :param entryType: int
    #     :param orgEditorType: int
    #     :return: note_type: int
    #     """
    #     note_type = 0
            
    #     #  返回xml格式的note笔记内容,noteType == 0 and orgEditorType == 1
    #     if noteType == 0 and orgEditorType == 1:
    #         note_type = 1
    #     # 返回json格式的note笔记内容
    #     elif  (noteType == 7 or noteType == 5) and orgEditorType == 1:
    #         note_type = 2
    #     # 返回md文件内容
    #     elif  noteType == 0 and orgEditorType == 0:
    #         note_type = 3
    #     return note_type
    
    
    def judge_type(self,file_id: str ,youdao_file_suffix: str) -> int:
        """
        判断返回内容
        :param entryType: int
        :param orgEditorType: int
        :return: note_type: int
        """
        note_type = 0
        is_xml = False
        if youdao_file_suffix == ".note":
            response = self.youdaonote_api.get_file_by_id(file_id)
            content = response.content[:5]
            is_xml = True if content == b"<?xml" else False
            if is_xml:   # xml类型
                note_type = 1
            else:   # json类型
                note_type = 2
        elif youdao_file_suffix == ".md":
            note_type = 3
        else:
            print(f"文件后缀「{youdao_file_suffix}」不识别，请检查！")
        
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
        # 2、如果文件是 note 类型，将其转换为 MarkDown 类型
        if note_type == 1:
            try:
                new_file_path = YoudaoNoteConvert.covert_xml_to_markdown(file_path)
            except ET.ParseError:
                print(f'{file_path} 笔记应该为 17 年以前新建，格式为 html，将转换为 Markdown ...')
                new_file_path = YoudaoNoteConvert.covert_html_to_markdown(file_path)
            except Exception:
                print(f'{file_path} 笔记转换 MarkDown 失败，将跳过')
        elif note_type == 2:
            new_file_path = YoudaoNoteConvert.covert_json_to_markdown(file_path)
        elif note_type == 3:
            YoudaoNoteConvert.markdown_filter(file_path)
            new_file_path = file_path
        # 迁移附件和图片
        
        if  os.path.exists(new_file_path):
            pull_image = PullImages(self.youdaonote_api,self.smms_secret_token,self.is_relative_path)
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
        if modify_time < os.path.getmtime(local_file_path):
            logging.info('此文件「%s」不更新，跳过', local_file_path)
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
        name = name.replace('\n','')
        # 去除换行符
        name = name.strip()
        # 替换一些特殊符号
        name = regex_symbol.sub('_', name)
        name = del_regex_symbol.sub('', name)
        return name


if __name__ == '__main__':
    start_time = int(time.time())
    try:
        youdaonote_pull = YoudaoNotePull()
        # data = youdaonote_pull._optimize_file_name(' \/":|*?#())<> []  你(好) (he#l**o|)s')
        # print(data)        
        ydnote_dir_id, error_msg = youdaonote_pull.get_ydnote_dir_id()
        if error_msg:
            print(error_msg)
            sys.exit(1)
        print('正在 pull，请稍后 ...')
        youdaonote_pull.pull_dir_by_id_recursively(ydnote_dir_id, youdaonote_pull.root_local_dir)
    except requests.exceptions.ProxyError as proxyErr:
        print('请检查网络代理设置；也有可能是调用有道云笔记接口次数达到限制，请等待一段时间后重新运行脚本，若一直失败，可删除「cookies.json」后重试')
        traceback.print_exc()
        print('已终止执行')
        sys.exit(1)
    except requests.exceptions.ConnectionError as connectionErr:
        print('网络错误，请检查网络是否正常连接。若突然执行中断，可忽略此错误，重新运行脚本')
        traceback.print_exc()
        print('已终止执行')
        sys.exit(1)
    # 链接错误等异常
    except Exception as err:
        print('其他错误：', format(err))
        traceback.print_exc()
        print('已终止执行')
        sys.exit(1)

    end_time = int(time.time())
    print('运行完成！耗时 {} 秒'.format(str(end_time - start_time)))
