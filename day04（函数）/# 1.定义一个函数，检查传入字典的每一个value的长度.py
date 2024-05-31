# 1.定义一个函数，检查传入字典的每一个value的长度
# 如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者
def dict_value():
    dict1 = {'CPU':'intel_x86', 'RAM':'samsung','ROM':'wd','GPU':'NV'}
    for i, j in dict1.items():
        if len(j) > 2:
            dict1 [i] = j[:2]
    return dict1
print(dict_value())