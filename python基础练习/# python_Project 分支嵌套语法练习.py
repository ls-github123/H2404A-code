# python_Project 分支嵌套语法练习

ticket = str (input('是否买到了高铁票（ 已买到 / 未买到 ）：'))

if ticket == '未买到' :
   print ('没买到票，扒火车跑路吧！')
    
else:
    print ('出发前往高铁站，准备乘坐高铁')
    print ('乘坐高铁前需安检，且你已随身携带刀具')
    
    knife_length = float (input('请输入所携带刀具刀刃部分长度（厘米）：'))
    
    if knife_length <= 3:
        print ('正常通过，乘坐高铁')
      
    else:
        print ('涉嫌违法，满身大汉！')