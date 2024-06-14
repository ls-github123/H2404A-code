# 4.装饰器文件读取数据
# 原函数功能：
# 	从文件中读取所有的数据，以列表的形式返回数字类型的数据；返回列表
# 装饰器功能：
# 	获取列表中的最小值并对使用高阶函数实现列表进行降序排序；将列表中的最小值+1000与降序后的列表返回
def outer(f):
    def inner():
        num_list = []
        for i in f():
            num_list.append(int(i.strip()))
        mindata = min(num_list)
        data = sorted(num_list, reverse = True)
        return f'文件中数据进行降序排序后输出为:{data}, 最小值+1000输出为:{mindata + 1000}'
    return inner
            
@outer
def func():
    with open('data.txt', 'r', encoding='utf8') as file:
        data = file.readlines()
    return data
print(func())