# 5.定义三个程序
# 第一个程序的要求，让用户任意输入数字，数字数量不限制，存放在文件1.txt中(推荐一行一个)
# 第二个程序的要求，获取文件中所有的数字，判断是否是偶数，如果是则打印即可；如果一个偶数都没有则输出一个偶数都没有
# 第三个程序的要求，获取文件中所有的数据，进行降序排序，并求和
def input_num():
    while True:
        num = int(input('请任意输入数字(输入0结束):'))
        if num == 0:
            print('结束输入')
            return even_num()
        else:
            with open('1.txt', 'a', encoding='utf8') as file:
                file.write(f'{num}\n')

def even_num():
    list_evennum = []
    print('偶数判断')
    with open('1.txt','r', encoding='utf8') as file:
        num = file.readlines()
        for char in num:
            i = int(char.strip())
            if i % 2 == 0:
                list_evennum.append(i)
    if len(list_evennum) == 0:
        print('一个偶数都没有!')
        return sum_num()
    else:
        print(f'输入的数字中,偶数为:{list_evennum}')
        return sum_num()

def sum_num():
    list_allnum = []
    with open('1.txt', 'r', encoding='utf8') as file:
        num = file.readlines()
        for char in num:
            i = int(char.strip())
            list_allnum.append(i)
    sorted_numbers = sorted(list_allnum, reverse = True)
    print(f'文件中所有的数据降序排序为:{sorted_numbers},总和为:{sum(list_allnum)}')

input_num()