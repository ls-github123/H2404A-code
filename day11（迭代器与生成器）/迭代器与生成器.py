# 迭代
# 代码开发中 称之为循环遍历
# 迭代是访问集合(代指一堆数据 列表元素 字符串字符)元素的一种方式


# 可迭代对象
# 表象概念: 可以被for循环所循环遍历的对象
# 本质概念: 底层拥有iter方法的对象

# 常见可迭代对象(iterable) -- 字符串、列表、元组、集合、字典

# 判断对象是否为可迭代对象
from collections.abc import Iterable
from os import lstat
from signal import raise_signal
from turtle import pen

from numpy import iterable
# isinstance(对象, 可迭代对象) 需要导包
# 判断对象是否为可迭代对象
# isinstance(对象, 类)
# 判断当前对象是否为某个类的实例
for i in {'name':'张三', 'age':18}:
    print(i)

print(isinstance(10, Iterable))
print(isinstance(10.6,Iterable))
print(isinstance(True, Iterable))
print(isinstance('hello',Iterable))

# 自定义一个可迭代对象 --> 面向对象思路实现
class MyIter:
    # 初始化生成一个空列表
    def __init__(self):
        self.list1 = []
        
    # 定义方法实现往列表中增加数据
    def add(self):
        self.list1.append('张三')
        self.list1.append('李四')
        self.list1.append('王五')
        self.list1.append('赵六')
    
    # 底层编写iter方法 __iter__   
    def __iter__(self):
        # iter方法作用:返回一个迭代器
        pass
        
my = MyIter()
my.add()
print(isinstance(my,Iterable)) # --> False
# __iter__  --> True

# iterator -- 迭代器  -- 依次获取可迭代对象中的每一个数据
# iteration -- 迭代

# 可迭代对象本质 -- 底层拥有iter方法的对象
# iter 方法: 在类中使用iter,以魔法方法的形式使用  __iter__
# 在类外使用，以普通方法的形式使用 iter()

# iter()函数和next()函数
# iter()作用:返回一个迭代器
list1 = ['张三', '李四', '王五']
# 通过iter方法获取list1的迭代器对象
ret = iter(list1)
# 调用next方法让迭代器依次获取下一个
print(next(ret))
print(next(ret))
print(next(ret))
# 如果可迭代对象中已经没有数据，此时再调用next方法会抛出 停止迭代 异常
  # print(next(ret)) # --> StopIteration
# next(迭代器) 作用: 通过迭代器next方法依次获取可迭代对象中的下一个数据

# for...in...本质
# 通过iter()函数获取可迭代对象iterable的迭代器iterator,然后对获取到的迭代器
# iterator 不断调用next()方法来获取下一个值并将其赋给item

# 迭代器的功能
# 1.返回可迭代对象中的元素
# 2.记录当前迭代位置
# 3.当迭代完成时再次迭代 抛出停止迭代异常(StopIteration)异常

# 迭代器本质
# 实现编写迭代器，底层必须拥有iter和next方法
# python要求迭代器也必须是可迭代的，要求底层必须有iter方法
# 迭代器具体功能的实现需要next方法实现


# 迭代器
# 自定义可迭代对象 --> 面向对象
print('-------- 迭代器 --------')
class MyIterable:
    def __init__(self):
        self.list1 = []
        
    def add(self):
        self.list1.append('黄子')
        self.list1.append('媛子')
        self.list1.append('张三')
        self.list1.append('罗佩奇')
    
    def __iter__(self):
        return MyItor(self.list1)
    
class MyItor:
    def __init__(self,lst):
        self.lst = lst
        self.current = 0
    
    # 可迭代对象底层必须有iter
    def __iter__(self): # iter返回一个迭代器
        # 当前底层有用iter和next,本身就是一个迭代器
        # iter方法只需要返回自己本身,自己本身就是迭代器对象
        return self
    
    def __next__(self):
        # next()作用:返回可迭代对象中的元素
        # 判断可以迭代条件 --> 一定与迭代位置有关
        # 下标范围 --> 0 ~ len()-1
        # 迭代完成再次迭代，抛出停止迭代的异常
        if self.current <= len(self.lst) - 1:
            # 返回可迭代对象中的元素 --> 列表中获取指定的元素 --> 通过下标 列表名[下标]
            data = self.lst[self.current]
            # 记录当前迭代位置 --> 下标 --> 自增
            self.current += 1
            return data
        else:
            raise StopIteration

# 实例化对象 对象名 = 类名()       
my1 = MyIterable()
my1.add()

# 验证对象是否为可迭代对象
print(isinstance(my1, Iterable))

# 迭代器获取可迭代对象中数据的三种方式:

# 1.通过for循环依次获取
for i in my1:
    print(i)

# 2.通过list()强转将可迭代对象中的数据存放在列表中返回
print(list(my1))

# 3.通过tupel()强转将可迭代对象中的数据存放在元组中返回
print(tuple(my1))
