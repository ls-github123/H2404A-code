# 闭包与装饰器

# 闭包
# 1.内外函数嵌套
# 2.内函数引用外函数作用域下的非全局变量
# 3.外函数返回内函数
def outer():
    # 嵌套作用域 --> 外函数的作用域下
    a = 1
    def inner():
        # 内函数引用外函数作用域下的非全局变量
        print(a)
    # 外函数返回内函数对象(内函数对象--内函数名)
    return inner
# 调用闭包
# 函数名() == inner
# 函数名()() ==inner()
outer()() # -->  1

# 定义闭包第二种方式
# 内外函数嵌套
def outer1(x):
    # 外函数携带的参数 --> 外函数作用域下的非全局变量
    def inner1():
        # 内函数引用外函数作用域下的非全局变量
        print(x)
    # 外函数返回内函数调用 --> 仅用于定义闭包
    return inner1()
# 调用闭包
# outer1() == inner1()
outer1(666) # --> 666

# 闭包案例:闭包实现猜字谜游戏
# 给定一个谜底,给用户三次机会实现猜数字
# 或大或小都给提示，正确即结束
def outer_num():
    def inner_num():
        num = 10
        count = 0
        while count < 3:
            a = int(input('请输入谜底:'))
            if a == num:
                print('猜对了')
                break
            elif a < num:
                print('小了')
                count += 1
            elif a > num:
                print('大了')
                count += 1
    return inner_num
# 调用
# outer_num()()


# 装饰器
# 作用:在不改变原函数的基础上给函数增加新的功能
# (利用了闭包思路，本质上是一个内部闭函数)
# 应用场景:引入日志、函数执行时间统计、执行函数前预备处理
# 执行函数后清理功能、权限校验等场景

# 一个装饰器装饰一个原函数
def outer(f):
    def inner():
        print('请进行自我介绍')
        # 让原函数执行 --> 函数名() --> func() --> f()
        f()
        print('介绍的非常好,下次不要了')
    return inner

# 原函数
# 装饰器装饰某一个原函数,将原函数的函数名作为装饰器的实参传递
# @outer() == outer(原函数函数名)() == outer(func)()
@outer
def func():
    print('我叫张三')
func()

# 案例
# 定义一个原函数--> 获取100-900之间的回文偶数，如果区间内有满足条件的数据则打印
# 定义一个装饰器 -->统计原函数执行时间
import time
def outer1(func1):
    def inner():
        s_time = time.time()
        func1()
        e_time = time.time()
        r_time = e_time - s_time
        if r_time < 0.02:
            print(f'{r_time}')
            print('非一般的速度')
        else:
            print('太慢了!')
    return inner

@outer1
def func1():
    list_num = []
    for i in range(100,1000):
        if str(i) == str(i)[::-1]:
            list_num.append(i)
    if len(list_num) == 0:
        print('区间内没有满足条件的数据')
    else:
        print(f'数字100-999之间满足条件的数字为:{list_num},共有{len(list_num)}个')
func1()


# 装饰器装饰一个带参数的原函数
# 如果原函数带参数，要求内函数也要带参数 --> 形参参数数量一致即可
# 要求内函数中原函数的调用也要传参 --> 与内函数中参数数量和参数名均需保持一致
def outer2(func2):
    def inner(name):
        print('请进行自我介绍')
        func2(name)
        print('介绍的非常好,下次不要了')
    return inner
    
@outer2
def func2(name):
    print(f'我叫({name})')
func2('张三')

# 案例:用户任意传递两个数字,原函数实现打印两个数字的和
# 装饰器:在原函数进行求和操作之前输出'准备进行求和操作'
# 原函数求和结束后输出'求和操作结束'
def outer3(func3):
    def inner(num1, num2):
        print('准备进行求和操作')
        func3(num1, num2)
        print('求和操作结束')
    return inner

@outer3
def func3(num1, num2):
    print(f'两个数字:{num1, num2},和输出为:{num1 + num2}')
# num1 = int(input('输入第一个数字:'))
# num2 = int(input('输入第二个数字:'))
# func3(num1, num2)


# 装饰器装饰带返回值的原函数
# (要求内函数中也要有返回值)
def outer4(f):
    def inner():
        return '<h1>' + f() + '</h1>'
    return inner
@outer4
def func4():
    return '我是张重量'
print(func4())

# 定义一个原函数,列表中增加10个5-100之间的随机整数，返回列表中的最大值
# 定义一个装饰器:输出列表中的最大值+1000的结果
import random
def outer5(f):
    def inner():
        return f'列表中的最大值+1000的结果为:{f() + 1000}'
    return inner
@outer5
def func5():
    list_num = []
    for i in range(10):
        list_num.append(random.randint(5,100))
    print(f'随机生成的10个5-100之间的整数为:{list_num}')
    return max(list_num)
print(func5())

# 装饰带参数和返回值的原函数
# 原函数:进行自我介绍 --> 返回自我介绍
# 装饰器:给原函数返回值加<h3>标签 
def outer6(f):
    def inner(func7_list):
        return '<h3>' + f(func7_list) + '</h3>'
    return inner
@outer6
def func6(name):
    return f'我叫{name}'
# name = input('输入姓名:')
# print(func6(name))


func7_list = []
for i in range(10):
    func7_list.append(random.randint(10,100))
def outer7(f):
    def inner(func7_list):
        func7_list.sort(reverse = True)
        data = f(func7_list) + 1000
        return func7_list, data
    return inner
@outer7
def func7(func7_list):
    return min(func7_list)
print(func7(func7_list))


# 装饰带不定长参数的原函数
# 原函数:用户传递任意多个数字，要求原函数对所有数据进行求和输出
def outer8(f):
    def inner():
        print('开始求和操作')
        f()
    return inner

def func8(*args):
    print(f'输出和为:{sum(args)}')
func8(5,6,7,8,9,10,11,12)
