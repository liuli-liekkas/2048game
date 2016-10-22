#题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
#程序分析：无。
def f(n):
    l = []
    num = 1
    num2 = n
    for i in range(100):
        l.append(num2 % 10)
        num2 = num2 // 10
        if num2 != 0:
            num += 1
        else:
            break
    if num % 2 == 1:
        n1 = 0
        for i in range((num-1)//2):
            if l[i] == l[num-i-1] :
                n1 += 1
            else:
                print('这不是一个回文数')
                break
        if n1 == (num-1)//2:
            print('这是一个回文数')
    if num % 2 == 0:
        n2 = 0
        for i in range(num//2):
            if l[i] == l[num-i-1]:
                n2 += 1
            else:
                print('这不是一个回文数')
                break
        if n2 == (num)//2:
            print('这是一个回文数')
num = int(input('请输入一个数:'))
f(num)
