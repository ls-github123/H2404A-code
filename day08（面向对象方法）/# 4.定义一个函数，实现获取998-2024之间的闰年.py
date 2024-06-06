# 4.定义一个函数，实现获取998-2024之间的闰年
# 将所有的闰年存放在列表中；判断区间内是否有满足条件的数据
# 如果有则输出并统计数量；没有则输出”区间内没有满足条件的数据”；
# 要求函数功能实现统计整个程序的运行时长
# 如果时长小于0.01则输出”速度真快！”，否则输出”这也太慢了
import time
start_time = time.time()
year_list = []
for year in range(998,2025):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        year_list.append(year)
if len(year_list) == 0:
    print('998-2024区间内没有满足条件的数据')
else:
    print(f'998-2024区间的闰年为:{year_list},共有:{len(year_list)}年')
end_time = time.time()
running_time = end_time - start_time
print(f'程序运行时长:{running_time}')
if running_time < 0.01:
    print('速度真快!')
else:
    print('太慢了!')