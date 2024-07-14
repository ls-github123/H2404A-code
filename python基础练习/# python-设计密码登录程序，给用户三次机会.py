# python-设计密码登录程序，给用户三次机会，用户名为admin  密码为admin123
# 如果用户输入正确则登录成功并告诉用户这第几次输入账号密码登陆成功 ,否则登陆失败，并告诉用户还有几次登陆机会


for num in range (1,4,1):

    user_name = str (input ('请输入用户名：'))
    user_pwd = str (input ('请输入密码：'))

    if user_name == 'admin' and user_pwd == 'admin123':
        
        print (f'通过身份验证，登录成功，这是您第 {num} 次登录成功')

        break
    
    else:

        print (f'登录失败，用户名或密码错误，您还有 {3-num} 次登录机会！')