# 汽车管理系统
import re  # 调用正则表达式模块
import random  # 调用随机数模块
import time  # 调用时间处理模块
import bcrypt # 调用bcrypt加密模块 -- 对用户密码进行哈希转换
import getpass # 调用getpass模块，隐藏用户输入的密码
# 定义一个全局变量空列表，用于存放录入的车辆信息，正式功能中使用后端mysql数据库替代
list_all_carts = []

# 菜单展示模块
def menu():
    print('-------- 欢迎使用H2404A型商品车信息管理系统 --------')
    print() # 空行
    print('1.增加车辆信息')
    print('2.展示系统中所有车辆信息')
    print('3.查询车辆信息')
    print('4.修改车辆信息')
    print('5.删除车辆信息')
    print('6.退出系统')
    print('*' * 45)
    
# 密码哈希转换模块
def bcrypt_module(user_password):
    password = user_password.encode('utf-8') # 声明密码，转换为字节串
    salt = bcrypt.gensalt() # 生成随机盐
    hashed = bcrypt.hashpw(password, salt).decode('utf-8') # 生成密码哈希字符串,转换为字符串
    return hashed

# 用户账户注册模块
def sing_account():
    print('-------- 欢迎使用H2404A型商品车信息管理系统 --------')
    print('请先登录或注册')
    file_path = 'user_account.txt' # 定义存放用户账户和密码的文件路径
    verification_info = accountinfo_extraction(file_path) # 接收accountinfo_extraction()函数中返回的用户信息字典数据
    user_have_acoount = input('请输入任意字符进入注册界面(如你已有账号,请直接点击<enter>键跳过):')
    if user_have_acoount == '': # ''值 -- 点击<enter>直接跳过，否则将执行else
        return login_account()
    else:
        print('开始进行用户账户注册')
        user_mobile = input('请输入用户手机号(11位数字):')
        user_email = input('请输入用户邮箱(支持@qq.com、@sino.com、@163.com、@gmail.com、@outlook.com):')
        user_password = input('请输入用户密码(长度必须在6位以上,可包含数字、大小写字母、下划线):')      
    re_user_mobile = re.match(r'^1[3-9]\d{9}$',user_mobile)
    re_user_email = re.match(r'^[A-Za-z0-9_]{6,14}@(qq|sino|163|gmail|outlook)\.com$',user_email)
    re_user_password = re.match(r'^[A-Za-z0-9_]{6,}$',user_password) 
    if re_user_mobile and re_user_email and re_user_password:
        # 注册信息查重，如手机号和邮箱有任一注册过，则需更换
        if user_mobile in verification_info or user_email in verification_info:
            print('输入的账号(手机号或邮箱)已注册过,请更换!')
            return sing_account()
        else:
            print('注册信息校验通过,请等待系统生成6位验证码')
            verification_code = str(random.randint(100000,999999))
            time.sleep(3) # 程序休眠3秒
            print(f'生成的验证码为:{verification_code}')
            input_verification_code = input('请输入系统返回的验证码:')
            if input_verification_code == verification_code:
                print('验证码正确')
                hashed_password = bcrypt_module(user_password)  # 将用户密码传递给bcrypt_module函数，并接收返回的哈希值
                with open('user_account.txt', 'a', encoding='utf8') as file:
                    file.write(f'mobile:{user_mobile} email:{user_email} hashed:{hashed_password}\n')
                print('用户账户注册完成')
                print('您的账户信息将保存在本地路径下的<user_account.txt>文件中,密码已经过bcrypt算法进行高强度哈希加密')
                login_account() # 注册完成,自动进入登录界面
            else:
                print('输入的验证码错误,注册失败!')
                return False
    else:
        print('输入的账号或密码不符合系统规范,注册失败!')
        return False

