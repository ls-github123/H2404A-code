# 7.二分查找算法实现从列表中快速的查询某个指定数据所在列表的下标
list1 = [1,3,8,16,24,37,49,51,62,70,84,96,102,258,347]
def func_recursion(lst, n, start, end):
    if end >= start:
        Mid = (start + end) // 2
        if lst[Mid] == n:
            return f'要查询的数据下标为{Mid}'
        elif lst[Mid] < n:
            return func_recursion(lst, n ,Mid + 1, end)
        elif lst[Mid] > n:
            return func_recursion(lst, n, start, Mid - 1)
    else:
        return '范围内没有要查询的数据'
    
Data = int(input('请输入要查询的数据:'))
print(f'输入数据{data},查询结果为:{func_recursion(list1, Data, 0, len(list1) - 1)}')
