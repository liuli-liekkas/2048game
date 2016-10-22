#题目：求1+2!+3!+...+20!的和。
#程序分析：此程序只是把累加变成了累乘。
def f(n):
    Sum = 0
    for i in range(1,n+1):
        sum = 1
        for j in range(1,i+1):
            sum *= j
        Sum += sum
    return Sum
print(f(20))