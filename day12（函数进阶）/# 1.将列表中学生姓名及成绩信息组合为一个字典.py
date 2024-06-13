# 1. 将下列每个学生姓名及其成绩组合为一个字典
names = ['张三', '李四', '小明', '小红']
math = [90, 89, 88, 99]
english = [98, 78, 66, 82]
chinese = [23, 98, 100, 72]
ret = zip(names, math, english, chinese)
data = list(ret)
stuinfo_list = []
for char in data:
    stuinfo_dict = {}
    stuinfo_dict['name'] = char[0]
    stuinfo_dict['math'] = char[1]
    stuinfo_dict['english'] = char[2]
    stuinfo_dict['chinese'] = char[3]
    stuinfo_list.append(stuinfo_dict)
print(f'整合后的学生信息输出为:{stuinfo_list}')