import datetime

# 获取当前时间
now = datetime.datetime.now()
# 获取7天的时间间隔
day7 = datetime.timedelta(days=7)
# 在当前的时间基础上加7天
ret = now + day7
# print(now, ret)
print(ret.strftime("%Y-%m-%d %H:%M:%S"))


