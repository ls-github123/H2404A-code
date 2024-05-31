# 1.声明一个列表，在列表中保存6只小狗的信息
# a.统计不及格学生的个数
# b.打印不及格学生的名字和对应的成绩
# c.统计未成年学生的个数
# d.打印手机尾号是8的学生的名字
# e.打印最高分和对应的学生的名字
# f.删除性别不明的所有学生

students = [
    {'name': '张三', 'age': 23, 'score': 88, 'tel': '23423532', 'gender': '男'},
    {'name': '李四', 'age': 26, 'score': 80, 'tel': '12533453', 'gender': '女'},
    {'name': '王五', 'age': 15, 'score': 58, 'tel': '56453453', 'gender': '男'},
    {'name': '赵六', 'age': 16, 'score': 57, 'tel': '86786785', 'gender': '不明'},
    {'name': '小明', 'age': 18, 'score': 98, 'tel': '23434656', 'gender': '不明'},
    {'name': '小红', 'age': 23, 'score': 72, 'tel': '67867868', 'gender': '女'},
    ]

# a
fail_stu = sum (1 for stu in students  if stu['score'] < 60 )
print (f'#a 不及格学生的个数为:{fail_stu} 个')

# b
fail_stu = [(stu['name'],stu['score']) for stu in students if stu ['score'] < 60]
print (f'#b 不及格学生的的名字和对应的成绩分别为:{fail_stu}')

# c
child_stu = sum (1 for stu in students  if stu['age'] < 18 )
print (f'#c 未成年学生的个数为:{child_stu} 人')

# d
end_8_stu = [(stu['name']) for stu in students  if stu['tel'][-1] == '8' ]
print (f'#d 手机尾号是8的学生的名字为:{end_8_stu}')

# e
dict_max_fail = {}
for stu in students :
    dict_max_fail [stu ['name']] = [stu ['score']]
print(dict_max_fail)
for stu,stu_score in dict_max_fail.items():
    if stu_score == max (dict_max_fail.values()):
        print (f'#e 最高分和对应的学生名字为:{stu_score[0]},{stu}')

# f
list_none_gender = []
for stu in students:
    if stu['gender'] == '不明':   
        list_none_gender.append (stu)
for stu in list_none_gender:
    if stu in students:
        students.remove (stu)
print (f'#f 删除性别不明的学生后显示为:{students}')