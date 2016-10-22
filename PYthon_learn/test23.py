'''打印出如下图案（菱形）:
   *
  ***
 *****
*******
 *****
  ***
   *
程序分析：先把图形分成两部分来看待，前四行一个规律，后三行一个规律，
利用双重for循环，第一层控制行，第二层控制列。'''
from sys import stdout
def f(n):
    for i in range(1,n+1):
        for j in range(n-i):
            stdout.write(' ')
        for j in range(2*i-1):
            stdout.write('*')
        print()
    for i in range(1,n):
        for j in range(1,i+1):
            stdout.write(' ')
        for j in range(2*(n-i)-1):
            stdout.write('*')
        print()
f(8)

