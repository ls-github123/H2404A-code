# 学生信息管理系统
# 制作学生管理系统-->可以增加多个学生
# 要求需要录入每个同学的姓名、年龄、性别
# 将所有学生的信息整理好录入系统即可
# 提示：
# 学生多个信息整合-->筛选数据类型接收
# 多个学生信息整合-->筛选数据类型接收
list_student_info = [] # 定义一个空列表，用于接收和整合录入的所有学生信息
while True:
    model_choice = input('请输入字母 Y 开始或继续录入学生信息,输入 Q 结束:')
    if model_choice.upper() == 'Y':
        student_name = input('请输入学生姓名:')
        student_age = input('请输入学生年龄:')
        student_gender =input('请输入学生性别(男/女):')
        # 使用len()方法校验输入的学生信息，如果有空值则提示并返回重新输入
        if len(student_name) == 0 or len(student_age) == 0 or len(student_gender) == 0: 
            print('输入的学生信息不能有空值,请重新输入!')
        else:
            dict_student_info = {'name':student_name, 'age':student_age, 'gender':student_gender} # 将单个学生的信息组成一个字典
            list_student_info.append(dict_student_info) # 将单个学生信息组成的字典作为一个元素写入列表
            print(f'学生 {student_name} 信息已添加')
    elif model_choice.upper() == 'Q':
        print('结束学生信息录入')
        if len(list_student_info) > 0: # 校验列表中是否已录入学生信息
            print(f'当前录入的学生信息为:{list_student_info}')
            break
        else:
            print('当前暂未录入学生信息!')
            break
    else:
        print('输入的信息无效,请重新输入！')