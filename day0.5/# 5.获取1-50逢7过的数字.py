# 5.获取1-50逢7过的数字
# 逢七过：7的倍数和含有7的数
# 含有7：字符 in 字符串
list1 = []
for num in range(1,51):
    if num % 7 == 0 or '7' in str(num):
        list1.append(num)
print(f'数字1-50区间内,符合逢7过的数为:{list1},共有{len(list1)}个')
if len(list1) == 0:
    print('数字1-50区间内没有符合条件的数')