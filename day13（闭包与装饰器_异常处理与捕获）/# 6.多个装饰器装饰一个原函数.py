# 6.多个装饰器装饰一个原函数
# 原函数功能要求  
# 	返回 "我是xxx"  xxx名字由传参决定
# 装饰器1功能：
# 	给 原函数字符串增加a标签
# 装饰器2功能：
# 	给 原函数字符串增加p标签
# 要求通过装饰器装饰，最后实现效果为"<p><a>我是xxx</a></p>"
def outer2(f):
    def inner(x):
        return '<p>' + f(x) + '</p>'
    return inner
def outer1(f):
    def inner(x):
        return '<a>' + f(x) + '</a>'
    return inner

@outer2
@outer1
def func(name):
    return f'我是{name}'
print(func('张三'))