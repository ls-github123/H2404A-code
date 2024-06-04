# 2.用户随机输入一个全英文的字符串，判断这个字符串是否全是小写
import re
while True:
    input_str = input('随机输入一个英文字符串:')
    re_lower_str = re.match(r'^[a-z]+$', input_str) 
    # 从输入字符串开始到结束遍历，如果包含任何非小写字母或非字母字符,将返回none
    if re_lower_str:
        print(f'字符串 {input_str} 为全小写字母组成')
    else:
        print(f'字符串 {input_str} 非全小写字母组成')