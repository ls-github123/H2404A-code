# 7.定义一个函数，将字符串str1 = "f5s684e8f1s321f3e48484efe5"当作参数传入
# 统计字符串中数字的个数，字母的个数，并求字符串中所有数字的和
def process_str(str1):
    list_alpha = []
    list_num = []
    for char in str1:
        if char.isdigit():
            list_num.append(int(char))
        elif char.isalpha():
            list_alpha.append(char)
    return f'字符串:{str1}中,数字的个数为:{len(list_num)},字母的个数为:{len(list_alpha)},所有数字的和为:{sum(list_num)}'

str1 = 'f5s684e8f1s321f3e48484efe5'
print(process_str(str1))