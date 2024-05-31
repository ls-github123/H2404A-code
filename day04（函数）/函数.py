# 函数
# 将一段具体功能性代码进行封装，封装到函数中
# 需要在哪里执行代码，调用函数即可
# 降低代码冗余，提高重用性

# 内置函数：python解释器自带，能够直接进行使用
# 自定义函数: 程序员根据自己的需要

# 定义函数  1.函数名首字母小写  2.参数可选 根据程序需求决定是否传参
def func():
    '''函数文档声明--实现九九乘法表'''
    for y in range(1,10):
        for x in range(1,y+1):
            print(f'{x} x {y} = {x * y}',end ='|')
        print() #换行

# 调用函数  函数名(参数)
func()
# 函数文档声明
help(func)

# 参数分类
# 形参 -- 形式上的参数,定义函数时传递形参
# 实参 -- 实际调用的参数,调用函数时传递实参
a = 10
print(a ** 2)


def info(name_input):
    name = name_input
    print(f'我叫{name}')

# name_input= input('输入名字:')
# info(name_input)

# 位置参数 形参与实参数量和位置一一对应
def func1(a, b):
    print(a + b)
func1(5,6)

# 关键字参数
def func2(name, age, height, weight):
    print(f'我的名字叫:{name},年龄:{age},身高:{height},体重:{weight}')

func2('张三', 18, weight = 160, height = 158) #　多个关键字参数之间可以打乱顺序
# 如果函数既有位置参数，又有关键字参数，位置参数必须位于关键字参数之前，否则报错

# 缺省参数 -- 在传递形参时以 键=值 的形式传递参数
def func3(name, age, height, weight, sex='保密'):
    print(f'我的名字叫:{name},年龄:{age},身高:{height},体重:{weight},性别:{sex}')
func3('张三',18,158,160)


# 不定长参数 --  不确定长度 --> 数量
# 1.不定长位置参数 -- *args 将所有位置参数(未命名参数)接收,存放在args元组中
def func4(*args):
    print(*args)
func4(f'*args:{1,8,9,4,6,8,6,7,25,35,34}')

# 2.不定长关键字参数 -- **kwargs  将所有关键字参数(命名参数)接收,存放在kwargs字典中
def func5(**kwargs):
    print(kwargs)
func5(name = '张三', age = 18, phone = 187, address = '海子')

def func7(*args,**kwargs):
    print(args)
    print(kwargs)
func7('京爷', 24, 101, height = 158, weight = 160)
# 位置参数必须定义在关键字参数之前，否则会报错


# 函数的返回值  --> return 值
# 获取函数的返回值 --> print(调用函数)
def func8():
    a = 8
    b = 9 # 局部变量 -- 定义在函数内，只能在函数内使用
    return a * b
print(func8() * 64)


def func10(a,b): # 定义一个函数，函数的功能实现任意两个数字进行求和
    return a ** 2 + b ** 2, a + b

# a = int(input('func10-a:'))
# b = int(input('func10-b:'))
# print(func10(a,b))

# 返回值分类
# 1.函数返回一个值   return 值
# 2.函数返回多个值   return 值1， 值2...  --多个值被存放在元组中返回
# 3.函数返回 none  (1) return none    (2) return    (3) 不写return
# 4.函数返回函数  涉及到闭包


# 保存函数返回值
# 函数执行结束后获取和结果的平方 立方 转字符串
ret = func10(5,6)
print(ret)
print(list(ret))

# return 关键字作用  1.返回函数值 2.结束函数
def func_range():
    for i in range(1,10):
        return i
print(func_range())  # ---> 1



# 函数的分类 -- 函数根据参数和返回值进行分类
# 1.无参数无返回值
def func_noself():
    print('无参数无返回值的函数')
func_noself()

# 2.无参数有返回值
def func_self():
    return '无参数有返回值的函数'
print(func_self())

# 3.有参数无返回值
def func_noreturn(a):
    print(f'有参数 {a} 无返回值的函数')
func_noreturn(10)

# 4.有参数有返回值的函数
def func_selfreturn(b):
    return f'有参数 {b} 有返回值的函数'
print(func_selfreturn(20))




# 函数的嵌套调用
str_eng = input('请输入一个英文短句:')

def func_move(str_eng):
    list1 = str_eng.split()
    print(list1)
    # 1.第一步将每一个单词及对应的长度整合成一个字典 --> 单词作为键，长度作为值
    dict_eng = {}
    for i in list1:
        dict_eng[i] = len(i)
    print(dict_eng)
    
    # 2.第二步 判断当前的长度是否为所有长度中的最大值
    for i, j in dict_eng.items():
        if j == max(dict_eng.values()):
            print(i, j)
    return i , j

print(func_move(str_eng))

# 函数的嵌套  -- 在一个函数内定义另外一个函数
def outer():
    def inner():
        pass
    
# 函数的嵌套调用
def func_one():
    print('这是函数one的开始')
    
    func_two()
    print('这是函数one的结束')
        
def func_two():
    print('这是函数two的开始')
    print('这是函数two的结束')

func_one()