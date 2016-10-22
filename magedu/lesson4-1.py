#分别使用递归、循环和生成器求菲波那切数列
def fib1(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return (fib1(n-1)+fib1(n-2))
n = 10
l = []
for i in range(n+1):
    l.append(fib1(i))
print(l)


def fib2(n):
    fibs2 = []
    if n == 0:
        fibs2 = [1]
    elif n == 1:
        fibs2 = [1,1]
    else:
        fibs2 = [1,1]
        for i in range(2,n+1):
            fibs2.append(fibs2[i-1] + fibs2[i-2])
    return fibs2
print(fib2(10))

