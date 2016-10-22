#题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
#程序分析：无。
def output(s,l):
    if l == 0:
        return 0
    else:
        print(s[l-1])
        output(s,l-1)
s = input('请输入字符:')
l = len(s)
output(s,l)