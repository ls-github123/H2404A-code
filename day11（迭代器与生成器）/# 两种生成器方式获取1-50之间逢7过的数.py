# 两种生成器方式获取1-50之间逢7过的数
tuple1 = (i for i in range(1,51) if i % 7 == 0 or '7' in str(i))
print(f'1. 1-50之间逢7过的数为:{tuple(tuple1)}')


def func():
    for i in range(1,51):
        if i % 7 == 0 or '7' in str(i):
            yield i
print(f'2. 1-50之间逢7过的数为:{list(func())}')

for i in func():
    print(i)