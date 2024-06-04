# 6.域名匹配
# 匹配以"www"起始并以".com"结尾的域名例如 www.baidu.com,  也支持其它域名.edu .net .cn
import re
while True:
    DomainName = input('请输入一个完整域名:')
    re_DomainName = re.match(r'^(www.)[a-z0-9_]*\.(com|edu|net|cn)$',DomainName)
    if re_DomainName:
        print(f'输入的域名:{DomainName}为合规域名!')
    else:
        print(f'输入的域名:{DomainName}为非法域名!')