# python-循环嵌套 99乘法表打印

# 定义变量 x 为横向轴坐标，变量 y 为纵向轴坐标

for y in range (1,10,1): # 外层循环-y轴

    for x in range (1,y+1,1): # 内层循环-x轴
        
        print (f'{x} x {y} = {x*y}',end = ' / ')

    print () #换行打印