# 定义账户信息提取模块
def accountinfo_extraction(file_path):
    dict_user_accoutninfo = {} # 定义一个空字典，用于暂存用于校验的用户账户信息
    with open(file_path, 'r', encoding='utf8') as file:
        for line in file.readlines(): # 遍历文件中的每一行
            info_parts = line.strip().split(' ') #将用户注册信息按行提取，每名用户信息提取为一个列表
            mobile_info = info_parts[0]
            email_info = info_parts[1]
            password_info = info_parts[2]
            # 解决了多用户注册时，只能校验最后一名用户注册信息(即写入文件user_account.txt中最后一行数据)的问题
            mobile = mobile_info.split(':')[1] if mobile_info.startswith('mobile') else None
            email = email_info.split(':')[1] if email_info.startswith('email') else None
            password = password_info.split(':')[1] if password_info.startswith('hashed') else None
            #  将手机号和邮箱作为键，将密码的哈希值作为对应的值
            #  存储在字典dict_user_accoutninfo中
            if mobile and password:
                dict_user_accoutninfo[mobile] = password
            if email and password:
                dict_user_accoutninfo[email] = password
    return dict_user_accoutninfo  # 返回字典数据

# 定义用户账户登录模块
def login_account():
    print('用户账户登录')
    file_path = 'user_account.txt' # 定义存放用户账户和密码的文件路径
    verification_info = accountinfo_extraction(file_path) # 接收accountinfo_extraction()函数中返回的用户信息字典数据
    attempts = 3
    while attempts > 0: # 用户3次登录机会循环
        user_login = input('请输入用户账号(注册时使用的邮箱或密码):')
        user_login_password = getpass.getpass('请输入您的密码(已使用getpass模块隐藏明文,请直接输入后按<enter>确认):')
        # 校验输入的账号和密码是否匹配
        if user_login in verification_info: # 输入的账号user_login作为键，是否在返回的用户注册信息字典verification_info中存在
            # 输入的用户账号信息user_login作为字典的键
            # 对应的值—密码哈希字符串  使用.encode()转换为'utf-8'编码字节串，并用新变量hashed_password接收
            # bcrypt处理的是'字节串'而不是字符串
            hashed_password = verification_info[user_login].encode('utf-8')
            if bcrypt.checkpw(user_login_password.encode('utf-8'), hashed_password):
                # bcrypt: Python中用于密码哈希的库,它可以安全地存储和验证密码
                # checkpw: bcrypt库中的一个函数,用于验证密码是否与存储的哈希值匹配
                # user_login_password.encode('utf-8') -- 这部分将用户输入的密码转换成UTF-8编码的字节串
                # hashed_password: 从数据库或文件中检索到的存储的密码哈希值
                print(f'用户({user_login})登录成功')
                return True
            else:
                attempts -= 1
                if attempts > 0:
                    print(f'登录失败,请检查用户名或密码,还可登录{attempts}次')
                else:
                    print('登录次数已用完,请重启系统')
                    exit()
        elif user_login == '':
            print('输入的账号信息不能为空,请重新输入!')
        else:
            print('输入的账号不存在,请重新输入')

# main() 1.增加车辆信息
def add_cartsinfo(list_all_carts):
    new_cartsinfo = {}
    print('向系统中增加车辆信息')
    carts_brand = input('请输入车辆品牌(制造商):')
    carts_model = input('请输入车辆型号:')
    carts_price = input('请输入车辆价格(万元):')
    carts_quantity = input('请输入入库数量(辆):')
    # 正则校验输入合规性
    re_carts_brand = re.match(r'^[\u4e00-\u9fa5]{2,}$', carts_brand) # 输入必须为中文，长度至少2位
    re_carts_model = re.match(r'^[A-Za-z0-9_]{1,}$', carts_model) # 输入可为大小写字母、数字0-9、可包含下划线，长度至少1位
    re_carts_price = re.match(r'^[0-9]+(.[0-9]{1,2})?$', carts_price) # 输入可为整数，如果为小数，小数点后最多为2位
    re_carts_quantity = re.match(r'^\d{1,}$', carts_quantity) # 输入的必须为整数，至少为1位数字
    if re_carts_brand and re_carts_model and re_carts_price and re_carts_quantity:
        for new_cartsinfo in list_all_carts:
            if new_cartsinfo['brand'] == carts_brand and new_cartsinfo['model'] == carts_model and new_cartsinfo['price'] == carts_price:
                cartsinfo_index = int(list_all_carts.index(new_cartsinfo)) # # 查找对应车辆信息在列表中的下标序号
                print('系统中已有该型车数据')
                list_all_carts[cartsinfo_index]['quantity'] += int(carts_quantity)
                print(f'该车型(品牌(制造商):{new_cartsinfo['brand']},型号:{new_cartsinfo['model']})库存数量增加:{carts_quantity} 辆')
                return False
        new_cartsinfo = {'id':str(len(list_all_carts) + 1), 'brand':carts_brand, 'model':carts_model, 'price':carts_price, 'quantity':int(carts_quantity)}
        list_all_carts.append(new_cartsinfo)
        print(f'车辆({carts_brand}, {carts_model})信息添加成功')
        print(list_all_carts)
        return True
    else:
        print('输入的车辆信息与系统规范不符,请重新添加!')
        
