# 定义函数，用户随机输入字符串，将用户输入的字符串作为参数传入
# 将字符串中的字符作为字典的键，字符出现的次数作为字典的值，输出字典

def dict_str(user_str):
    dict_user = {}
    for char in user_str:
        dict_user[char] = user_str.count(char)
    print(dict_user)

while True: 
    user_str = input('请随机输入一个字符串:')
    dict_str(user_str)