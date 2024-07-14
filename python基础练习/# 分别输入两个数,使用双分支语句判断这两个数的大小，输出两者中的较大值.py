# 分别输入两个数,使用双分支语句判断这两个数的大小，输出两者中的较大值

print ('分别输入两个数，系统将自动判断两个数的大小，并输出两者中较大的值')
num_1 = float (input ('请输入第一个数字：'))
num_2 = float (input ('请输入第二个数字：'))

if num_1 == num_2:
    
    print ('两者值大小相等')

elif num_1 > num_2:

    print (f'第一个数字 {num_1} 值较大')

else:

    print (f'第二个数字 {num_2} 值较大') 