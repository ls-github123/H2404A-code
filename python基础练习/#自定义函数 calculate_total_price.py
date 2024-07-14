#自定义函数 calculate_total_price
#程序需求：根据商家输入的鱼的种类、单价、数量，计算并输出最终的总价
#语言：python

def calculate_total_price (fish_type, price_per_kg, quantity):
    total_price = price_per_kg * quantity
    return total_price

if __name__ == "__main__": #检查当前脚本是否被直接执行，如果是，则执行下面的代码块
    fish_type =input("请输入鱼的种类：")
    price_per_kg = float(input("请输入鱼的单价(元/斤)："))
    quantity = float(input("请输入鱼的数量（斤）："))
    
    total_price = calculate_total_price(fish_type, price_per_kg, quantity)

    print ( "{}鱼{}元/斤，一条鱼约{}斤，需要花费{}元".format(fish_type, price_per_kg, quantity, total_price))