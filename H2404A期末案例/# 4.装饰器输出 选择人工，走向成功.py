# 4.装饰器输出<a><p>选择人工，走向成功</p></a>
def outer1(f):
    def inner():
        return '<a>' + f() + '</a>'
    return inner

def outer2(f):
    def inner():
        return '<p>' + f() + '</p>'
    return inner

@outer1
@outer2
def func():
    return '选择人工,走向成功'
print(func())