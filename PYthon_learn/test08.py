#输出9*9乘法口诀表
for i in range(1,10):
    for j in range(1,i+1):
        result = i * j
        print('%d * %d = %d ' %(i,j,result),end = '')
        j += 1
    print('')
    i += 1
