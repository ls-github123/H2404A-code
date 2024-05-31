# 4.定义一个函数，函数功能实现让用户随机输入一个字符串
# 找到这个字符串中出现次数最多的字符及该字符出现的次数
def count_str(str1):
    dict_char = {}
    for char in str1:
        dict_char [char] = str1.count(char)
    max_count = max(dict_char.values())
    most_frequent_chars = [k for k ,v in dict_char.items() if v == max_count]
    return f'字符串中出现次数最多的字符为:{', '.join(most_frequent_chars)},出现次数为: {max_count} 次'

while True:
    str1 = input('随机输入一个字符串:')
    print(count_str(str1))