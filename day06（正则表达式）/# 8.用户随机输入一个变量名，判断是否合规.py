# 8.用户随机输入一个变量名，判断是否合规
# 变量名规则：1.由数字、字母、下划线组成  2.数字不能开头  
# 3.不能使用python内置关键字作为变量名（keyword模块中kwlist中包含所有的python内置关键字）
import re, keyword
while True:
    print(keyword.kwlist)
    VariableName = input('请随机输入一个变量名:')
    re_variableName = re.match(r'^\D[a-zA-Z0-9_]*$',VariableName)
    kw = keyword.kwlist
    if re_variableName:
        if VariableName not in kw:
            print(f'输入的变量名:{VariableName}合规')
        else:
            print(f'输入的变量名{VariableName}不合规!')
    else:
        print(f'输入的变量名:{VariableName}不合规!')
