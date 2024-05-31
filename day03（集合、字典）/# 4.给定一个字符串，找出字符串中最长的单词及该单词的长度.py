# 4.给定一个字符串 str1 = "hello xiao mi you are beautiful girl"
# 找到这个字符串中出现长度最长的单词及该单词的长度
str1 = "hello xiao mi you are beautiful girl"
max_word = {}
for word in str1.strip().split():
    max_word [word] = [len(word)]
for word,len_word in max_word.items():
    if len_word == max(max_word.values()):
        print(f'字符串 "{str1}" 中出现长度最长的单词为:{word},长度为:{len_word[0]}')