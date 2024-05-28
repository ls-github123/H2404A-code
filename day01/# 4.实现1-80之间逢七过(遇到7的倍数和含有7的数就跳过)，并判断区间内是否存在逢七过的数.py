#  4.实现1-80之间逢七过(遇到7的倍数和含有7的数就跳过)，并判断区间内是否存在逢七过的数
# 如果区间内存在，则输出所有的逢七过以后其余的数并统计数量
# 如果区间内不存在，则输出 "区间内没有满足条件的数据"
count = 0
list1 = []
for num in range(1,80+1):
    if num % 7 == 0 or '7' in str(num):
        count += 1
    else:
        list1.append(num)

if count == 0:
    print('区间内没有满足条件的数据')
else:
    print(f'数字1-80区间内逢7过以后其余的数为:{list1},共有:{len(list1)}个')