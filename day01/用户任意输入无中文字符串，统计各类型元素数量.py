# 让用户任意输入一个无中文的字符串
# 统计字符串中字母的个数、数字的个数、其余字符的个数
while True:
    str1 = str(input('请输入一个无中文字符串:'))
    list_alpha = []
    list_digit = []
    list_str = []
    for char in str1:
        if char.isalpha():
            list_alpha.append(char)
        elif char.isdigit():
            list_digit.append(char)
        else:
            list_str.append(char)
    
    print(f'用户输入的字符串{str1}中,字母的个数为:{len(list_alpha)},数字的个数为:{len(list_digit)},其余字符的个数为:{len(list_str)}')