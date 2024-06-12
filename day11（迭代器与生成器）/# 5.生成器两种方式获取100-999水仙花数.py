# 5.生成器两种方式获取100-999之间水仙花数
tuple1 = (i for i in range(100,1000) if int(str(i)[0]) ** 3 + int(str(i)[1]) ** 3 + int(str(i)[2]) ** 3 == i)
print(f'1.集合推导式获取数字100-999之间的水仙花数为:{tuple(tuple1)}')



def func():
    for i in range(100,1000):
        if int(str(i)[0]) ** 3 + int(str(i)[1]) ** 3 + int(str(i)[2]) ** 3 == i:
            yield i           
print(f'2.函数yield方式获取数字100-999之间的水仙花数为:{list(func())}')