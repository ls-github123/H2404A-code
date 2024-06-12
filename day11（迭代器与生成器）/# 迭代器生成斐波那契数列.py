# 迭代器生成斐波那契数列
class FibonacciIterator:
    def __init__(self, max_count):
        self.max_count = max_count  # 要生成的斐波那契数列的最大个数
        self.count = 0  # 当前生成的斐波那契数列的个数
        self.a, self.b = 0, 1  # 初始化斐波那契数列的前两个数

    def __iter__(self):
        return self  # 返回迭代器对象本身

    # def __next__(self):
    #     if self.count >= self.max_count:
    #         raise StopIteration  # 当达到最大个数时，停止迭代
    #     if self.count == 0:
    #         self.count += 1
    #         return self.a  # 返回第一个斐波那契数
    #     if self.count == 1:
    #         self.count += 1
    #         return self.b  # 返回第二个斐波那契数
    #     # 生成下一个斐波那契数
    #     next_value = self.a + self.b
    #     self.a, self.b = self.b, next_value  # 更新前两个数
    #     self.count += 1
    #     return next_value
    
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
