# 7.制作随机点名器
# 将自己小组的成员名称录入到列表中，实现制作一个小组随机点名器
import random
list_name = ['李硕', '郭勇健','刘骏腾', '翟昶旭', '孔祺博']
while True:
    control = input('<enter>点名/<q>退出:')
    if control == '':
        name = random.choice(list_name)
        print(name)
    elif control.lower() == 'q':
        exit()
    else:
        print('输入的信息无效!')