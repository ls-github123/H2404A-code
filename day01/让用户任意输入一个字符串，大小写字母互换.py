# 让用户任意输入一个字符串
# 将字符串中的字母进行大小写互换-->原本是大写字母需要调整为小写
str1 = str(input('请任意输入一个字符串:'))
list1 = []
for char in str1:
    if char.isupper():
        list1.append(char.lower())
    elif char.islower():
        list1.append(char.upper())
    else:
        list1.append(char)

print(f'输入的字符串 {str1} 经大小写互换后为:{''.join(list1)}')