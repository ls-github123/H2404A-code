# 让用户输入自己的出生年份，统计从自己出生年份到今年之间的闰年，将所有的闰年存放在列表中；
# 	判断这个区间是否有满足条件的数据，
# 	如果有，则输出输出满足条件数据及个数
# 	如果没有，则输出区间没有满足条件的数据

while True:
    list_birthyear = []
    user_birthyear = input('请输入用户出生年份:')
    for year in range(int(user_birthyear), 2025):
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            list_birthyear.append(year)

    if len(list_birthyear) > 0:
        print(f'用户出生年份 {user_birthyear} 至 今年(2024) 之间的闰年为:{list_birthyear},共有 {len(list_birthyear)} 年')
    else:
        print(f'用户出生年份 {user_birthyear} 至 今年(2024) 区间内没有满足条件的数据!')