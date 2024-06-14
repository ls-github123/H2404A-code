# 5.能将小明输入的数据录入并按照从高到低的顺序输出  排序利用高阶函数实现
 	# 输入和输出如图所示：
 	# 输入：
 	# 	1.75 1.56 1.98 1.73 1.69 1.82 1.84
 	# 输出：
    #   1.98 1.84 1.82 1.75 1.73 1.69 1.56
heigh_list = []
while True:
    HeighInput = float(input('请输入身高数据(输入0结束):'))
    if HeighInput == 0:
        break
    else:
        heigh_list.append(HeighInput)
ret = sorted(heigh_list, reverse = True)
print(f'整合后的数据输出为:{ret}')
