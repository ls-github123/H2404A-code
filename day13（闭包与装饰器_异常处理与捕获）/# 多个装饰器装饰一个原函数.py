# 多个装饰器装饰一个原函数
# 执行顺序:开始从上往下开始，结束从下往上结束
def outer1(f):
    def inner():
        print('这是我的装饰器1的开始')
        f()
        print('这是我的装饰器1的结束')
        
    return inner

def outer2(f):
    def inner():
        print('这是我的装饰器2的开始')
        f()
        print('这是我的装饰器2的结束')
    return inner

@outer1
@outer2
def func():
    print('我是原函数')
func()