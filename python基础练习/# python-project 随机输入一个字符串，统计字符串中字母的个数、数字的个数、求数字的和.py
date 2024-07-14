# 随机输入一个字符串，统计字符串中字母的个数、数字的个数、求数字的和 str1 = “hello123python456world789”

str_1 = 'hello123python456world789'

letter_count = 0
digit_count = 0
digit_sum = 0

# 遍历字符串中的每个字符
for char in str_1:
    
    # 检查字符是否为字母
    if char.isalpha () == True:
        letter_count += 1
    
    # 检查字符是否为数字
    elif char.isdigit () == True:
        digit_count += 1
        digit_sum += int (char)

print(f'字符串 {str_1} 中，字母的个数为 {letter_count} ,数字的个数为 {digit_count} ,数字的和为 {digit_sum}')