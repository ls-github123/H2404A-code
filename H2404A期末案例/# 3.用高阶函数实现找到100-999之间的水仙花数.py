# 3.用高阶函数实现找到100-999之间的水仙花数
num_list = []
for i in range(100,1000):
    num_list.append(i)
ret = filter(lambda x:int(str(x)[0]) ** 3 + int(str(x)[1]) ** 3 + int(str(x)[2]) ** 3 == x, num_list)
print(f'filter函数查找数字100-999之间的水仙花数为:{tuple(ret)}')