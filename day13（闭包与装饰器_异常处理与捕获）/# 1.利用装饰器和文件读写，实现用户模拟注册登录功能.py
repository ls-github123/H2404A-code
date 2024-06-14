# 1.利用装饰器和文件读写，实现用户模拟注册登录功能
# 装饰器1功能：让用输入手机号和邮箱，如果手机号和邮箱都满足规则(正则验证)，
#     	则等待3秒接受一个6位数的随机验证码，
#     	如果用户输入的验证码也正确，则提示注册成功，并进入登录页
#     	(将注册成功的数据分行存放在文件1.txt中)
#    	否则提示注册失败
#  装饰器2功能：给用户三次登陆机会，让用户输入手机号和邮箱
#     	如果手机号和邮箱与文件中存放的注册的数据一致，
#     	则判定登陆成功，进入首页即可
#     	否则输出登陆失败，并提示还有几次登陆机会
# 原函数功能：模拟首页  输出"欢迎来到宝宝的宝宝是宝宝官方网站"
import random, re, time
def outer1(f):
    def inner():
        mobile = input('请输入用户手机号:')
        email = input('请输入用户邮箱:')
        re_mobile = re.match(r'^1[3-9]\d{9}$', mobile)
        re_email = re.match(r'^[A-Za-z0-9]{6,14}@(qq|163|gmail|outlook|sina)\.com$', email)
        if re_mobile and re_email:
            verification_code = random.randint(100000,999999)
            print('输入信息验证通过,请等待系统生成6位验证码')
            time.sleep(3)
            print(f'生成的6位验证码为:{verification_code}')
            code = input('请输入验证码:')
            if code == str(verification_code):
                print('验证码输入正确')
                with open('1.txt', 'a', encoding = 'utf8') as file:
                    # 为增强写入数据的可读性，使用下划线分隔手机号和邮箱，同时使用开头标题进行标示
                    file.write(f'mobile:{mobile}_email:{email}\n')
                    print('注册成功')
                    print('注册信息已写入本地文件 1.txt 中')
                    # 偶发性会出现程序运行后读写冲突问题,数据无法写入文件,加入强行关闭机制
                    file.close() 
                    return f()
            else:
                print('验证码错误,注册失败!')
        else:
            print('注册失败')
            print('输入的手机号或邮箱不符合系统规则!')
    return inner

def outer2(f):
    def inner():
        user_dict = {}
        with open('1.txt', 'r', encoding = 'utf8') as file:
            data = file.readlines()
            for char in data:
                info_parts = char.split('_')
                mobile_info = info_parts[0]
                email_info = info_parts[1]
                mobile = mobile_info.split(':')[1] if mobile_info.startswith('mobile') else None
                email = email_info.split(':')[1] if email_info.startswith('email') else None
                user_dict[mobile] = email.strip()
        connect = 3
        while connect > 0:
            input_mobile = input('请输入注册时的手机号:')
            input_email = input('请输入注册时的邮箱:')
            if input_mobile in user_dict:
                if user_dict[input_mobile] == input_email:
                    print('账户信息校验通过,登录成功!')
                    return f()
                else:
                    connect -= 1
                    if connect > 0:
                        print(f'输入的手机号或邮箱不正确,登录失败,还有{connect}次机会!')
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