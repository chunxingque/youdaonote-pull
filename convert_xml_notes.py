import os
import sys

# 将当前目录加入环境变量，以便能导入 core.convert
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(BASE_DIR)

from core.convert import YoudaoNoteConvert

def convert_xml_notes(directory):
    count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # 忽略已有后缀名的文件，只处理可能为无后缀的 XML 文件
            if '.' not in file:
                try:
                    with open(file_path, 'rb') as f:
                        header = f.read(10)
                        
                    if header.startswith(b'<?xml'):
                        print(f"正在转换: {file_path}")
                        YoudaoNoteConvert.covert_xml_to_markdown(file_path)
                        count += 1
                except Exception as e:
                    print(f"处理文件 {file_path} 时出错: {e}")
                    
    print(f"转换完成，共将 {count} 个 XML 笔记文件转换为 .md 格式。")

if __name__ == "__main__":
    notes_dir = os.path.join(BASE_DIR, 'youdaonote')
    convert_xml_notes(notes_dir)
