# 函数进阶

# 匿名函数 --> lambda函数
# 函数对象 = lambda 形参:表达式
# 函数对象(实参)

# 注意:函数表达式默认以返回值形式返回
f1 = lambda x:f'这是一个有参数有返回值的lambda函数'

def func1(a):
    print(f'这是一个有参数无返回值的def函数,参数为{a}')
func1(10)

def func2(x):
    return f'这是一个有参数有返回值的def函数,参数为{x}'
print(func2(5))


# 四大高阶函数
# 当一个函数可接收另一个函数作为参数时，称为高阶函数
# 高阶函数中的参数必须要有返回值

# map()
# map(函数, 可迭代对象)
# 作用:将函数依次作用于可迭代对象中的每一个元素上

list1 = [1,3,5,7,9]
def func(x):
    return x ** 2
ret = map(func, list1)
print(list(ret))

# 使用高阶函数将列表中所有的数据转换成字符串类型的数据
# 存放在一个新的元组中返回
def func_str(x):
    return str(x)
ret2 = map(func_str,list1)
print(tuple(ret2))


# reduce()
# reduce(函数, 可迭代对象)
# 对可迭代对象中的数据进行累积操作，返回结果为具体值
# 调用时需要导包 from functools import reduce

# 使用高阶函数对列表中的数据进行求和
# 第一次 a = 1  b = 3 1 + 3 = 4
# 第二次 a = 4  b = 5  1 + 3 + 5 = 9
# ......
from functools import reduce
def func_sum(a, b):
    return a + b
ret3 = reduce(func_sum, list1)
print(ret3)

# 使用高阶函数实现求10的阶乘
list2 = [i for i in range(10,0,-1)]
def func_10(a, b):
    return a * b
ret4 = reduce(func_10,list2)
print(f'10的阶乘为:{ret4}')


# filter()
# filter(函数, 可迭代对象)
# 对可迭代对象中的数据进行过滤,仅保留满足条件的数据
# 返回结果为一个迭代器
list3 = [i for i in range(1,51)]
def func_filter(i):
    return i % 7 == 0 or '7' in str(i)
ret5 = filter(func_filter, list3)
print(f'数字1-50之间逢7过的数为:{tuple(ret5)}')

# 使用高阶函数实现获取100-999之间的水仙花数，数字存放在列表中返回
list4 = [num for num in range(100,1000)]
def func_num(i):
    return int(str(i)[0]) ** 3 + int(str(i)[1]) ** 3 + int(str(i)[2]) ** 3 == i
ret6 = filter(func_num, list4)
print(f'数字100-999之间的水仙花数为:{tuple(ret6)}')



# sort() 列表排序方法
# 语法: 列表名.sort(key, reverse)
# 作用:不指定任何参数默认升序排序;指定参数reverse = True 降序排序
# key 规则:将列表中的数据按照指定的规则进行排序

# sorted()
# sorted(可迭代对象, key排序规则, reverse指定升降序)
# 作用:对可迭代对象中的数据按照指定排序规则进行升降序排序(默认升序)
list5 = [-1, 0, 3, -4, 5, -6, 7]
def func_abs(i):
    return abs(i)
ret7 = sorted(list5, reverse = True, key = func_abs)
print(ret7)


# 枚举函数
# enumerate()
# 语法:enumerate(可迭代对象)
# 作用:获取可迭代对象中的每一个元素及序号
ret_enumerate = enumerate(list1, start = 11)
for i, j in ret_enumerate:
    print(i, j)
    

# 拉链函数
# zip()
# 语法:zip(可迭代对象)
# 作用:从多个可迭代对象中,按顺序读取数据，组合成一个元组,存放在新的迭代器对象中
# 以数量少的为准
list6 = ['张三','黄子','媛子','佳琪']
list7 = ['李四','佩奇','心悦','史史']
ret8 = zip(list6,list7)
for i in ret8:
    print(i)
    

# 递归函数
# 递归:在一个函数内部调用函数本身(自己调用自己)
# 编写递归函数规律:
    # 1.在定义和调用函数时传递起始值
    # 2.大范围判断(判断何时结束递归)
    # 3.实现自己调用自己(参数发生变化)

#　案例一：通过递归函数获取1-5的和
def func_recursion(x):
    if x == 5:
        return 5
    else:
        return x + func_recursion(x + 1)
print(func_recursion(1)) # --> 15
# func_recursion(1) = 1 + 2 + 3 + 4 + 5
# func_recursion(2) = 2 + 3 + 4 + 5
# func_recursion(3) = 3 + 4 + 5
# func_recursion(4) = 4 + 5
# func_recursion(5) = 5

# 案例二:通过递归函数实现获取100-1的和
def func_recursion2(x):
    if x == 1:
        return 1
    else:
        return x + func_recursion2(x - 1)
print(func_recursion2(100)) # --> 5050

# 案例三:通过递归函数实现求100以内偶数的和
def func_recursion3(x):
    if x == 100:
        return 100
    else:
        return x + func_recursion3(x + 2)
print(func_recursion3(2))

# 案例四:通过递归实现10以内的阶乘
def func_recursion4(x):
    if x == 10:
        return 10
    else:
        return x * func_recursion4(x + 1)
print(func_recursion4(1)) # --> 3628800

# 递归实现二分查找算法
# 二分查找 --> 一分为二查询 --> 加快查询速度
# 对于数据的要求:1.数据的数量无要求 2.数据的大小无要求 3.数据的排列必须是有规律的(升序或降序) 
list8 = [6,10,23,35,47,58,66,73,91,123,456,789]
# lst：指定要从哪个列表中查询数据
# n:指定要查询的数据
# start: 要查询的范围的起始下标 --> 随着二分的效果进行变化
# end：要查询的范围的结束下标 --> 随着二分的效果进行变化
def func_recursion5(lst, n, start, end):
    # 如果二分范围内已经没有数据 --> 范围内没有要查询的数据 --> 结束递归
    # 只要 end >= start, 说明范围内有数据
    if end >= start:
        # 找到中间值 中间值 = (开始+结束) / 2
        # python3中除法结果为小数,下标不存在小数,对2取整(//)
        mid = (start + end) // 2
        # 中间值 == 要查询的数据 --> 中间值就是要查询的数据 -->得到中间值下标
        if lst[mid] == n:
            return(f'要查询的数据的下标为:{mid}')
        # 中间值 <要查询的数据>  --> 去中间值右侧范围内进行查询 --> start = mid + 1
        elif lst[mid] < n:
            return func_recursion5(lst, n, mid+1, end)
        # 中间值 <要查询的数据> --> 去中间值左侧范围内进行查询 --> end = mid - 1
        elif lst[mid] > n:
            return func_recursion5(lst, n, start, mid-1)
    else:
        return '范围内没有要查询的数据'
data = int(input('请输入要查找的数据:'))
print(func_recursion5(list8, data, 0, len(list8)-1))