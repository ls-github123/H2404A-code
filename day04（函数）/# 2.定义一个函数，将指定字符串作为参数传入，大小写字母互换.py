# 2.定义一个函数，将字符串str1 = "5r+f9eejiojl\HUhjuhUIHjnwbBHJKGvfd"作为参数传入
# 将字符串中的小写字母变成大写，大写字母变成小写，其余符号都不变

def str_alpha(str1):
    list_str = []
    for char in str1:
        if char.isupper():
            list_str.append(char.lower())
        elif char.islower():
            list_str.append(char.upper())
        else:
            list_str.append(char)
    
    print(f"大小写互换后的字符串输出为:{''.join(list_str)}")

str1 = '5r+f9eejiojl\HUhjuhUIHjnwbBHJKGvfd'
str_alpha(str1)