# 自动提取当前目录的名字并且做成一个txt保存当当前目录

import os

# 读取所有文件
files = os.listdir()

files.sort()

# 写入文件
with open("file_names", "w") as f:
    for i in files:
        i = i.strip(".md")
        f.write(i + "\n\n") 
