# 2.高阶函数和匿名函数实现,字符串所有单词首字母大写，其余字母小写
str1 = "hello world hello python"
str_list = [word for word in str1.split(' ')]
ret = map(lambda word:word.title(), str_list)
str2 = ' '.join(list(ret))
print(f'字符串首字母大写转换后输出为:{str2}')