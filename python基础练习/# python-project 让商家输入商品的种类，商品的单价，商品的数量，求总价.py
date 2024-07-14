# python-project 让商家输入商品的种类，商品的单价，商品的数量，求总价
# 例：print("xxx商品 xxx元一件，购买xxx件，需要花费xxx元")

name = str (input ('请输入商品名称：'))
unit_price = float (input ('请输入商品单价（元/件）： '))
num = int (input ('请输入商品数量（件）：'))
price = unit_price * num

print (f'商品品名：{name} ，{unit_price} 元/件，购买 {num} 件，总计需要花费 {price:.2f} 元！')