# 字典
# 由一系列键值对组成的可变映射容器
# 键值对 item: name:张三、age:25  一一对应关系
# 键:不重复且不可变  支持不可变数据类型--整型、浮点型、字符串、元组
# 值:对值没有要求
# 映射：键与值一一对应关系
# 可变：有增删改方法 所有操作都作用于原容器


# 键:key
# 值:value
dict1 = {'name':'张三','age':25, 'gender':'男', 'girlfriend':'黄子'}
print(dict1)
print(type(dict1))

# 构造法 -- 本质是数据类型转换
# dict(键=值, 键=值...)
dict2 = dict(name = '张三', age = 25)
print(dict2)
print(type(dict2))

# 增加、修改方法 -- 有则修改、无则增加
dict1['age'] = 18
dict1['name'] = '胖琪'
print(dict1)

# 查询方法
# 1.直接通过键查询
# 字典名[键] -- 获取键对应的值,键不存在则报错
print(dict1['name'])

# get(键)  字典名.get(键,default) -- 获取键对应的值 键不存在则返回none
print(dict1.get('girlfriend'))
print(dict1.get('girl'))

# 删除数据方法
# pop() -- 字典名.pop(键)  --删除指定键对应的键值对 如果键不存在则报错
dict1.pop('gender')
print(dict1)

# clear()  -- 清空字典，空字典本身仍然存在
#dict1.clear()

# del(字典名) -- 删除整个字典，删除后字典不存在
# del 字典名[键]  --删除指定键对应的键值对，如果键不存在则报错

# 字典常用的查询方法
dict_connect = {'name':'SSH', 'verision':'2.0', 'public_key':'fniosdfdsnfojfo64','private_key':'fdsf4555'}

# keys()  -- 字典.keys()  返回一个包含字典中所有键的对象
print(dict_connect.keys())


# values() -- 字典名.values()  返回一个包含字典中所有值的对象
print(dict_connect.values())

# items()  -- 字典名.items()  返回一个包含所有(键,值)元组的对象
print(dict_connect.items())



# 循环遍历字典

# 循环遍历字典的键
for i in dict_connect.keys():
    print('循环遍历字典键')
    print(i,dict_connect[i])  # 变量i接收每一个键,dict_connect[i]获取值

# 循环遍历字典的值
for i in dict_connect.values():
    print(i)

# 循环遍历字典的键值对
for i in dict_connect.items():
    # 变量 i 接收键值对元组
    print(i)
    
for i, j in dict_connect.items():
    # 变量 i 接收所有的键
    # 变量 j 接收所有的值
    print(i,j)
    

# in     not in
# 判断键是否在字典中存在，如果在在返回true,不在则返回false
print('name' in dict_connect) # --> true