# python-project while循环 求1-100间所有奇数的和

num = 0
sum = 0 

while num <= 100:
    if num % 2 == 1:
       sum += num
    num += 1

print (sum)