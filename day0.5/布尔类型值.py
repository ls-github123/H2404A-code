a = 0
b = -5
c = ''
d = ' '

print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(4 > 5) # True
print(4 < 5) # False

# 逻辑运算符是根据条件的布尔类型值进行判断
# 返回结果是一个具体的值
print(0 and 7)
print(4 > 5 and 7)
print(5 < 6 and 0 and False and True)
print(0 or 7) # a不成立则返回b
print (4 > 5 or 7)
print (5 < 6 or 7)
print(5 < 6 and 7 > 8 or False and 0 or not True) # False