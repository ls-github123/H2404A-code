# 1、 定义一个类：Person，它用来表示一个人，它包含：
# 2个实例属性：name和age（分别表示一个人的姓名和年龄）
# 用户由键盘随机输入一个字符串和正整数数字，将输入的这两个值作为Person类__init__方法的两个参数传入，并赋给类的实例属性name和age
# 4个实例方法：
# 1)show_my_life()
# 打印我的成长历程，比如如果我是2013年出生，今年10岁，则打印出类似如下结果：
# 	2013年 出生
# 	2014年 1岁 
# 	...
# 	2023年 10岁
# 2)show_leap_year()
# 	判断从我出生那一年到今年（2023年），是否含有闰年（能被4整除但不能被100整除，或者能被400整除的年份），如果有，打印出全部闰年，如果没有，则打印“没有闰年”
# 3)can_recite()
# 	输出我是XX能背诵九九乘法表，打印出9*9乘法表
# 4)show_num()
# 	表示我能打印年龄--500之间所有回文奇数以及个数
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def ShowMyLife(self):
        print('1.成长历程:')
        print(f'{self.age}年 出生')
        age = 0
        for year in range(self.age + 1, 2024):
            age += 1
            print(f'{year}年 {age}岁')
            
    def ShowLeapYear(self):
        year_list = []
        for i in range(self.age,2024):
            if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
                year_list.append(i)
        if len(year_list) == 0:
            print(f'2.出生年{self.age}年 至 2023年区间内没有满足条件的数!')
        else:
            print(f'2.出生年{self.age}至 2023年区间内的闰年为:{year_list}')
    
    def CanRecite(self):
        print(f'3.我是{self.name},能背诵九九乘法表:')
        for y in range(1,10,1):
            for x in range(1,y+1,1):
                print(f'{x} x {y} = {x*y}',end = ' / ')
            print() # 换行
            
    def ShowNum(self):
        num_list = []
        print(f'4.我能打印年龄{self.age}至500之间的回文奇数及个数')
        for num in range(self.age, 501):
            if str(num)[::-1] == str(num) and num % 2 != 0:
                num_list.append(num)
        print(f'年龄{self.age}至500之间的回文奇数为:{num_list}, 共有:{len(num_list)}个')
    
# 调用
name = input('请输入姓名:')
BirthYear = int(input('请输入出生年份:'))
age = int(input('请输入年龄:'))

Mylife = Person(name, BirthYear)
Mylife.ShowMyLife()

LeapYear = Person(name, BirthYear)
LeapYear.ShowLeapYear()

CanRecite = Person(name, age)
CanRecite.CanRecite()

ShowNum = Person(name, age)
ShowNum.ShowNum()
