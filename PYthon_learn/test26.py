#题目：利用递归方法求5!。
#程序分析：递归公式：fn=fn_1*4!
def f(n):
    sum = 1
    for i in range(1,n+1):
        sum *= i
    return sum
print(f(5))

def f(n):
    if n == 1:
        return 1
    else:
        return n*f(n-1)
print(f(5))