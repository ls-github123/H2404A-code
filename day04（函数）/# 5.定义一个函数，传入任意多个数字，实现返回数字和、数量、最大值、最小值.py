# 5.定义一个函数，实现传递任意多个数字。
# 函数功能实现 将所有数字的和、数字的数量、数字中的最大值、数字中的最小值进行返回
def process_num(*args):
    # 将输入转换为整数列表
    numbers = [int(num) for num in args if num.isdigit()]
    # 计算和、数量、最大值和最小值
    total = sum(numbers)
    count = len(numbers)
    max_value = max(numbers) if numbers else None
    min_value = min(numbers) if numbers else None
    return f'输入数字的总和为:{total}, 共输入了 {count} 个数字, 输入数字中的最大值为:{max_value}, 最小值为:{min_value}'

def process_input():
    numbers = []
    while True:
        str_num = input('请随机输入数字(输入 Q 停止): ')
        if str_num.upper() == 'Q':
            print('停止输入!')
            break
        elif str_num.isdigit():
            numbers.append(str_num)
        else:
            print('输入的字符无效，请重新输入')
    return process_num(*numbers)

# 调用函数并打印结果
print(process_input())
