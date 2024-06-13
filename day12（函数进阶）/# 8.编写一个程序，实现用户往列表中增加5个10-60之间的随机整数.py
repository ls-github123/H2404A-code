# 8.编写一个程序，实现用户往列表中增加5个10-60之间的随机整数
# (1)要求使用高阶函数和匿名函数实现获取所有数的平方
# (2)要求使用高阶函数和匿名函数实现对所有平方进行求和
# (3)要求使用高阶函数和匿名函数实现获取所有平方数中的奇数
# (4)要求使用高阶函数实现对所有的平方数进行降序排序
import random
from functools import reduce
list_user = []
for i in range(5): # 循环5次
    list_user.append(random.randint(10,60)) # 使用random模块随机获取10-60之间的一个整数，存入列表list_user

print(f'随机获取5个10-60之间的随机整数为:{list_user}')

ret1 = map(lambda i:i**2, list_user)
data = list(ret1)
print(f'1.使用高阶函数和匿名函数获取所有数的平方,输出为:{data}')

ret2 = reduce(lambda a,b:a + b, data)
print(f'2.使用高阶函数和匿名函数对所有数的平方求和为:{ret2}')

ret3 = filter(lambda i : i % 2 != 0, data)
print(f'3.使用高阶函数和匿名函数获取所有平方数中的奇数为:{tuple(ret3)}')

ret4 = sorted(data, reverse = True)
print(f'4.使用高阶函数实现对所有平方数降序排序输出为:{ret4}')