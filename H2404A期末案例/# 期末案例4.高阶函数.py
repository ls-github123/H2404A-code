# 4.高阶函数
from functools import reduce

numbers = range(100)
ret1 = filter(lambda x:str(x) == str(x)[::-1], numbers)
data = list(ret1)
print(f'1.高阶函数和匿名函数获取100以内的回文数为:{data}')

ret2 = map(lambda x:x*2, data)
data2 = list(ret2)
print(f'2.使用高阶函数和匿名函数实现对所有的回文数取2倍数为:{data2}')


ret3 = reduce(lambda a , b : a + b, data2)
print(f'3.使用高阶函数和匿名函数对所有2倍数求和为:{ret3}')

ret4 = sorted(data2, reverse = True)
print(f'4.使用高阶函数对所有2倍数降序排序为:{ret4}')
