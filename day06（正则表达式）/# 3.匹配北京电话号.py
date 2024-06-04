# 3.匹配北京手机号  010-55667788，中间的-有或没有都可以  前面必须以010开头
import re
while True:
    input_phone = input('请输入包含010开头的电话号:')
    re_input_phone = re.match(r'^(010)[-]?\d{8}$',input_phone)
    if re_input_phone:
        print(f'输入的电话号{input_phone}合规!')
    else:
        print(f'输入的电话号{input_phone}不合规!')