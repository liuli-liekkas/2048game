#题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
#程序分析：学会分解出每一位数。
num = int(input('请输入一个数字:'))
l = []
n = 1
num2 =num
for i in range(20):
    l.append(num2 % 10)
    num2 = num2 // 10
    if num2 != 0:
        n += 1
    else:
        break
print(l)
print(n)