# main() 2.展示系统中所有车辆信息
def show_allinfo(list_all_carts):
    if len(list_all_carts) == 0:
        print('!!!系统中暂未录入车辆信息,请先添加!!!')
        return add_cartsinfo(list_all_carts)
    else:
        print('展示系统中所有商品车信息:')
        for i, carts_info in enumerate(list_all_carts, start = 1):
            print(f'序号:{i}, 系统编号:{carts_info['id']}, 品牌(制造商):{carts_info['brand']}, 型号:{carts_info['model']}, 价格(万元):{carts_info['price']}, 库存(辆):{carts_info['quantity']}')

# main() 3.查询车辆信息
def select_cartsinfo(list_all_carts):
    searched_cartsinfo = [] # 定义一个空列表，寄存查询到的车辆信息
    print('查询指定车辆信息')
    search_input = input('请输入要查询车辆的系统编号、品牌(制造商)或型号:')
    for select_cartsinfo in list_all_carts:
        if select_cartsinfo['id'] == search_input or select_cartsinfo['brand'] == search_input or select_cartsinfo['model'] == search_input:
            searched_cartsinfo.append(select_cartsinfo)
    if searched_cartsinfo:
        print('找到以下匹配的车辆信息:')
        for i, carts_info in enumerate(searched_cartsinfo, start = 1):
            print(f'序号:{i}, 系统编号:{carts_info['id']}, 品牌(制造商):{carts_info['brand']}, 型号:{carts_info['model']},价格(万元):{carts_info['price']}, 库存(辆):{carts_info['quantity']}')
    else:
        print(f'系统中未找到对应{search_input}的车辆信息!')
        return False

