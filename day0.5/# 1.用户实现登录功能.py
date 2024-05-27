# 1.给用户三次机会 实现登录功能
for num in range(1,4):
    user_name = str(input('请输入用户名:'))
    user_password = str(input('请输入用户密码:'))
    if user_name == 'admin' and user_password == '123':
        print('信息正确，登录成功!')
        break
    else:
        print(f'账户名或密码错误，您还有 {3-num} 次登录机会')