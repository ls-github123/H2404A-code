# 8、定义一个函数，实现获取100-999之间的水仙花数
# 将所有的水仙花数存放在列表中；判断区间内是否有满足条件的数据
# 如果有则输出并统计数量；没有则输出”区间内没有满足条件的数据”；
# 要求函数功能实现统计整个程序的运行时长
# 如果时长小于0.01则输出”速度真快！”，否则输出”这也太慢了
import time
start_time = time.time()
num_list = []
for i in range(100,1000):
    if int(str(i)[0]) ** 3 + int(str(i)[1]) ** 3 + int(str(i)[2]) ** 3 == i:
        num_list.append(i)
if len(num_list) == 0:
    print('数字100-999区间内没有满足条件的数据')
else:
    print(f'数字100-999区间的水仙花数为:{num_list},共有:{len(num_list)}个')
end_time = time.time()
running_time = end_time - start_time
print(f'程序运行时长:{running_time}')
if running_time < 0.01:
    print('速度真快!')
else:
    print('太慢了!')