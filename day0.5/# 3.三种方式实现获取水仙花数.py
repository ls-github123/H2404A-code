# 获取水仙花数
# 1.通过算术运算符获取个位、十位、百位数
list_1 = []
for i in range(100,1000):
    ge = i % 10
    shi = i // 10 % 10
    bai = i // 100
    if ge ** 3 + shi ** 3 + bai ** 3 == i:
        list_1.append(i)
print(f'算术方法获取到的水仙花数为:{list_1}')

# 2.通过嵌套循环获取个位十位百位上的数0
list_2 = []
for i in range(1,10):
    for j in range(10):
        for k in range(10):
            if k**3 + j**3 + i**3 == i*100 + j*10 + k:
                list_2.append(i*100 + j*10 + k)
print(f'嵌套循环方式获取到的水仙花数为:{list_2}')

# 3.通过索引获取个位、十位、百位上的数
list_3 = []
for i in range(100,1000):
    num = str(i)
    if int(num[0]) ** 3 + int(num[1]) ** 3 + int(num[2]) ** 3 == i:
        list_3.append(int(num))
print(f'通过索引方式获取到的水仙花数为:{list_3}')
