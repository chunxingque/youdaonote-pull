import os
import glob
import re


def rename_blank_name(file_dir):
    """重命名开头空格的名字

    Args:
        file_dir (_type_): _description_
    """
    file_path = f"{path_dir}/**/*.md"
    file_list = glob.glob(file_path,recursive=True)
    re_rule = re.compile(r'[\ ]')
    # print(file_list)
    for file in file_list:
        file_name = os.path.basename(file)
        is_match = re.match('\ ',file_name)
        if is_match:
            dir_name = os.path.dirname(file)
            new_name = file_name.strip()
            tmp_name = re_rule.sub('_',file_name)
            tmp_file = os.path.join(dir_name,tmp_name)
            new_file = os.path.join(dir_name,new_name)
            os.rename(file,tmp_name)
            if os.path.exists(new_file):
                os.remove(new_file)
            os.rename(tmp_name,new_file)
            print(f'[{file}] -> [{new_file}]')


if __name__ == '__main__':
    path_dir = 'D:\\obsidian\\obsidian'
    rename_blank_name(path_dir)
        





