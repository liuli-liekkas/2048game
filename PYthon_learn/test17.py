#题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
#程序分析：利用while语句,条件为输入的字符不为'\n'。
import string
s = input('请输入数据:')
num = 0
space = 0
strs = 0
other = 0
for i in s:
    if i.isalpha():
        strs += 1
    elif i.isspace():
        space += 1
    elif i.isdigit():
        num += 1
    else:
        other += 1
print('char = %d,space = %d,digit = %d,others = %d' % (strs,space,num,other))