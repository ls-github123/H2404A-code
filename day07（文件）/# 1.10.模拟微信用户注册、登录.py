# 1.模拟微信用户注册
# 让用户输入自己的手机号和密码，
# 如果手机号和密码都符合规则（6位数字组成）且手机号未注册过则注册成功，
# 则将用户注册的手机号存放在wechat.txt文件中；
# 如果手机号已注册过则提示用户"已注册过的手机号不能重复注册"
import re
def accountinfo_exeraction(file_path): # 账户注册数据提取
    dict_user_accountinfo = {}
    with open(file_path, 'r', encoding='utf8') as file:
        for line in file.readlines(): 
            # 按行读取文件中用户注册数据，每行为一个用户数据，以列表形式返回
            info_parts = line.strip().split('_') # 对数据进行切片检索
            mobile_info = info_parts[0]
            email_info = info_parts[1]
            pwd_info = info_parts[2]
            mobile = mobile_info.split(':')[1] if mobile_info.startswith('mobile') else None
            email = email_info.split(':')[1] if email_info.startswith('email') else None
            pwd = pwd_info.split(':')[1] if pwd_info.startswith('password') else None
            if mobile and pwd:
                dict_user_accountinfo[mobile] = pwd
            if email and pwd:
                dict_user_accountinfo[email] = pwd
    return dict_user_accountinfo
            
def sing_account():
    file_path = 'wechat.txt'
    verification_info = accountinfo_exeraction(file_path)
    UserMobile = input('请输入用户手机号:')
    UserEmail = input('请输入用户邮箱:')
    UserPwd = input('请设置用户密码(6位纯数字):')
    re_usermobile = re.match(r'^1[3-9]\d{9}$',UserMobile)
    re_useremail = re.match(r'^[A-Za-z0-9]{6,14}@(qq|gmail|outlook|163|sina)\.com$',UserEmail)
    re_userpwd = re.match(r'^\d{6}$', UserPwd)
    if re_usermobile and re_useremail and re_userpwd:
        if UserMobile in verification_info: # 手机\邮箱 查重
            print(f'输入的手机号{UserMobile}已注册过，请更换!')
            return sing_account()
        elif UserEmail in verification_info:
            print(f'输入的邮箱:{UserEmail}已注册过,请更换!')
            return sing_account()
        else:
            with open('wechat.txt', 'a', encoding='utf8') as file:
                file.write(f'mobile:{UserMobile}_email:{UserEmail}_password:{UserPwd}\n') # 校验无误的注册数据写入文件
                print(f'账户({UserMobile})注册成功')
                print('数据已写入本地文件 wecaht.txt')
            return True # 可多次注册
    else:
        print('输入的手机号或密码不符合系统规则,请重新输入!')
        return main() 


# 10.登录功能：
#    编写一个函数，实现登录功能
#    三次机会，让用户输入登录账号和登陆密码
#    (登陆账号可以是手机号登录也可以是邮箱登录，手机号和邮箱在文件中存放)
#    如果账号和密码都正确则登陆成功；否则登陆失败，并提示还有几次登陆机会
#    如果登陆成功则输出 "欢迎xxx登陆成功"
def login_account():
    print('用户账户登录')
    file_path = 'wechat.txt'
    verification_info = accountinfo_exeraction(file_path)
    attempts = 3
    while attempts > 0:
        UserLogin = input('请输入用户账号(注册时使用的邮箱或密码):')
        UserPwd = input('输入密码:')
        if UserLogin in verification_info:
            if UserPwd == verification_info[UserLogin]:
                print(f'用户{UserLogin}账户登录成功')
                return main()
            else:
                attempts -= 1
                if attempts > 0:
                    print(f'登录失败,请检查用户名或密码,还可登录{attempts}次')
                else:
                    print('登录次数已用完,请重新进入')
                    exit()
        else:
            print('输入的账号不存在!')
            return login_account()

def main():
    while True:
        model_choice = input('请选择功能序号(1.注册 2.登录):')
        if model_choice == '1':
            sing_account()
        elif model_choice == '2':
            login_account()
        else:
            print('输入的信息无效')

main()