# 1、可以判断用户输入的手机号是否是合法的，一个合法的手机号满足以下条件：
# 手机号码由11位数字组成
# 手机号前三位为网络识别号，对应不同的手机运营商；
# 在本题目中，只有以下几种情况，其余情况均认为无效手机号
# 中国电信：133，153，180，181，189
# 中国联通：130，131，155，185，186
# 中国移动：135，136，150，182，188
# 剩余八位数字任意：
# 现在输入手机号码，判断是否合法
# 输出要求：
# 如满足正确手机号匹配，中国电信输出China Telecom，中国联通输出 China Unicom，
# 中国移动输出China Mobile Communications，其余不满足情况输出-1
# 输入：
# 13312345678
# 输出：
# China Telecom

import re
while True:
    UserMobile = input('请用户输入手机号:')
    ret_UserMobile = re.match(r'^1(3|5|8)(0|1|2|3|5|6|8|9)\d{8}$', UserMobile)
    if ret_UserMobile:
        print(f'输入的手机号:{UserMobile}合法')
        operators = int(ret_UserMobile.group()[:3])
        if operators in [133,153,180,181,189]:
            print('China Telecom')
        elif operators in [130,131,155,185,186]:
            print('China Unicom')
        elif operators in [135,136,150,182,188]:
            print('China Mobile Communications')
        else:
            print('- 1')
    else:
        print(f'输入的手机号:{UserMobile}不合法!')