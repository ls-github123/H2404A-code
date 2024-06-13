# 6.迭代器实现随机获取5人姓名并输出
import random
class RandomName:
    def __init__(self):
        self.namelist = ['张三', '黄子', '媛子', '思莹',\
                         '佳琪', '思悦', '不窜', '佩奇', '嘉宜',\
                        '心悦']
        self.connect = 0 # 初始化计数器
        self.selected_names = set() # 用于记录已经选择的姓名
        # 集合中的元素有无序且不重复的特性
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.connect < 5:
            while True:
                name = random.choice(self.namelist)
                if name not in self.selected_names:  # 校验元素是否重复
                    self.selected_names.add(name) # 向集合中添加每次获取的姓名，用于校验重复性
                    self.connect += 1
                    return name
        else:
            raise StopIteration # 定义异常处理

# 调用            
randomname = RandomName()
print(f'随机获取的5个学生姓名为:{list(randomname)}')