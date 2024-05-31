# # 定义一个函数，函数功能实现将列表中的kk修改为大写的KK，将列表中的数字1修改为字符串1
# list1 = ["aa",4,5,["python",'kk',[1,0]],7]

def func():
    list1 = ["aa",4,5,["python",'kk',[1,0]],7]
    list1[3][1] = 'KK'
    list1[3][2][0] = '1'
    print(list1)
func()