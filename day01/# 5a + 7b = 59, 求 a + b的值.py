# 5a + 7b = 59, 求 a + b的值
def find_a_and_b():
    for a in range(100):
        b = (59 - 5 * a) / 7
        if b.is_integer(): # 确保b是整数
            print(f'a = {a}, b = {int(b)}, a + b = {a + int(b)}')
find_a_and_b()