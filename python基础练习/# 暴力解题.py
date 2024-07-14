# 暴力解题


for x in range (-100,100,1): 

    num_1 = (x+2)*(x+3)*(x+4)*(x+5)
    num_2 = (x-2)*(x-3)*(x-4)*(x-5)
    
    if num_1 // num_2 == 1:

     print (x)