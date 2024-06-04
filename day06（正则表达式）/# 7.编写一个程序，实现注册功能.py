# 7.编写一个程序,实现注册功能
# 让用户输入手机号、邮箱和密码，如果手机号邮箱和密码都满足规则则注册成功，否则注册失败
# 手机号规则：11位数字、以1开头、第2位数字是3-9之间的任意一个、其余数字不限制
# 邮箱规则：@前由6-14位数字字母组成，可以匹配qq、163、139、sina邮箱，皆以.com结尾
# 密码规则：6位数字组成
import re
while True:
    user_mobile = input('请输入手机号(11位数字):')
    user_email = input('请输入邮箱(支持qq/163/139/sina邮箱):')
    user_password = input('请设置密码(6位数字):')
    re_user_mobile = re.match(r'^1[3-9]\d{9}$', user_mobile)
    re_user_email = re.match(r'^[A-Za-z0-9]{6,14}@(qq|163|139|sina)\.com$',user_email)
    re_user_password = re.match(r'^\d{6}$', user_password)
    if re_user_mobile and re_user_email and re_user_password:
        print('注册成功')
    else:
        print('注册失败!')