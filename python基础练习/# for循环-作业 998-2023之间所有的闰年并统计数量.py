# for循环-作业 998-2023之间所有的闰年并统计数量
# 闰年的判断规则：能够被4整除但不能被100整除的年份，或者能够被400整除的年份

year = 0

print ('以下列举出公元 998-2023 年之间的所有闰年：')
for y in range (998,2024,1):

    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0 :  # 闰年判断条件

        year += 1 
        
        print ( y )

print (f'公元 998-2023 年间，共有闰年数量为: {year} 年')