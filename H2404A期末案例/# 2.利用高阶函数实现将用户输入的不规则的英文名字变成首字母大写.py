# 2.利用高阶函数实现将用户输入的不规则的英文名字变成首字母大写
# [“admin”,”JACK”,”banB”]---[“Admin”,”Jack”,”Banb”]
list_str = ['admin','JACK','banB']
ret = map(lambda char : char.title(), list_str)
print(list(ret))