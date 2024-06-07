# 继承-案例
class GrandFather:
    def __init__(self):
        self.money = '一个亿'
    
    def house(self):
        print('一栋中式大别墅')
        
class Father(GrandFather):
    def __init__(self):
        self.money = '两个亿'
        
    def house(self):
        print('欧式风格大别墅')
    
    
    # 获取父类属性
    def get_grand_money(self):
        super().__init__()
        print(f'获取到的grandfathe的money值为{self.money}')
        
    # 调用父类方法
    def get_grand_house(self):
        super().house()
       
class Son(Father):
    def __init__(self):
        self.money = 20
        
    def house(self):
        print('学校宿舍')
    
    # 获取父类money属性
    def get_father_money(self):
        super().__init__()
        print(f'获取到的father的money的值为{self.money}')
    
    def get_father_house(self):
        super().house()


son = Son()
son.get_father_house()
son.get_father_money()
son.get_grand_house()
son.get_grand_money()
print(son.money)