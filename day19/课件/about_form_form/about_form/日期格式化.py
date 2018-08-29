import datetime


now = datetime.datetime.now()
print(now, type(now))
# 把Python中日期格式的时间转换成字符串格式的时间
print(now.strftime("%Y-%m-%d"))
# 把日期格式的时间转换回Python中的日期格式

