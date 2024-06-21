# 3.定义给列表增加10个10-900之间随机整数
import random
def outer1(f):
    def inner(x):
        sort = sorted(f(x), reverse=True)
        return f'装饰器返回降序排序后为{sort},最大值数据+1000返回为:{max(sort) + 1000}' 
    return inner

@outer1
def func(numlist):
    print(f'列表中的最大值为:{max(numlist)}')
    return numlist
numlist = []
for i in range(10):
    i = random.randint(10,900)
    numlist.append(i)
print(numlist)
print(func(numlist))