# 编写一个Python程序，提示用户输入一个日期（年-月-日），然后格式化输出为"YYYY/MM/DD"形式

def format_date (year, month, day):
    formatted_date = "{:04d}/{:02d}/{:02d}" .format(year, month, day)
    return formatted_date

if __name__ == "__main__":
    year = int(input("请输入年份信息："))
    month = int(input("请输入月份信息："))
    day = int(input("请输入天数（最大为31）："))

formatted_date = format_date (year, month, day)
print ("格式化后的日期为：{}" .format(formatted_date))
