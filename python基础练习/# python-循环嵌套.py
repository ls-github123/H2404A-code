# python-循环嵌套
# 循环嵌套的核心：外层循环执行一次，内层循环执行所有

for i in range (1,4,1):
    for j in range (1,4,1):
        print ('♥', end=' ')
     
    print ()


# 打印9行正三角形
for i in range (1,10,1):

    for j in range (1,i+1,1):
        print ('*',end='')

    print ()