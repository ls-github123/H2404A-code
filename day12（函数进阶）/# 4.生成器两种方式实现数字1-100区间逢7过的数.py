# 4.生成器两种方式实现数字1-100区间逢7过的数
ret1 = (i for i in range(1,101) if i % 7 == 0 or '7' in str(i))
print(f'1.推导式方法实现数字1-100区间逢7过的数为:{tuple(ret1)}')

def func():
    for i in range(1,101):
        if i % 7 == 0 or '7' in str(i):
            yield i
print(f'2.for-in方法实现数字1-100区间逢7过的数为:{list(func())}')