# 9.模拟注册功能
# 注册功能：
#    编写一个函数，实现注册功能
#    让用户输入手机号、邮箱和密码，
#    手机号规则：11位数字、以1开头、第2位数字是3-9之间的任意一个、其余数字不限制
#    邮箱规则：@前由6-14位数字字母组成，可以匹配qq、163、139、sina邮箱，皆以.com结尾
#    密码规则：6位数字组成、
#    如果手机号邮箱和密码都满足规则等待3秒接受一个4位数的随机验证码
# 如果密码和验证码都正确则注册成功，将注册成功的数据分行存放在reg.txt文件中
import re, random, time
def account():
    UserMobile = input('输入手机号:')
    UserEmali = input('输入邮箱:')
    UserPwd = input('输入密码:')
    re_usermobile = re.match(r'^1[3-9]\d{9}$', UserMobile)
    re_useremail = re.match(r'^[A-Za-z0-9]{6,14}@(qq|163|139|sina)\.com$',UserEmali)
    re_userpwd = re.match(r'^\d{6}$', UserPwd)
    if re_usermobile and re_useremail and re_userpwd:
        print('信息验证通过,请等待生成4位验证码')
        code = random.randint(1000,9999)
        time.sleep(3)
        print(f'生成的4位验证码为:{code}')
        input_code = input('请输入验证码:')
        if input_code == str(code):
            print('验证码正确')
            with open('reg.txt', 'a', encoding='utf8') as file:
                file.write(f'mobile:{UserMobile}_email:{UserEmali}_password:{UserPwd}\n')
            print('账户信息写入成功,保存至本地路径下(reg.txt)文件中')
        else:
            print('验证码错误!')
            return account()
    else:
        print('输入的信息不符合系统规范,注册失败,请重新输入!')
        return account()

account()