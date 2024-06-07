# 案例-封装
class Myclass:
    def __init__(self):
        self.money = 200
        # 将属性设置为私有属性:在属性名前加 __
        self.__mimi = '一个小秘密'
    
    # 方法设置为私有方法:方法名前__  
    def __car(self):
        print('一辆黑色的小汽车')
    
    # 在一个实例方法中获取实例属性 self.属性名()
    # 在一个实例方法中调用另外一个实例方法:self.方法名()
    def publiccar(self):
        self.__car()
        
    # 获取私有属性：定义一个公共的实例方法
    def get_mimi(self):
        print(f'我的小秘密是:{self.__mimi}')
    
    # 修改私有属性:定义一个公共的实例方法，在方法中实现对属性的值进行修改
    def set_mimi(self, greatmimi):
        # self.属性名 = 属性值
        self.__mimi = greatmimi
        print(self.__mimi)
        
my = Myclass()
print(my.money)
# print(my.__mimi)
my.publiccar()
my.get_mimi()
my.set_mimi('一个大秘密')
