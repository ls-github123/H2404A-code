# 模拟注册程序
import re
UserMobile = input('请输入用户手机号:')
UserEmail = input('请输入用户邮箱:')
UserPassword = input('请设置用户密码:')
re_usermobile = re.match(r'^1[3-9]\d{9}$', UserMobile)
re_useremail = re.match(r'^[A-Za-z0-9]{6,14}@(qq|163|outlook|139|sino)\.com$', UserEmail)
re_userpassword = re.match(r'^\d{6}$',UserPassword)
if re_usermobile and re_useremail and re_userpassword:
    with open('user_account.txt', 'w', encoding='utf8') as file:
        file.write(f'mobile:{UserMobile}_email:{UserEmail}_password:{UserPassword}\n')
    print('账户信息写入完成')
    print('账户注册成功')
else:
    print('输入的账户信息不符合系统规范!')