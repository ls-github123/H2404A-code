# 8.定义一个函数，实现制作一个住户管理系统。要求：当前系统可以存入多个住户信息。
#  1>. 让住户输入自己的姓名、单元号(例如：2单元)、房屋门牌号(例如：303)
#  2>. 要求一个房屋只录入一个住户的信息，不允许一个房屋录入多个住户(不允许数据单元号和房屋门牌号同时一致)
#  3>. 将每个房屋住户信息整理好之后录入到系统中即可

list_occupant_info = [] # 将住户信息列表定义在函数外部  -- 为全局变量
def occupant_manage_sys(**dict_occupant_info):
    for char in list_occupant_info:
        # 定义重复校验  不允许数据单元号和房屋门牌号同时一致
        if char['unit'] == dict_occupant_info['unit'] and char['number'] == dict_occupant_info['number']:
            return '住户信息已存在,不能重复录入!'
    list_occupant_info.append(dict_occupant_info)
    print('住户信息录入成功')
    return list_occupant_info
    
def occupant_process(occupant_name, occupant_unit, occupant_number):
    while True:
        if len(occupant_name) == 0 or len(occupant_unit) == 0 or len(occupant_number) == 0:
            return '住户信息录入不能为空!'
        else:
            dict_occupant_info = {'name':occupant_name, 'unit':occupant_unit, 'number':occupant_number}
            return occupant_manage_sys(**dict_occupant_info)

# 获取数据
while True:
    print('欢迎使用住户信息管理系统')
    occupant_name = input('请输入住户姓名:')
    occupant_unit = input('请输入住户单元号:')
    occupant_number = input('请输入住户门牌号:')
# 调用函数并打印结果
    print(occupant_process(occupant_name, occupant_unit, occupant_number))