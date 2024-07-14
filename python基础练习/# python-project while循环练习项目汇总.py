# python-project while循环练习项目汇总

# 1/ 输出1-100之间所有数字之和
num_1 = 1
sum_1 = 0  # 定义一个存放和的变量 sum ，赋予初始值为 0

while num_1 <= 100 :
    
    sum_1 += num_1  # sum = sum + num
    
    num_1 += 1  # num = num + 1

print (f'1-100之间所有数之和为 {sum_1}')



# 2/ 输出1-100之间所有奇数的和
num_2 = 1
sum_2 = 0

while num_2 <= 100 :
    
    if num_2 % 2 == 1:
        
        sum_2 += num_2
    
    num_2 += 1

print (f'数字1-100之间，所有奇数的和为 {sum_2}') 


# 3/ 输出1-100之间7的倍数的和
num_3 = 1
sum_3 = 0

while num_3 <= 100:
    if num_3 % 7 == 0:
        sum_3 += num_3
    num_3 += 1

print (f'数字1-100之间7的所有倍数之和为 {sum_3}')