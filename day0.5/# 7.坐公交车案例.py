# 7.坐公交车案例
while True:
    price = int(input('请输入卡内余额:'))
    if price >= 2:
        print('可以上车')
        seat = int(input('请输入车上剩余座位数:'))
        if seat >= 1:
            print('有空余座位,请及时坐好')
            break
        else:
            print('无空余座位,请站稳扶好!')
            break
    else:
        print('余额不足,请下车步行')