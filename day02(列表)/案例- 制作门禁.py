# 制作门禁：
# 现有一小区，住户的人数未进行统计；
# 要求所有住户将自己的名字录入到门禁中，便于更好的管理
# 最后打印门禁中的内容即可
# 案例提示：
# 门禁系统的数据类型是什么？
# 如何实现让多个用户将输入的数据加到门禁中？

list_user_name = []

while True:
    model_choice = input('请输入要使用的功能序号(1 -添加住户姓名; 2 -输入业主姓名,验证身份):')
    if model_choice == '1':
        while True:
            user_name = input('添加住户姓名(输入 E 退出):')            
            if user_name.upper() == 'E':   
                print(list_user_name)
                break
            else:
                list_user_name.append(user_name)
    elif model_choice == '2':
        while True:
            user_id = input('请输入业主姓名,验证身份:')
            if user_id in list_user_name:
                print(f'欢迎{user_id}业主回家')
                break
            else:
                print('不是本小区人员,禁止入内!')
    else:
        print('输入的值无效,请重新输入!')