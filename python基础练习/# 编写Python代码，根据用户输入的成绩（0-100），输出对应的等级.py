# 编写Python代码，根据用户输入的成绩（0-100），输出对应的等级（优秀、良好、合格、不合格）

fraction = float (input ('请输入用户成绩（0-100）：'))

if fraction >= 90:
    print (f'该成绩等级为：[优秀]')

elif  80 <= fraction < 90:
    print (f'该成绩等级为：[良好]')

elif 60 <= fraction < 80:
    print (f'该成绩等级为：[及格]')

else:
    print (f'该成绩等级为：[不及格]')