# python-project 体重BMI指数计算器
# 体重指数 = 体重 (kg) / (身高 (m) × 身高 (m))
     # 体重指数小于18.5属于偏瘦
 	 # 体重指数介于18.5和20.9之间，属于苗条
 	 # 体重指数介于20.9和24.9之间属于适中
 	 # 体重指数超过24.9偏胖


weight = float ( input ('请输入你的真实体重（KG）：'))
height = float ( input ('请输入你的当前身高（M）：'))
BMI = weight / height**2

if BMI < 18.5 :
    print (f'你的当前体重指数为{BMI:.2f}，属于 <偏瘦> 体型！')

elif 18.5 <= BMI < 20.9 :
    print (f'你的当前体重指数为{BMI:.2f}，属于 <苗条> 体型！')

elif 20.9 <= BMI <=24.9 :
    print (f'你的当前体重指数为{BMI:.2f}，属于 <适中> 体型！')

else :
    print (f'你的当前体重指数为{BMI:.2f}，已超过偏胖指数 24.9，属于 <偏胖-坦克> 体型，请注意饮食搭配，多运动！')