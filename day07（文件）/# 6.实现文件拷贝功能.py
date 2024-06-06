# 6.实现文件拷贝功能
# 让用户随机输入一个文件名，实现将这个文件进行拷贝
# 例如：文件名为 day7.md  拷贝后的文件为 day7[复件].md
file_name = input('请输入要拷贝文件的完整文件名:')
num = file_name.rindex('.')
start = file_name[:num]
end = file_name[num:]
new_file_name = start + '[复件]' + end
with open(file_name, 'r', encoding='utf8') as file:
    data = file.read()
with open(new_file_name, 'w', encoding='utf8') as f:
    f.write(data)
print(f'文件{file_name}拷贝完成')