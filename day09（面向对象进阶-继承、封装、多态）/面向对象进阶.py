# 面向对象进阶
# 三要素:继承、封装、多态

# 简单继承
# 在定义类时，类名后的()写入要继承的父类
# 被继承的类称之为父类、基类
# 要继承别的类的类称之为子类、派生类

# 继承 -- 子类继承父类，子类拥有了父类的属性和方法
# 减少代码的重复性，方便代码的维护和更新
class Father:
    def __init__(self):
        self。money = 200
    def house(self):
        print('一栋大house')    

class Son(Father):
    pass

s = Son()
print(s。money)
s。house()

# 单继承  -- 一个子类继承一个父类
# 多继承 -- 一个子类继承多个父类  继承顺序:__mro__:查询子类继承顺序
# 如果子类中有init，且继承的多个父类中都编写了init,初始化自己本身的的init,所有的父类都不执行
# 如果子类中没有init，且继承的多个父类中都编写了init，初始化第一个父类的init，其他父类的init都不执行
# 如果子类中没有init，且继承的第一个父类没有init，其余多个父类中都编写了init,初始化第二个父类的init
# 以此类推   当其余类的init不进行初始化，就无法获取其余类中的属性
 
    # 如果第一个子类没有kongfu属性，第二个父类有，子类无法获取kongfu，因为只会执行第一个父类的init
    # 此时，子类获取属性，只能获取第一个父类的属性，其余父类的属性都无法获取 
    
# 如果多个父类的方法同名，子类按照mro顺序继承方法
# 如果多个父类有不同名的方法，子类按照mro顺序继承方法，哪一个父类中有，就调用哪一个父类中的方法

class Master: # 老师傅类
    def __init__(self):
        self。kongfu = '古法煎饼果子配方'
        self.m_money = 2000
        
    def make_cake(self):
        print(f'利用{self.kongfu}制作古法煎饼果子')

class School:  # 学校类
    def __init__(self):
        self。kongfu = '现代煎饼果子配方'
        self.s_money = 20000
    
    def make_cake(self):
        print(f'利用{self.kongfu}制作现代煎饼果子')


# 子类重写父类方法 --> 在子类中重新编写与父类中同名的方法
# 此刻子类默认获取自己类中的方法
class Cat(School, Master):  # 大猫类
    def __init__(self):
        self。kongfu = '猫式煎饼果子配方'
        
    def make_cake(self):
        print(f'利用{self.kongfu}制作猫式煎饼果子')
        
    # 定义一个方法，实现获取school类中的同名属性和方法
    def new_make_cake(self):
        # 子类获取父类同名的属性:super().__init__()
        super().__init__()
        print(self。kongfu)
        # 子类调用父类同名属性:super().方法名()  -- >推荐使用super()
        # super()不支持执行多个父类的方法 --> 一般应用于单继承的多层继承
        super().make_cake()
        
    # 定义一个方法，实现获取master类中的同名属性和方法
    def old_make_cake(self):
        # 子类获取父类同名属性:类名.__init__(self)
        Master.__init__(self)
        print(self.kongfu)
        # 子类调用父类同名的方法:类名.方法名()
        Master().make_cake()
        

cat = Cat()
print(cat。kongfu)
cat.make_cake()
cat.new_make_cake()
cat.old_make_cake()


# 封装
# 将对象的属性和实现细节隐藏封装，仅对外提供公共的访问方式
# 优点:提高代码安全性
# 一般使用私有属性和私有方法实现封装

# 私有属性
# 私有属性和私有方法都无法使用对象进行调用获取
# 可用来处理内部的事务，在类内部随意使用


# 多态
# 不同的子类对象调用不同的父类方法产生不同的执行结果
# 定义时的类型与运行时的类型不一样，主要应用于java\c等强类型语言
# 多态存在的必要条件，继承与方法重写
# python中的多态是弱化类型

class Father:
    def car(self):
        print('一辆黑色的小汽车')

class Son1(Father):
    def car(Self):
        print('一辆绿色的小汽车')

class Son2(Father):
    def car(self):
        print('一辆蓝色的小汽车')
        
def func(name):
    name.car()
    
son1 = Son1()
son1。car()
son2 = Son2()
