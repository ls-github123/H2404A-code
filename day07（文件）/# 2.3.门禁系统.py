# 门禁系统
# 2.编写一个程序，让业主输入自己的名字，录入到系统中(系统使用文件user.txt即可)
# 业主数量不确定；如果业主名字输入n就停止录入操作
def access_add():
    while True:
        print('-------- 业主信息录入(停止录入请输入 n ) --------')
        UserName = input('请输入业主姓名:')
        if UserName.lower() == 'n':
            print('停止录入!')
            return access_enter()
        else:
            with open('user.txt', 'a', encoding = 'utf8') as file:
                file.write(f'{UserName}\n')
                print(f'业主({UserName})信息已录入')

# 3.编写一个程序，门禁系统长期开放。业主回家只需要在门口输入自己的名字，
# 如果输入的名字在系统中存在，则输出"欢迎xxx业主回家"；否则输出"不是本小区业主，禁止入内
def access_enter():
    while True:
        print('-------- 欢迎使用H2404A门禁系统 --------')
        print('添加业主信息,请输入字母 A :')
        UserName = input('请输入业主姓名:')
        if UserName.upper() == 'A':
            return access_add()
        else:
            with open('user.txt', 'r', encoding ='utf8') as file:
                data = file.readlines()
            if UserName + '\n' in data:
                print(f'欢迎({UserName})业主回家')
            else:
                print(f'({UserName})不是本小区业主,禁止入内!')

access_enter()