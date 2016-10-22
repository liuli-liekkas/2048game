#将一个列表的数据复制到另一个列表中。
l1 = []
i = 0
while i <= 9:
    a = input('请输入10个数据:')
    l1.append(a)
    i += 1
l2 = l1[:]
print('原先的列表是:{}')
print('复制出来的数据是:{}'.format(l2))


