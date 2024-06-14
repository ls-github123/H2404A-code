# 5.alist = [12, 32, 24, 58, 76, 17, 98],将alist作为参数传入原函数，
# 在原函数内部将列表中的最大值进行返回；
# 定义装饰器函数，在装饰器中对该列表降序排序返回，并将最大值加1000返回
def outer(f):
    def inner(x):
        sort = sorted(f(x), reverse = True)
        return f'装饰器返回列表alist数据降序排序为:{sort}'
    return inner
@outer
def func(alist):
    print(f'原函数返回列表alist数据中最大值+1000为:{max(alist) + 1000}')
    return alist

alist = [12, 32, 24, 58, 76, 17, 98]
print(func(alist))