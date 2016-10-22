while True:
    money = int(input('请输入利润:'))
    arr = [0,100000,200000,400000,600000,1000000]
    rat = [0.1,0.075,0.05,0.03,0.015,0.01]
    profit = 0
    for i in range(5,-1,-1):
        if money > arr[i]:
            profit += ((money - arr[i]) * rat[i])
            money = arr[i]
    print(profit)