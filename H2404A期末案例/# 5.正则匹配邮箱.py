# 5.正则匹配邮箱
import re
input_email = input('请输入邮箱地址:')
re_email = re.match(r'[A-Za-z0-9]{4,20}@(163|126|qq)\.com$', input_email)
if re_email:
    print(f'输入的邮箱:{input_email}符合系统规则')
    if re_email.group(1) == '163':
        print('为163邮箱')
    elif re_email.group(1) == '126':
        print('为126邮箱')
    elif re_email.group(1) == 'qq':
        print('为qq邮箱')
else:
    print('输入的邮箱不符合系统规则')