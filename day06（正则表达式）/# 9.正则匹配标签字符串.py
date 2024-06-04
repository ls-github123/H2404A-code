# 9.正则匹配标签字符串
# str1 = "<p><a>法外狂徒张三！哪里逃？！</a></p>"，正则匹配当前字符串
import re
str1 = "<p><a>法外狂徒张三！哪里逃？！</a></p>"
re_str1 = re.match(r'^<([a-z][a-z1-6]?[a-z]*)><([a-z][a-z1-6]?[a-z]*)>.*</\2></\1>$',str1)
if re_str1:
    print(f'字符串{str1}匹配')
else:
    print(f'字符串{str1}不匹配!')