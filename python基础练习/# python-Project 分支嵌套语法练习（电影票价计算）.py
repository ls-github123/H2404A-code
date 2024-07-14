# python-Project 分支嵌套语法练习（电影票价计算）

# 定义所需变量，为变量赋值
price_3D = 120
price_none_3D = 90
week = int (input ('今天是周几（周一至周五用“1-5”代替，周六和周末用“6、7”代替）：'))
movie_3D = input ('3D输入“1”，非3D输入“0”：')
VIP = input ('是VIP身份输入“1”，非VIP身份输入“0”：')

if  week == '6' or week == '7' :  # 首先判断当前时间是否为周末_判断当前时间为 周六或周日
    if movie_3D == '1' : # 判断是否观看3D影片_判断为周六或周日观看3D影片
        
        if VIP == '1' : #判断是否为VIP客户_周六或周日观看3D影片的VIP客户
           money = price_3D * 0.9

        else: #判断为_周六或周日观看3D影片的非VIP客户
            money = price_3D

    else: #判断为 不观看3D影片

        if VIP == '1': #判断是否为VIP客户_判断为不观看3D影片的VIP客户
            money = price_none_3D * 0.8

        else: #判断为_不观看3D影片的非VIP客户
            money = price_none_3D * 0.9
    
else: #判断当前时间为_周一至周五

    if movie_3D == '1' :

         if VIP == '1':
             money = price_3D * 0.7

         else:
             money = price_3D * 0.9 
    
    else:

        if VIP == '1':
            money = price_none_3D * 0.7

        else:
            money = price_none_3D * 0.8

print (f'电影票的总金额是:{money:.2f}元')  # 输出购买所对应电影票的金额数据