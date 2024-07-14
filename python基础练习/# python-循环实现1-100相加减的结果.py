# python-循环实现1-2+3-4+5-6……+99-100的结果

sum = 0
for x in range (1,101,1):
    
    if x % 2 == 1:
        
        sum += x
    
    else:

        sum -= x

print (sum)