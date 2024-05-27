# 2.查找自己出生年份至2023年之间所有闰年
# 闰年：能被4整除 但是 不能被100整除 或者 能被400整除
birth_year = int(input('请输入你的出生年份:'))
list1 = []
count = 0
for year in range(birth_year,2024):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        list1.append(year)
        count += 1
print(f'出生年份{birth_year}年 至 2023年之间的闰年为:{list1},共有{count}年')
if count == 0:
    print('区间内没有满足条件的数')