# 学生信息管理系统

import re  # 调用正则表达式模块
import random  # 调用随机数模块
import time  # 调用时间处理模块
import bcrypt # 调用bcrypt加密模块 -- 对用户密码进行哈希转换
import getpass # 调用getpass模块，隐藏用户输入的密码

# 定义一个全局变量空列表，用于存放录入的学生信息，正式功能中使用后端mysql数据库替代
all_student_info = []
# 定义菜单展示模块
def menu():
    print('-------- 欢迎使用H2404A型学生信息管理系统 --------')
    print() # 空行
    print('1.展示系统中所有学生信息')
    print('2.向系统中添加学生信息')
    print('3.查询指定学生信息')
    print('4.修改指定学生信息')
    print('5.删除指定学生信息')
    print('6.退出系统')
    print('*' * 30)

# 定义用户密码哈希转换模块
def bcrypt_module(user_password): 
    password = user_password.encode('utf-8')  # 声明密码，转换为字节串
    salt = bcrypt.gensalt() # 生成随机盐
    hashed = bcrypt.hashpw(password, salt) # 生成哈希字符串
    return hashed.decode('utf-8')

# 定义用户账户注册模块
def sing_account():
    print('-------- 欢迎使用H2404A型学生信息管理系统 --------')
    print('请先登录或注册')
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

# 定义账户信息提取模块
def accountinfo_extraction(file_path):
    dict_user_accoutninfo = {} # 定义一个空字典，用于暂存用于校验的用户账户信息
    with open(file_path, 'r', encoding='utf8') as file:
        for line in file.readlines(): # 遍历文件中的每一行
            # 在单行字符串中 提取出包含开头标题信息的 手机号、邮箱及哈希密码 字符串
            
            #  ！！！报错写法  每次循环迭代时，都会重新定义 mobile_info、email_info 和 password_info 变量
            # 因此在循环结束后，这些变量只会保留最后一行的值  password 变量在循环外部无法访问
            # mobile_info = line.strip().split(' ')[0]
            # email_info = line.strip().split(' ')[1]
            # password_info = line.strip().split(' ')[2]
                # 修改后
            info_parts = line.strip().split(' ') #将用户注册信息按行提取，每名用户信息提取为一个列表
            mobile_info = info_parts[0]
            email_info = info_parts[1]
            password_info = info_parts[2]
            
            # 在单行字符串中 提取出包含开头提示信息的 手机号、邮箱及哈希密码 字符串
                # 报错写法 -- 
            # 尝试访问 password 变量时，它没有被正确地赋值,for 循环内部
            # 因为 mobile、email 和 password 变量只在某些条件分支内被赋值,而不是在每次迭代时都被赋值
            # if mobile_info.startswith('mobile'):
            #     mobile = mobile_info.split(':')[1]
            # elif email_info.startswith('email'):
            #     email = email_info.split(':')[1]
            # elif password_info.startswith('hashed'):
            #     password = password_info.split(':')[1]
                # 修改后
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
        if user_login in verification_info:
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


# main() 1.展示系统中所有学生信息功能
def show_allinfo(all_student_info):
    if len(all_student_info) == 0:
        print('!!!系统中暂未录入学生信息,请先添加!!!')
    else:
        print(f'系统中的所有学生信息为:{all_student_info}')

# main() 2.向系统中添加学生信息
def add_stuinfo(all_student_info):
    new_stuinfo = {} # 定义一个空字典，用于暂存单个学生信息
    stu_name = input('请输入学生姓名:')
    stu_gender = input('请输入学生性别(男/女):')
    stu_idnum = input('请输入学生身份证号(18位字符,最后一位如为X必须为大写):')
    
    # 正则校验输入信息合规性
    # 输入信息必须为中文且不能为空
    re_stu_name = re.match(r'^[\u4e00-\u9fa5]{1,}$',stu_name)
    # 输入信息必须为 男或女
    re_stu_gender = re.match(r'^[男女]{1}$',stu_gender)
    # 暂定输入信息必须为18位,正式系统中需按照身份证号实际编码规则进行校验
    re_stu_idnum = re.match(r'^\d{17}(\d|X)$',stu_idnum) 
    if re_stu_name and re_stu_gender and re_stu_idnum:
        # 校验输入的学生信息是否重复
        for new_stuinfo in all_student_info:
            if new_stuinfo['id_num'] == stu_idnum:
                print(f'学生{stu_name}身份证号与系统内记录重复,请检查!')
                return False
        new_stuinfo = {'id':str(len(all_student_info) + 1), 'name':stu_name, 'gender':stu_gender, 'id_num':stu_idnum}
        all_student_info.append(new_stuinfo)
        print(f'学生({stu_name})信息添加成功')
        print(all_student_info) # 输出整个系统列表中的数据
        return True
    else:
        print('输入的学生信息不合规,请检查并重新输入!')

