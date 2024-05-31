# 3.给定一个字符串  str1 = "hello xiao mi you are beautiful girl"
# 要求将字符串中的单词作为字典的键，字典的值是单词的长度
str1 = "hello xiao mi you are beautiful girl"
dict_word = {}
for word in str1.strip().split():
    dict_word [word] = [len(word)][0]
print(dict_word)