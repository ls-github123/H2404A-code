# for 循环输出数字1-20之间偶数的积

num = 1
num_x = 0 

print ('数字1-20之间的所有偶数为：') 

for x in range (1,21,1):    
  
    if x % 2 == 0:

     num *= x
     
     num_x += 1

     print (x)

print (f'共有 {num_x} 个偶数，所有偶数之积为：{num}')