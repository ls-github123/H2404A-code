# 3.迭代器生成斐波那契数列
class FibonacciIterator:
    def __init__(self, max_count):
        self.max_count = max_count  # 要生成的斐波那契数列的最大个数
        self.count = 0  # 初始化计数器
        self.a, self.b = 0, 1  # 定义初始值

    def __iter__(self):
        return self  # 返回迭代器对象本身
    
    def __next__(self):
        if self.count < self.max_count:
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return result
        else:
            raise StopIteration # 定义异常处理

# 调用
max_count = int(input('输入要获取的斐波那契数个数:'))
fib_iter = FibonacciIterator(max_count)
list_num = []
for num in fib_iter:
    list_num.append(num)
print(f'获取的{max_count}个斐波那契数列数为:{list_num}')
