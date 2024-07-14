# python for-in循环 求数字1-100之间有多少质数

count = 0

print ('由计算可知，数字1-100之间质数分别为：')

for x in range (1,101,1):
    
    num = 0
    
    for y in range (1,x+1,1):

        if x % y == 0:

            num += 1

    if num == 2: #变量num等于2时，说明循环中有2个数为x的因数，即1和它本身，此时的x为1个质数

     count += 1
     
     print (y)

print (f'数字1-100之间，共有 {count} 个质数')
     