# 正则匹配网易标签
import re
while True:
    str_title = input('输入网页标签标题:')
    # 开始标签定义别名 (?P<别名>正则表达式)     结束标签使用别名 (?P=别名)
    re_title = re.match(r'^<(?P<re_title>[a-z][1-6a-z]?[a-z]*)>.*</(?P=re_title)>$',str_title) # 分组起别名
    print(re_title.group())