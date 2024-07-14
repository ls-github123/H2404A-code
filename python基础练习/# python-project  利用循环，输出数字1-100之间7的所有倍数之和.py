# python-project 输出数字1-100之间，7的所有倍数之和

total = 0

print ('数字1-100之间7的所有倍数为：')

for num in range (1,101):
   
   if num % 7 == 0: # 定义7的倍数判断条件
       
       total += num 

       print (num)

print (f'所有倍数之和为：{total}')