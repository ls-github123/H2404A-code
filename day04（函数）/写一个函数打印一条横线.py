# 写一个函数打印一条横线
# 打印自定义行数的横线

def print_one_line():
    print('_' * 30)
    
# 打印多条横线
def print_num_line(num):
    i = 0
    while i < num:
        print_one_line()
        i += 1

while True:
    line_num = input('请输入要打印的横线条数:')        
    print_num_line(int(line_num))