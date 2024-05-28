# 用户任意输入一个文件名，实现得到该文件的备份文件名
# 例如:用户输入'aaa.txt.py'得到'aaa.txt-副本.py'
file_name = input('请输入任意文件名,包含后缀:')
num = file_name.rfind('.')

old_file = file_name[:num] # 获取文件名
file_end = file_name[num:] # 获取文件后缀名

new_file = old_file + '-副本' + file_end
print(new_file)