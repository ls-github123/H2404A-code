# 1.迭代器实现往列表中增加数据，输出所有数据
class IterList:
    def __init__(self):
        self.list1 = []
        self.index = 1
    
    def add(self, num):
        self.list1.append(num)
        
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index < len(self.list1):
            num = self.list1[self.index]
            self.index += 1
            return num
        else:
            raise StopIteration # 定义异常处理
        
iterlist = IterList()
for num in range(10):
    iterlist.add(num)

for i in iterlist:
    print(i)