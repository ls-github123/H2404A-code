# 2.迭代器实现往列表中任意增加数据，倒序输出所有数据
class IterList:
    def __init__(self):
        self.list = []
        self.index = 0
        
    def add(self,num):
        self.list.append(num)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < 1:
            num = self.list[self.index]
            self.index += 1
            return self.list[::-1]
        else:
            raise StopIteration
        
iterlist = IterList()
iterlist.add(1)
iterlist.add(2)
iterlist.add(3)
    
for num in iterlist:
    print(num)