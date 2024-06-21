# 2.两个装饰器装饰一个原函数
def outer2(f):
    def inner():
        return '<a>' + f() + '</a>'
    return inner

def outer1(f):
    def inner():
        return '<h3>' + f() + '</h3>'
    return inner

@outer1
@outer2
def func():
    return '我是法外狂徒张三'
print(func())