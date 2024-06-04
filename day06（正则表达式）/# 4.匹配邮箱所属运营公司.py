# 4.匹配邮箱所属运营公司
# 现有邮箱列表
# ["xiao_Wang@139.com", "xiaoWang@163.com.com","123456789?@qq.com",
# "xiaowang@163.com","xiaowang987531@139.com","lisi123456@sina.com"]
# 使用分组匹配查找出其中合规的邮箱信息，并判断其所属运营公司（网易、腾讯、新浪、移动）
import re
list_email = ["xiao_Wang@139.com", "xiaoWang@163.com.com","123456789?@qq.com",\
"xiaowang@163.com","xiaowang987531@139.com","lisi123456@sina.com"]
for char in list_email:
    re_email = re.match(r'^[A-Za-z0-9_]+@(139|163|qq|sina)\.com$',char)
    if re_email:
        if char.strip().split('@')[1][:-4] == '163':
            print(f'合规邮箱:{char}, 运营公司:网易')
        elif char.strip().split('@')[1][:-4] == '139':
            print(f'合规邮箱:{char}, 运营公司:移动')
        elif char.strip().split('@')[1][:-4] == 'qq':
            print(f'合规邮箱:{char}, 运营公司:腾讯')
        else:
            print(f'合规邮箱:{char}, 运营公司:新浪')
    else:
        print(f'不合规邮箱:{char}')