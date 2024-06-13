# 案例
# 单独案例list1 = [1,3,5,7,9]
# 实现通过高阶函数和匿名函数实现得到最终的结果 13579   (结果是整型类型的数据)

# 使用高阶函数和匿名函数获取10-80之间的回文数
# 使用高阶函数和匿名函数实现对所有回文数取平方值
# 使用高阶函数和匿名函数实现对所有平方值进行结果求和
# 使用高阶函数和匿名函数实现对所有的平方值结果进行排序

from functools import reduce
list1 = [1, 3, 5, 7 ,9]
result = reduce(lambda x,y: x * 10 + y, list1)
print(result)


list2 = [i for i in range(10,81)]
ret1 = filter(lambda i :str(i) == str(i)[::-1], list2)
palindrome_numbers = tuple(ret1) # 
# filter 和 map 返回的都是迭代器，因此在使用一次之后就会耗尽，无法再次使用
# 额外定义一个变量 palindrome_numbers 对数据进行接收缓存
print(f'1.数字10-80之间的回文数为:{palindrome_numbers}')

ret2 = map(lambda i : i ** 2, palindrome_numbers)
palind1 = tuple(ret2)
print(f'2.所有回文数取平方值后为:{palind1}')

ret3 = reduce(lambda x, y : x + y, palind1)
print(f'3.所有平方值的结果求和为:{ret3}')

ret4 = sorted(list(palind1), reverse=True)
print(f'4.对所有平方值结果进行倒序排序为:{ret4}')
