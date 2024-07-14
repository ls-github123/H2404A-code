# 假设一张纸厚度为0.5毫米，珠穆朗玛峰的高度为8848.48米，计算纸对折多少次后，其厚度能大于珠峰的高度

paper_thickness = 0.5 / 1000  # 0.50 除以1000，转换单位为 米
everest_height = 8848.48

folds = 0  # 初始化对折次数为零

while paper_thickness <= everest_height:
    
    paper_thickness *= 2 
    
    folds += 1

print (f'经计算得，计算纸至少经过 {folds} 次对折后，其厚度能大于珠峰高度')