# main() 3.查询指定学生信息
def select_stuinfo(all_student_info):
    searched_stuinfo = [] # 定义一个空列表，寄存查询到的学生信息
    search_input = input('请输入要查询的学生姓名、系统编号或身份证号:')
    for select_stuinfo in all_student_info: # 遍历学生信息存储列表
        if select_stuinfo['name'] == search_input or select_stuinfo['id'] == search_input or select_stuinfo['id_num'] == search_input:
            # 在学生信息存储列表中遍历个体字典,使用临时变量select_stuinfo进行接收
            # 如果临时变量select_stuinfo接收到个体字典name键或id_num键的值等于输入值search_input,则将该个体字典写入寄存列表
            searched_stuinfo.append(select_stuinfo)
    if searched_stuinfo: # 解决问题 -- 如果两个及以上学生姓名重复，会同时展示两个学生信息
        print('找到以下匹配的学生信息:')
        for i, students_info in enumerate(searched_stuinfo, start = 1):
            print(f'序号:{i}, 系统编号:{students_info['id']}, 姓名:{students_info['name']}, 性别:{students_info['gender']}, 身份证号:{students_info['id_num']}')
    else:
        print(f'在当前系统中未找到对应({search_input})的学生信息!')
        return False

# main() 4.修改指定学生信息
def modify_stuinfo(all_student_info):
    select_stuinfo(all_student_info) # 提高代码重用性
    choice_stuinfo = input('请输入要修改信息的学生系统编号或身份证号:')
    found = False  # 添加一个标志变量来跟踪是否找到学生信息
    for stuinfo in all_student_info:
        if stuinfo['id'] == choice_stuinfo or stuinfo['id_num'] == choice_stuinfo:
            found = True  # 找到匹配项，更新标志变量
            stuinfo_index = int(all_student_info.index(stuinfo)) # 查找对应学生信息在列表中的下标序号
            while True:
                print('请选择要修改的信息')
                print('1.姓名, 2.性别, 3.身份证号')
                modify_choice = input('请输入要修改的信息序号:')
                if modify_choice == '1':
                    new_name = input('请输入修改后的姓名:')
                    re_new_name = re.match(r'^[\u4e00-\u9fa5]{1,}$',new_name)
                    if re_new_name:
                        all_student_info[stuinfo_index]['name'] = new_name
                        print(f'姓名({new_name})修改成功')
                        print(f'姓名:{all_student_info[stuinfo_index]['name']}, 系统编号:{all_student_info[stuinfo_index]['id']}, 性别:{all_student_info[stuinfo_index]['gender']}, 身份证号:{all_student_info[stuinfo_index]['id_num']}')
                        return True
                    else:
                        print(f'输入的姓名{new_name}不符合系统规范!')
                elif modify_choice == '2':
                    new_gender = input('请输入修改后的性别:')
                    re_new_gender = re.match(r'^[男女]{1}$', new_gender)
                    if re_new_gender:
                        all_student_info[stuinfo_index]['gender'] = new_gender
                        print(f'学生({stuinfo['name']},系统编号:{stuinfo['id']})性别修改成功')
                        return True
                    else:
                        print(f'输入的性别信息{new_gender}不符合系统规范!')
                elif modify_choice == '3':
                    new_id_num = input('请输入修改后的身份证号:')
                    re_new_idnum = re.match(r'^\d{17}(\d|X)$', new_id_num) # 正则校验身份证号合规性
                    if re_new_idnum:
                        for new_stuinfo in all_student_info:
                            if new_stuinfo['id_num'] == new_id_num: # 身份证号查重
                                print(f'学生{stuinfo_index['name']}修改的身份证号与系统内已有记录重复,请检查!')   
                            else:
                                all_student_info[stuinfo_index]['id_num'] = new_id_num
                                print(f'(学生{stuinfo['name']},系统编号:{stuinfo['id']})身份证号修改成功')
                                return True
                    else:
                        print(f'修改后的身份证号信息:{new_id_num}不符合系统规范!')
                else:
                    print('输入的信息无效!')
    if not found: # 如果没有找到匹配项，则在循环结束后打印消息
        print('系统中没有该学生信息!')

# main() 5.删除指定学生信息
def del_stuinfo(all_student_info): 
    select_stuinfo(all_student_info) # 提高代码重用性
    delete_stuinfo = input('请输入要删除信息的学生系统编号或身份证号:')
    for stuinfo in all_student_info:
        if stuinfo['id'] == delete_stuinfo or stuinfo['id_num'] == delete_stuinfo:
            stuinfo_index = int(all_student_info.index(stuinfo)) # 查找对应学生信息在列表中的下标序号
            enter_del = input('请确认是否删除改名学生信息(Y -确认删除, E -取消):')
            if enter_del.upper() == 'Y':
                all_student_info.pop(stuinfo_index)
                print(f'学生:({stuinfo['name']}),系统编号:({stuinfo['id']}),相关信息已从系统中删除!')
                return True
            elif enter_del.upper() == 'E':
                print('取消删除该学生信息')
                return False
            else:
                print('输入的信息无效!')
                return False
        else:
            print('系统中没有该学生信息!')
    

# 定义主函数
def main():
    sing_account() # 调用用户账户注册模块功能
    while True:
        menu() # 调用菜单
        mode_selection = input('请输入要执行的功能序号:')
        if mode_selection == '1':
            show_allinfo(all_student_info)
        elif mode_selection == '2':
            add_stuinfo(all_student_info)
        elif mode_selection == '3':
            select_stuinfo(all_student_info)
        elif mode_selection == '4':
            modify_stuinfo(all_student_info)
        elif mode_selection == '5':
            del_stuinfo(all_student_info)
        elif mode_selection == '6':
            print('退出系统')
            exit()
        else:
            print('输入的参数无效,请重新输入!')

if __name__ == '__main__':
    main()