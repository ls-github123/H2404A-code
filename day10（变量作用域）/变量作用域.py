# 变量作用域
# 命名空间
# 内置命名空间、全局命名空间、局部命名空间

# 作用域
# Python 中的作用域决定了变量名称的可见性和生命周期
c = 50 # 全局作用域
def func():
    a = 30 # 嵌套作用域
    def func1():
        b = 20 # 局部作用域
        print(a,b)
    func1()
func()
# print(a)
# 内置作用域(B - Built-in)、局部作用域(L)、嵌套作用域(E)、全局作用域(G)

# LEGB法则 -- 作用域的查询顺序(就近原则)

# 全局与局部定义相同名字的变量不产生任何冲突
num = 10
def func2():
    num = 20
    print(num)
func2() # --> 20

def func3():
    print(num)
func3() # --> 10


# 修改全局变量
def func_modify():
    global num # global 换行对变量进行重新赋值
    num = 30
func_modify()
print(num)

# 修改嵌套作用域下的变量
def func1_modify():
    num = 15 # 嵌套作用域下的变量
    def func1():
        # 修改嵌套作用域下的变量  nonlocal 变量 换行对变量进行重新赋值
        nonlocal num
        num = 35 # 局部作用域下的变量
        print(num)
    func1()
    print(num)
func1_modify()
