#题目：输出指定格式的日期。
#程序分析：使用 datetime 模块。
# 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
# 创建日期对象
# 日期算术运算
# 日期替换
import datetime
print(datetime.datetime.today().strftime('%m-%d-%Y'))
lasttime = datetime.date(1941,1,5)
print(lasttime.strftime('%m-%d-%Y'))
newtime = lasttime + datetime.timedelta(days=100)
print(newtime.strftime('%m-%d-%Y'))
latetime = lasttime.replace(year = lasttime.year + 1)
print(latetime.strftime('%m-%d-%Y'))