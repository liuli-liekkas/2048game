#写一个函数，实现对整数的排序，默认升序排列。 不能使用任何内置函数和第三方库
kw = []
while True:
    a = input('请输入数据:')
    if a == 'q':
        break
    b = int(a)
    kw.append(b)
print('输入的数据数列为:{}'.format(kw))
def newsort(s=0):
    l = kw[:]
    lenth = len(l)
    if s == 0:
        while lenth > 0:
            for i in range(lenth-1):
                if (l[i] > l[i+1]):
                    l[i],l[i+1] = l[i+1],l[i]
            lenth -= 1
    elif s == 1:
        while lenth > 0:
            for i in range(lenth-1):
                if (l[i] < l[i+1]):
                    l[i],l[i+1] = l[i+1],l[i]
            lenth -= 1
    return l
print('排序后的数列为:{}'.format(newsort()))

#插入排序
def sort(lst,reverse=False):
    dst = []
    for n in lst:
        for i,e in enumerate(dst):
            if not reverse:
                if n < e:
                    dst.insert(i,n)
                    break
            else:
                if n > e:
                    dst.insert(i,n)
                    break
        else:
            dst.append(n)
    return dst

def sort(lst,cmp=None,reverse=False):
    def default_cmp():
        if a > b:
            return 1
        if a == b:
            return 0
        if a < b:
            return -1
    if cmp is None:
        cmp = default_cmp() #函数是一等对象的一个体现
    dst = []
    for n in lst:
        for i, e in enumerate(dst):
            if not reverse:
                if cmp(n,e) < 0:
                    dst.insert(i, n)
                    break
            else:
                if cmp(n,e) > e:
                    dst.insert(i, n)
                    break
        else:
            dst.append(n)
    return dst