#判断101-200之间有多少个素数，并输出所有素数。
# 判断素数的方法：用一个数分别去除2到sqrt(这个数)，
# 如果能被整除，则表明此数不是素数，反之是素数。
l=list(range(101,201))
l1=l[::1]
length =len(l)
def prime():
    num = 0
    for i in range(length):
        for j in range(2,l[i]):
            if l[i] % j == 0:
                l1.remove(l[i])
                break
    print(len(l1))
    print(l1)

prime()