# python 用户输入一个数，判断这个数是否为质数

num = int (input ('请输入一个整数：'))
y = 0

for x in range (1,num+1,1):

    if num % x == 0: # 判断当前x是否为输入数字num的因数

        y += 1

if y == 2:  # 如果y=2，说明输入数字num只有2个因数，即数字1和它本身，符合质数判断条件

 print (f'数字 {num} 为质数')

else:

 print (f'数字 {num} 不是质数')