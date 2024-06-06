# 文件拷贝
# 1.让用户输入 要进行拷贝的文件/文件路径
# 2.实现拷贝当前文件(拷贝后的文件需要与源文件在同一级目录下)

# 获取拷贝后的文件名 = 源文件名 + '-副本' + 原后缀名
# 读取源文件中的所有内容
# 将内容写入新的文件中

file = input('请输入要拷贝的文件:')
num = file.rindex('.')
start = file[:num]
end = file[num:]
new_file = start + '-副本' + end
with open(file, 'r', encoding='utf8') as f:
    data = f.read()

with open(new_file, 'w', encoding='utf8') as f:
    f.write(data)