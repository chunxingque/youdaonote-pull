#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量转换本地的 .note 文件为 .md 格式
用法：python convert_local_notes.py [目录路径]
"""

import logging
import os
import sys
import xml.etree.ElementTree as ET

# 添加项目根目录到路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(BASE_DIR)

from core.convert import YoudaoNoteConvert, jsonConvert

MARKDOWN_SUFFIX = '.md'

def judge_local_file_type(file_path: str):
    """
    判断本地文件类型
    :param file_path: 文件路径
    :return: 'json', 'xml', 'html', 'text'
    """
    with open(file_path, 'rb') as f:
        content = f.read()
    
    # 去除开头空白
    content_stripped = content.lstrip()
    
    # 检查是否为 JSON
    if content_stripped.startswith(b'{"'):
        return 'json'
    
    # 检查是否为 XML/HTML（以 < 开头）
    if content_stripped.startswith(b'<'):
        # 尝试解析为 XML
        try:
            ET.fromstring(content)
            return 'xml'
        except:
            # 如果不是有效的 XML，可能是 HTML 片段
            return 'html'
    
    # 其他情况：纯文本
    return 'text'

def convert_note_file(file_path: str):
    """
    转换 .note 文件为 .md 文件
    :param file_path: .note 文件路径
    :return: 转换后的文件路径，如果失败返回 None
    """
    if not file_path.endswith('.note'):
        return None
    
    file_type = judge_local_file_type(file_path)
    new_file_path = file_path.replace('.note', MARKDOWN_SUFFIX)
    
    try:
        if file_type == 'json':
            # JSON 格式
            new_file_path = YoudaoNoteConvert.covert_json_to_markdown(file_path, is_delete=True)
            logging.info(f"JSON 转换成功：{file_path} -> {new_file_path}")
            return new_file_path
            
        elif file_type == 'xml':
            # XML 格式
            try:
                new_file_path = YoudaoNoteConvert.covert_xml_to_markdown(file_path)
                logging.info(f"XML 转换成功：{file_path} -> {new_file_path}")
                return new_file_path
            except Exception as e1:
                # 如果 XML 转换失败，尝试 HTML 转换
                try:
                    new_file_path = YoudaoNoteConvert.covert_html_to_markdown(file_path)
                    logging.info(f"HTML 转换成功（XML 失败）：{file_path} -> {new_file_path}")
                    return new_file_path
                except Exception as e2:
                    logging.error(f"XML 和 HTML 转换都失败：{file_path}，错误：{e1}, {e2}")
                    return None
                    
        elif file_type == 'html':
            # HTML 格式
            try:
                new_file_path = YoudaoNoteConvert.covert_html_to_markdown(file_path)
                logging.info(f"HTML 转换成功：{file_path} -> {new_file_path}")
                return new_file_path
            except Exception as e:
                logging.error(f"HTML 转换失败：{file_path}，错误：{e}")
                return None
                
        else:
            # 纯文本：直接保存为 .md 文件
            with open(file_path, 'rb') as f:
                content = f.read().decode('utf-8')
            with open(new_file_path, 'wb') as f:
                f.write(content.encode('utf-8'))
            # 删除原始 .note 文件
            if os.path.exists(file_path) and file_path != new_file_path:
                os.remove(file_path)
            logging.info(f"纯文本转换成功：{file_path} -> {new_file_path}")
            return new_file_path
            
    except Exception as e:
        logging.error(f"转换失败：{file_path}，错误：{e}")
        return None

def batch_convert(directory: str):
    """
    批量转换目录中的所有 .note 文件
    :param directory: 目录路径
    """
    count = 0
    success = 0
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.note'):
                file_path = os.path.join(root, file)
                count += 1
                logging.info(f"正在转换 ({count})：{file_path}")
                result = convert_note_file(file_path)
                if result:
                    success += 1
                    
    logging.info(f"转换完成！总共 {count} 个文件，成功 {success} 个")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s  %(levelname)s %(message)s')
    
    # 默认转换 youdaonote/ 目录
    default_dir = os.path.join(BASE_DIR, 'youdaonote')
    
    if len(sys.argv) > 1:
        target_dir = sys.argv[1]
    else:
        target_dir = default_dir
        
    if not os.path.exists(target_dir):
        logging.error(f"目录不存在：{target_dir}")
        sys.exit(1)
        
    logging.info(f"开始批量转换：{target_dir}")
    batch_convert(target_dir)
