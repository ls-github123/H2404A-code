# 9.检查指定字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容输出
dict1 = {'CPU':'Intel-xeon','RAM':'Samsung','ROM':'9G'}
for key, value in dict1.items():
    if len(value) > 2:
        dict1[key] = value[:2]
print(f'修改后的字典输出为:{dict1}')