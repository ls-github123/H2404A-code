# 用户任意输入一个字符串
# 字符作为单独的键，字符在字符串中出现的次数作为值
while True:
    str1 = input('请任意输入一个字符串:')
    dict1 = {}
    for char in str1:
        dict1[char] = str1.count(char)
    print(dict1)

    # 获取字符串中出现次数最多的字符及该字符出现的次数
    max_char = max (dict1.values())
    max_key = [i for i,j in dict1.items() if j == max_char]
    print(f'出现次数最多的字符为:{max_key}')
    print(f'出现的次数为:{max_char}')