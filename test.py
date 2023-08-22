import os
import glob

file_path = "D:\\youdaonote\\obsidian/**/*.md"
# 匹配当前目录下所有的txt文件
file_list = glob.glob(file_path,recursive=True)
print(file_list)