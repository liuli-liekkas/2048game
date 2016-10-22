#输入三个整数x,y,z，请把这三个数由小到大输出。
l=[]
a = int(input('请输入第一个数:'))
l.append(a)
b = int(input('请输入第二个数:'))
l.append(b)
c = int(input('请输入第三个数:'))
l.append(c)
for i in range((len(l)-1)):
    if(l[i] > l[i+1]):
        l[i],l[i+1] = l[i+1],l[i]
        i = 0
print(l)

