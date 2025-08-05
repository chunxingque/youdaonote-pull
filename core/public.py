from typing import Tuple
import json
import os
import shutil
import stat
import sys
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(BASE_DIR)
from core import logging_conf
logging_conf.init_logging()

CONFIG_PATH = 'config.json'


def covert_config(config_path: str=None) -> Tuple[dict, str]:
        """
        转换配置文件为 dict
        :param config_path: config 文件路径
        :return: (config_dict, error_msg)
        """
        config_path = config_path if config_path else CONFIG_PATH
        with open(config_path, 'rb') as f:
            config_str = f.read().decode('utf-8')

        try:
            config_dict = json.loads(config_str)
        except:
            return {}, '请检查「config.json」格式是否为 utf-8 格式的 json！建议使用 Sublime 编辑「config.json」'
        return config_dict, ''


def remove_readonly(func, path, _):
    """清除只读属性后重试删除"""
    os.chmod(path, stat.S_IWRITE)
    func(path)

def delete_folder(folder_path):
    """安全删除只读文件夹（包含子目录和文件）"""
    try:
        # 递归删除，遇到错误时调用remove_readonly处理
        shutil.rmtree(folder_path, onerror=remove_readonly)
    except Exception as e:
        logging.error(f"文件夹删除失败: {e}")