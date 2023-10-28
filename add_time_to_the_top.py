import os
import time

# 指定要遍历的目录
directory = './obsidian'


# 遍历目录下的所有 .md 文件,顶部添加时间。暂只支持Linux
# 执行此脚本前，如有需要可以先手动得到一份结构文件
# tree -D --timefmt="%Y-%m-%d %H:%M:%S" > original_file_tree.txt

for root, dirs, files in os.walk(directory):

    for file in files:
        if file.endswith('.md'):
            # 构建文件的完整路径
            file_path = os.path.join(root, file)

            # 获取文件的创建时间和修改时间
            st = os.stat(file_path)
            created_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(st.st_atime))
            modified_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(st.st_mtime))

            # 读取文件内容
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # 在文件内容顶部添加时间信息
            time_info = f"> Created on {created_time}\n> Modified on {modified_time}\n\n"
            content = time_info + content

            # 将更新后的内容写回文件
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)

            # 假设把md文件交给git管理，那么修改文件后把时间还原就没有意义了

print("时间信息已添加到所有 .md 文件的顶部。")

