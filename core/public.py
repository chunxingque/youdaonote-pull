from typing import Tuple
import json

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

        key_list = ['local_dir', 'ydnote_dir', 'smms_secret_token', 'is_relative_path']
        if key_list != list(config_dict.keys()):
            return {}, '请检查「config.json」的 key 是否分别为 local_dir, ydnote_dir, smms_secret_token, is_relative_path'
        return config_dict, ''
