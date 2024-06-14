# 2.装饰器写入数据
# 装饰器功能实现：
# 将原函数列表中的数据存入文件中。一行存入一个数字
# 原函数功能实现：
# 让用户输入任意多个数字，如果输入0则停止输入，将所有的数字存放在一个列表中，将列表返回
def outer(f):
    def inner():
        for i in f():
            with open('num.txt', 'a', encoding = 'utf8') as file:
                file.write(f'{i}\n')
                file.close()
    return inner

@outer
def func():
    num_list = []
    while True:
        input_num = input('请任意输入数字(输入0结束):')
        if input_num == '0':
            print(f'返回包含所有输入数字的列表为:{num_list}')
            break
        else:
            num_list.append(input_num)
    return num_list

# 调用
func()