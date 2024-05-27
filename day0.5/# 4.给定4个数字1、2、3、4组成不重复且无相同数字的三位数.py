# 4. 给定4个数字1、2、3、4 组成不重复且无相同数字的三位数
count = 0
list1 = []
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i != j) and (j != k) and (i != k):
                list1.append([i,j,k])
                count += 1
print(f'所有符合条件的三位数为:{list1},这样的三位数共有{count}组')