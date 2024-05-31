# 9.定义一个函数，函数功能为：输出斐波那契数；
# 要求通过传参的形式指定要输出的斐波那契的数量
def fibonacci(n):
    a, b = 0, 1
    list_fibonacci = []
    while len(list_fibonacci) < n:
        list_fibonacci.append(a)
        a, b = b, a + b   # a 被赋予 b 的当前值，而 b 则被赋予 a 和 b 当前值的和
    return list_fibonacci

while True:
    n = int(input('请输入要获取的斐波那契数的数量:'))
    print(f'获取的 {n} 个斐波那契数为:{fibonacci(n)}')