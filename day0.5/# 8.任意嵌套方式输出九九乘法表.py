# 9.任意嵌套方式输出九九乘法表
for y in range(1,10):
    
    for x in range(1,y+1):
        
        print(f'{x} x {y} = {x * y}',end = ' / ')
    
    print()