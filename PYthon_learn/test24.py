#题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
#程序分析：请抓住分子与分母的变化规律。
def f(n):
    a = 2
    b = 1
    sum = 0
    for i in range(1,n+1):
        sum += a/b
        a,b = a+b,a
    return sum
print(f(20))