# main() 4.修改车辆信息
def modify_cartsinfo(list_all_carts):
    print('修改系统中指定车辆的信息')
    select_cartsinfo(list_all_carts) # 调用查询模块功能，帮助用户选择
    choice_carts = input('请输入要修改车辆的系统编号:')
    found = False
    for cartsinfo in list_all_carts:
        if cartsinfo['id'] == choice_carts:
            found = True
            cartsinfo_index = int(list_all_carts.index(cartsinfo))
            while True:
                print('请选择要修改的信息')
                print('1.品牌(制造商), 2.型号, 3.价格, 4.库存')
                modify_choice = input('请输入要修改的字段序号:')
                if modify_choice == '1':
                    new_brand = input('请输入修改后的品牌(制造商):')
                    re_new_brand = re.match(r'^[\u4e00-\u9fa5]{2,}$', new_brand)
                    if re_new_brand:
                        list_all_carts[cartsinfo_index]['brand'] = new_brand
                        print(f'品牌(制造商){new_brand}修改成功')
                        print(f'系统编号:{list_all_carts[cartsinfo_index]['id']}, 品牌(制造商):{list_all_carts[cartsinfo_index]['brand']}, 型号:{list_all_carts[cartsinfo_index]['model']}, 价格(万元):{list_all_carts[cartsinfo_index]['price']}, 库存(辆):{list_all_carts[cartsinfo_index]['quantity']}')
                        return True
                    else:
                        print(f'输入的信息{new_brand}不符合系统规范!')
                elif modify_choice == '2':
                    new_model = input('请输入修改后的型号:')
                    re_new_model = re.match(r'^[A-Za-z0-9_]{1,}$', new_model)
                    if re_new_model:
                        list_all_carts[cartsinfo_index]['model'] = new_model
                        print(f'型号:{new_model}修改成功')
                        print(f'系统编号:{list_all_carts[cartsinfo_index]['id']}, 品牌(制造商):{list_all_carts[cartsinfo_index]['brand']}, 型号:{list_all_carts[cartsinfo_index]['model']}, 价格(万元):{list_all_carts[cartsinfo_index]['price']}, 库存(辆):{list_all_carts[cartsinfo_index]['quantity']}')
                        return True
                    else:
                        print(f'输入的信息{new_model}不符合系统规范!')
                elif modify_choice == '3':
                    new_price = input('请输入修改后的价格(万元):')
                    re_new_price = re.match(r'^[0-9]+(.[0-9]{1,2})?$', new_price)
                    if re_new_price:
                        list_all_carts[cartsinfo_index]['price'] = new_price
                        print(f'价格:{new_price}修改成功')
                        print(f'系统编号:{list_all_carts[cartsinfo_index]['id']}, 品牌(制造商):{list_all_carts[cartsinfo_index]['brand']}, 型号:{list_all_carts[cartsinfo_index]['model']}, 价格(万元):{list_all_carts[cartsinfo_index]['price']}, 库存(辆):{list_all_carts[cartsinfo_index]['quantity']}')
                        return True
                    else:
                        print(f'输入的信息{new_price}不符合系统规范!')
                elif modify_choice == '4':
                    new_quantity = input('请输入修改后的库存(辆):')
                    re_new_quantity = re.match(r'^\d{1,}$', new_quantity)
                    if re_new_quantity:
                        list_all_carts[cartsinfo_index]['quantity'] = int(new_quantity)
                        print(f'库存:{new_quantity}修改成功')
                        print(f'系统编号:{list_all_carts[cartsinfo_index]['id']}, 品牌(制造商):{list_all_carts[cartsinfo_index]['brand']}, 型号:{list_all_carts[cartsinfo_index]['model']}, 价格(万元):{list_all_carts[cartsinfo_index]['price']}, 库存(辆):{list_all_carts[cartsinfo_index]['quantity']}')
                        return True
                    else:
                        print(f'输入的信息{new_quantity}不符合系统规范!')
                else:
                    print('输入的序号无效!')
    if not found:
        print('系统中没有该车辆的信息!')

# main() 5.删除车辆信息
def del_cartsinfo(list_all_carts):
    print('删除指定车辆信息')
    select_cartsinfo(list_all_carts)
    delete_cartinfo = input('请输入要删除车辆的系统编号:')
    found = False
    for cartinfo in list_all_carts:
        if cartinfo['id'] == delete_cartinfo:
            found = True
            cartinfo_index = int(list_all_carts.index(cartinfo))
            print(f'系统编号:{cartinfo['id']}, 品牌(制造商):{cartinfo['brand']}, 型号:{cartinfo['model']}')
            enter_del = input('请确认是否删除该车辆信息(Y -确认删除, E -取消):')
            if enter_del.upper() == 'Y':
                list_all_carts.pop(cartinfo_index)
                print('车辆信息已删除')
                return True
            elif enter_del.upper() == 'E':
                print('取消删除该车辆信息')
                return False
            else:
                print('输入的信息无效!')
    if not found:
        print('系统中没有该车辆信息!')
    

# 定义主函数
def main():
    sing_account() # 调用用户账户注册模块功能
    while True:
        menu() # 调用菜单
        mode_selection = input('请输入要执行的功能序号:')
        if mode_selection == '1':
            add_cartsinfo(list_all_carts)
        elif mode_selection == '2':
            show_allinfo(list_all_carts)
        elif mode_selection == '3':
            select_cartsinfo(list_all_carts)
        elif mode_selection == '4':
            modify_cartsinfo(list_all_carts)
        elif mode_selection == '5':
            del_cartsinfo(list_all_carts)
        elif mode_selection == '6':
            print('退出系统')
            exit()
        else:
            print('输入的参数无效,请重新输入!')

if __name__ == '__main__':  # 文件作为脚本直接执行
    main()