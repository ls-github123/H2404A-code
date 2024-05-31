# 3.用户随机输入一个字符串作为函数参数传入
# 将字符串中的单词作作为字典的键存入，值为单词的长度
def str_dict(str1):
    dict_str = {}
    for char in str1.strip().split():
        dict_str [char] = [len(char)][0]
    return dict_str

str1 = input('请随机输入一个由英文单词组成的字符串:')
print(f'单词为键,长度为值的字典输出为:{str_dict(str1)}')