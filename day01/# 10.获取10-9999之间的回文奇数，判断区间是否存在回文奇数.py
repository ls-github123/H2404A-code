# 10.获取10-9999之间的回文奇数，判断区间是否存在回文奇数
# 如果区间有符合条件的数据则输出所有的数并统计数量
# 如果区间没有符合条件的数据则输出  "该区间没有满足条件的数"
# 回文奇数：正着读和倒着读一样的数且这个数是奇数
list_num = []
for num in range(10,10000):
    if str(num) == str(num)[::-1] and num % 2 != 0:
        list_num.append(num)
if len(list_num) == 0:
    print('数字10-9999区间内没有满足条件的数据')
else:
    print(f'数字10-9999区间内的回文奇数为:{list_num},共有:{len(list_num)}个')