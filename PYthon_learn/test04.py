#!/usr/bin/python3
#输入某年某月某日，判断这一天是这一年的第几天？
year = int(input('请输入哪一年:'))
month = int(input('请输入哪一月:'))
day = int(input('请输入哪一天:'))
if (0 < month < 13):
    if (0 < day < 32):
        months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
        sum = 0
        sum += months[month - 1]
        sum += day
        if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
            sum += 1
        print('这一天是%d年的第%d天' % (year, sum))

    else:
        print('输入的天数错误')

else:
    print('输入的月份错误')

