# 货币换算案例
while True:
    currency = input('请输入要换算的货币及金额(美元:$\人民币:￥):')
    if currency.startswith('$'):
        print(f'换算为人民币的金额为:{float(currency[1:]) * 7.25 :.3f}')
        
    elif currency.startswith('￥'):
        print(f'换算为美元的金额为:{float(currency[1:]) / 7.25 :.3f}')
        
    else:
        print('输入的数值非法')