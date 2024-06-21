# 5.装饰器文件读写，正则验证
import re, random, time
def outer1(f):
    def inner():
        print('账户注册')
        user_mobile = input('请输入用户手机号:')
        user_email = input('请输入用户邮箱:')
        re_mobile = re.match(r'^1[3-9]\d{9}$', user_mobile)
        re_email = re.match(r'^[A-Za-z0-9]{6,14}@(qq|163|outlook|gmail)\.com$', user_email)
        if re_mobile and re_email:
            print('信息验证通过,请等待生成4位验证码')
            code = random.randint(1000,9999)
            time.sleep(3)
            print(f'生成的验证码为:{code}')
            code_input = input('请输入验证码:')
            if code_input == str(code):
                print('验证码正确')
                with open('account.txt', 'a', encoding='utf8') as file:
                    file.write(f'mobile:{user_mobile}_email:{user_email}\n')
                    print('账户注册成功,信息已写入本地文件"account.txt"')
                    file.close()
                    return f()
            else:
                print('验证码错误,注册失败!')
        else:
            print('输入的信息不符合系统规范,请重新输入!')
    return inner

def outer2(f):
    def inner():
        user_dict = {}
        with open('account.txt', 'r', encoding = 'utf8') as file:
            data = file.readlines()
        for char in data:
            info_parts = char.split('_')
            mobile_patrs = info_parts[0]
            email_parts = info_parts[1]
            mobile = mobile_patrs.split(':')[1] if mobile_patrs.startswith('mobile') else None
            email = email_parts.split(':')[1] if email_parts.startswith('email') else None
            user_dict[mobile] = email.strip()
        attempts = 3
        while attempts > 0:
            input_mobile = input('请输入注册的手机号:')
            input_email = input('请输入注册的邮箱:')
            if input_mobile in user_dict:
                if user_dict[input_mobile] == input_email:
                    print('账户信息验证通过,登录成功')
                    return f()
                else:
                    attempts -= 1
                    if attempts > 0:
                        print(f'输入的手机号或邮箱不正确,登录失败,还有{attempts}次机会')
                    else:
                        print('登录次数已用完!')
                        break
            else:
                print('输入的手机号不存在!')
    return inner
 
@outer1        
@outer2
def func():
    print('欢迎来到宝宝的宝宝是宝宝官方网站')
func()