# 4.读取一个文件，输出除了以#号开头的行的内容
import re
with open('(#).txt', 'r', encoding='utf8') as file:
    data = file.readlines()
for char in data:
    if not char.startswith('#'):
        print(char)