# 5.str1="effe0.2fwrfw444.5fionoj0.0007joad",正则统计字符串中所有浮点数
import re
str1 = 'effe0.2fwrfw444.5fionoj0.0007joad'
re_float = re.findall(r'\d+\.\d+',str1)
print(f'字符串{str1}中的浮点数为:{re_float},共有{len(re_float)}个')