# 3.迭代器实现往列表中任意增加数据，倒序输出所有数据
class Data:
    def __init__(self):
        self.list = []
        self.index = -1
    
    def add(self,num):
        self.list.append(num)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= -len(self.list):
            data = self.list[self.index]
            self.index -= 1
            return data
        else:
            raise StopIteration

data = Data()
data.add(1)
data.add(2)
data.add(3)

for i in data:
    print(i)