# 5.实现随机输入字符串,如果字符串长度小于7就正常输出，否则按照保留首尾字符输出，并将中间字符的长度写在中间----如下例：
# 如 输入的是python 则正常输出 python 
# 如 输入的是hello python 则输出h10n

while True:
    str_input = input('请随机输入一段字符串:')
    if len(str_input) < 7:
        print(f'正常输出字符串:{str_input}')
    else:
        str1 = str_input[0] + str(int(len(str_input)) - 2) + str_input[-1]
        print(str1)