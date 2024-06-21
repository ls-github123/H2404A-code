# 1.迭代器实现斐波那契
class Fibonacci:
    def __init__(self,maxcount):
        self.maxcount = maxcount
        self.count = 0
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count < self.maxcount:
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return result
        else:
            raise StopIteration # 定义异常处理

# 调用
maxcount = int(input('请输入要获取的斐波那契数个数:'))
fibnum = Fibonacci(maxcount)
list_num = []
for num in fibnum:
    list_num.append(num)
print(f'获取的{maxcount}个斐波那契数为:{list_num}')