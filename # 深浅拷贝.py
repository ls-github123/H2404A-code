# 深浅拷贝
# is 和 ==
# a == b: 比较运算符，判断等号两边的值是否相等
# a is b:判断a是否是b, a 和 b是否是同一个值
a = 1
b = 1.0

print(a == b) # True
print(id(a), id(b)) # a, b变量内存地址不同
print(a is b) # --> False

c = '1.6'
d = '1.6'
print(c is d) # True
print(id(c), id(d)) # c, d变量内存地址相同

a1 = ['1.6']
b1 = ['1.6']
print(a1 is b1)
print(id(a1), id(b1))


a2 = {'name':'张三'}
b2 = {'name':'张三'}
print(a2 is b2)
print(id(a2), id(b2))

# 指向关系(不可变):整型、浮点型、字符串、元组 --> 指向同一内存地址

import copy
# 浅拷贝 使用copy模块copy
# 拷贝模块 copy
# 拷贝不可变数据类型的数据  --> 毫无意义，永远指向同一内存地址
# 浅拷贝只拷贝浅层数据
a = '1.6'
b = copy.copy(a)
print(a ,b)
print(id(a), id(b))
print(a is b)

# 拷贝可变数据类型
# 拷贝后的数据与拷贝前的数据不是同一个
list1 = [1,2,3,[4,5,6],7]
list2 = copy.copy(list1)
print(list1, list2)
print(id(list1), id(list2)) # id值不同
print(list1 is list2) # False

# 对原数据浅层数据进行修改，拷贝后的数据不会随之修改
list1.append(666)
print(list1)
print(list2)


# 深层数据
print(list1[3], list2[3])
print(id(list1[3]), id(list2[3])) # id值相同
print(list1[3] is list2[3]) # True

print(list1[4], list2[4])
print(id(list1[4]), id(list2[4])) # id值相同
print(list1[4] is list2[4])# True


# 深拷贝
# 相当于在计算机内存中重新开辟一块空间，拷贝后的数据和拷贝前数据没有指向关系
# 需使用copy模块中deepcopy方法
# 不可变数据 对于赋值、浅拷贝、深拷贝毫无意义
a = 1
b = copy.deepcopy(a)

print(a, b)
print(id(a), id(b))
print(a is b)

# 可变数据类型 --> 深拷贝
list3 = [1,2,3,[4,5,6]]
list4 = copy.deepcopy(list3)
print(list3, list4)
print(id(list3), id(list4)) # id值不同
print(list3 is list4) # False

# 深层数据
print(list3[3], list4[3])
print(id(list3[3]), id(list4[3])) # id值不同
print(list3[3] is list4[3]) # False

# 对原数据的浅层数据进行修改，拷贝后的数据不会随之修改
list3.append(7)
print(list3)
print(list4)

# 对原数据的深层数据进行修改，拷贝后的数据不会随之修改
