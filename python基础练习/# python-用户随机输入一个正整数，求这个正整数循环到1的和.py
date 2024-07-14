# python-用户随机输入一个正整数，求这个正整数循环到1的和
# 例：输入正整数6，则计算6+5+4+3+2+1的和

num = int (input ('请输入一个正整数：')) # 建立输入变量，用户输入数值，确定for循环起始位置
sum = 0

if num > 0:  # 加一个数字校验功能，使输入的数字必须为正整数，否责报数字不合法
   for x in range (num,0,-1):

    sum += x

   print (f'输入的正整数为: {num}，循环到1的和为：{sum}')

else: 
   print (f'输入的数字 {num} 不合法，输入数字必须为正整数！') 