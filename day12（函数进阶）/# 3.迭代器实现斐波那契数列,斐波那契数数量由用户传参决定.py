# 3.迭代器实现斐波那契数列,斐波那契数数量由用户传参决定
class Fibonacci:
    def __init__(self,max_count):
        self.max_count = max_count
        self.count = 0
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count < self.max_count:
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return result
        else:
            raise StopIteration
# 调用
max_count = int(input('请输入要获取的斐波那契数列数数量:'))
fibonacci = Fibonacci(max_count)
list_num = []
for num in fibonacci:
    list_num.append(num)
print(f'获取的{max_count}个斐波那契数输出为:{list_num}')