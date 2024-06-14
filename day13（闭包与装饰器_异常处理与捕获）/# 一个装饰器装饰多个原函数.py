# 一个装饰器装饰多个原函数
def outer(f):
    def inner():
        print('请进行自我介绍')
        f()
    return inner

@outer
def func1():
    print('我叫张三')
func1()

@outer
def func2():
    print('我叫李四')
func2()