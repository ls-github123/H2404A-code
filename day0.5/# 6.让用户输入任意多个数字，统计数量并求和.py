# 6.让用户输入任意多个数字，统计数量并求和
# 输入0停止，0不计入
list1= []
while True:
    num = int(input('请输入任意数字,输入0停止:'))
    if num == 0:
        print(f'输入的数字总和为:{sum(list1)},共输入了{len(list1)}个数字')
        break
    else:
        list1.append(num)