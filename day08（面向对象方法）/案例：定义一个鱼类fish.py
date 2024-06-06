# 定义一个鱼类fish
class Fish:
    # 对象一旦创建成功,立马调用__init__
    def __init__(self,kind, weight, price):
        # 作用: 给实例对象增加实例属性
        # 每一个对象的属性值都不同，属性值不能直接写死 --> 传参
        # __init__中的形参需要在实例化过程中传递实参 类名(实参)
        self.kind = kind
        self.weight = weight
        self.price = price
        self.sumprice = self.weight * self.price
        print('我是__init__方法')
    
    # new 方法 --> 返回父类new出来的实例 -->没有继承的父类 --> 使用object顶级父类
    # cls 类对象本身
    # 作用: 类的构造器，给类实例化对象
    # __new__在__init__之前执行
    # 调用:类创建对象的过程就是执行new
    def __new__(cls, *args, **kwargs):
        print('我是new方法')
        return object.__new__(cls)
    
    # 返回对象的描述信息，如不指定值，则print(对象名)默认输出内存地址
    # # 调用：打印对象时调用str
    def __str__(self):
        return f'我是{self.kind}'
    
    # 垃圾回收释放
    # 底层内置，正常情况不需手动调用
    # 作用:在对象销毁前调用，释放资源
    def __del__(self):
        print('被删除了!')
        
    def display_info(self):
        print(f'这条鱼的品种是{self.kind},重量为:{self.weight},单价为:{self.price},买这条鱼需要花费:{self.sumprice}元')

# 实例化对象 和 实例属性
caofish = Fish('草鱼', 5.6, 25)
jiyu = Fish('鲫鱼', 8.9, 20)

# 实例对象调用实例方法
caofish.display_info()
jiyu.display_info()

print(caofish) # __str__ 返回值
print(jiyu) # __str__ 返回值

# 对象名 = Fish(参数)
# new 创建对象
# init 给创建好的对象增加属性
