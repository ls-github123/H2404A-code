# 6.定义一个函数，实现让用户随即输入一个字符串，实现将字符串右移n位并输出
# 例如：用户输入"hello world" 右移两位以后实现输出"ldhello wor"
def move_str(str1,num):
    num = num % len(str1) # 算移动位数与字符串长度的余数--确保移动位数不会超过字符串长度
    return str1[-num:] + str1[:-num]

str1 = input('请随机输入一个字符串:')
num = int(input('请输入字符串右移的位数:'))
print(f'字符串 {str1},右移{num}位后输出的字符串为: {move_str(str1,num)}')
        