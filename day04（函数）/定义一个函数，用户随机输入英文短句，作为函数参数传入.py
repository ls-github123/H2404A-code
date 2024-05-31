#　定义一个函数，用户随机输入英文短句，作为函数参数传入
# 整合 每一个单词及长度 的数据并返回

def str_work(str1):
    dict_work = {}
    for char in str1.strip().split():
        dict_work [char] = [len(char)][0]
    return dict_work

while True:
    str1 = input('随机输入一个字符串:')
    print(f'字符串 {str1} 中每一个单词及长度的返回值为:{str_work(str1)}')