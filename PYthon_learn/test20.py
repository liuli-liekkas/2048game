#题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；
# 再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
#程序分析：1:100 2:100+50*2 3:100+50*2+25*2
def f(high,n):
    if n == 1:
        return high
    else:
        nowhigh = high
        for i in range(2,n+1):
            nowhigh = nowhigh + high/2**(i-2)
        print('球从%d落下,第%d落地时,共经过%f米,第%d次反弹%f' % (high,n,nowhigh,n,high/2**(n)))
f(100,10)



