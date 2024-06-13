# 学生信息整合
name_lst = ['张三','李四','王五','赵六']
math_score = [100, 89, 47, 96]
eng_score = [70, 90, 66, 34]
ret1 = zip(name_lst, math_score, eng_score)
data = list(ret1)
dict_list = []
for char in data:
    dict_info = {}
    dict_info['name'] = char[0]
    dict_info['math'] = char[1]
    dict_info['english'] = char[2]
    dict_list.append(dict_info)
print(f'整合后的学生信息为:{dict_list}')