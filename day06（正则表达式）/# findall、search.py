# findall / search
import re

# findall()
str1 = "这个视频的播放量位4879615,点赞量位18485,转发量位254"
# findall()
# 语法：re.findall(r"正则",字符串)
# 作用：以列表的形式返回字符串中所有符合规则的数据，如果没有匹配成功的数据则返回空列表
ret1 = re.findall(r"\d+",str1) # findall
print(ret1)


# search()
# 语法：re.search(r"正则",字符串)
# 作用：从字符串任意位置开始匹配。一旦匹配成功立马返回对象，匹配失败返回None
# ret.group()  如果匹配成功返回具体匹配成功的数据，匹配失败则报错
ret2 = re.search(r"\d+",str1)
print(ret2.group()) 


# match()
# 语法：re.match(r"正则",字符串)
# 作用：从字符串开头开始匹配。一旦匹配成功立马返回对象，匹配失败返回None；
# ret.group()  如果匹配成功返回具体匹配成功的数据，匹配失败则报错
ret3= re.match(r'\d+',str1)
print(ret3)
print(ret3.group()) # --> 报错