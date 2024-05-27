# 三目运算符
# -- 三元表达式 本质是一个简单的if else 判断

while True:
    age = int(input('请输入年龄:'))
    if age >= 18:
        print('成年了，可以进网吧')
    else:
        print('未成年禁止入内')
    break
        
print('成年了，可以进入网吧') if age >= 18 else print('未成年禁止入内!')