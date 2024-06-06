# 3.定义三个程序
# 第一个程序的要求，生成20个100-200之间的随机整数，要求存放在文件1.txt中(推荐一行一个)

# 第二个程序的要求，获取文件中所有的数字，判断是否是偶数，如果是则打印即可；如果一个偶数都没有则输出一个偶数都没有

# 第三个程序的要求，获取文件中所有的数据，进行降序排序，求和，并找到最大值和最小值
import random
def RandomInt():
    count = 0
    with open('1.txt', 'a' ,encoding='utf8') as file:
        while count < 20:
            file.write(f'{random.randint(100,200)}\n')
            count += 1

def AllNum():
    num_list = []
    with open('1.txt', 'r', encoding = 'utf8') as file:
        data = file.readlines()
        for i in data:
            num_list.append(int(i.strip()))
    for num in num_list:
        if num % 2 == 0:
            print(num)
    if len(num_list) == 0:
        print('一个偶数都没有!')

def AllData():
    allnum_list = []
    with open('1.txt', 'r', encoding = 'utf8') as file:
        data = file.readlines()
    for num in data:
        allnum_list.append(int(num.strip()))
    sorted_nums = sorted(allnum_list, reverse = True)
    print(f'所有数据降序排序后为:{sorted_nums},求和为:{sum(sorted_nums)},最大值为:{max(sorted_nums)},最小值为:{min(sorted_nums)}')

# 调用            
RandomInt()
AllNum()
AllData()