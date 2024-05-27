# for else
# for 循环正常执行结束会执行else中的代码

for i in range(1,6):
    print(i)
else:
    print('执行完成')

print('-' * 28)

for i in range(1,6):
    if i == 5:
        break
    else:
        print(i)
else:
    print('执行完成')