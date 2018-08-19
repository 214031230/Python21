import datetime


now = datetime.datetime.now()
print(now, type(now))
ret = now.strftime("%Y-%m-%d %H:%M:%S")
print(ret, type(ret))
