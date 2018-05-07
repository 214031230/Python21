#!/usr/bin/env python3
import time
# 时间的3种格式
# 1、时间戳timestamp（机器识别),时间戳表示的是从1970年1月1日00:00:00开始按秒计算的偏移量。我们运行“type(time.time())”，返回的是float类型。
print(time.time())
# 2、元组struct_time（可操作类型）,struct_time元组共有9个元素共九个元素:(年，月，日，时，分，秒，一年中第几周，一年中第几天等）
print(time.gmtime())  # 英国伦敦格林尼治时间
print(time.localtime())  # 本地时间，即中国北京时间
# 3、字符串格式化Format String （人类可以看懂的） 例如：1991-03-22
print(time.strftime("%Y-%m-%d %H:%M:%S"))
print(time.strftime("%y-%m-%d %H:%M:%S %a %A %b %B"))
print(time.strftime("%c"))
print(time.strftime("%x %X"))
print(time.strftime("%j"))
print(time.strftime("%U"))
print(time.strftime("%Z"))
# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00=59）
# %S 秒（00-59）
# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天（001-366）
# %p 本地A.M.或P.M.的等价符
# %U 一年中的星期数（00-53）星期天为星期的开始
# %w 星期（0-6），星期天为星期的开始
# %W 一年中的星期数（00-53）星期一为星期的开始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %Z 当前时区的名称
# %% %号本身

# 时间格式之间的转换
# 时间戳 ---> 元组格式
struct = time.localtime(1500000)  # 把时间戳1500000 转成 北京时间的元组格式
print(struct)
struct1 = time.localtime(1500000)  # 把时间戳1500000 转成 格林尼治时间的元组格式
print(struct1)
struct2 = time.localtime()  # 把当前时间转成北京时间的元组格式
print(struct2)

#  元组格式---> 时间戳
struct = time.localtime(1500000)
time_stamp = time.mktime(struct)
print(time_stamp)

# 元组格式 ---> 字符串格式
struct = time.localtime()  # 定义一个元组格式的时间
str_time = time.strftime("%Y-%m-%d", struct)
print(str_time)

struct = time.localtime(15000000)  # 指定一个元组格式的固定时间
str_time = time.strftime("%Y-%m-%d", struct)
print(str_time)

# 字符串格式 ---> 元组格式  time.strptime(时间字符串,字符串对应格式)
str_time = time.strftime("%Y-%m-%d")
struct = time.strptime(str_time, "%Y-%m-%d")
print(struct)

# 其他
#结构化时间 --> %a %b %d %H:%M:%S %Y串
#time.asctime(结构化时间) 如果不传参数，直接返回当前时间的格式化串
asc_time = time.asctime(time.localtime())
print(asc_time)

#时间戳 --> %a %d %d %H:%M:%S %Y串
#time.ctime(时间戳)  如果不传参数，直接返回当前时间的格式化串
ct_time = time.ctime(time.time())
print(ct_time)

# 练习题： 计算时间差
import time
true_time=time.mktime(time.strptime('2017-09-11 08:30:00','%Y-%m-%d %H:%M:%S'))  # 把字符串转成时间戳格式
time_now=time.mktime(time.strptime('2017-09-12 11:00:00','%Y-%m-%d %H:%M:%S'))   # 把字符串转成时间戳格式
dif_time=time_now-true_time  # 获取相隔时间戳
struct_time=time.localtime(dif_time)  # 时间戳转换成元组格式
print(struct_time)
print(time.localtime())
print('过去了%d年%d月%d天%d小时%d分钟%d秒'%(struct_time.tm_year-1970,struct_time.tm_mon-1,
                                       struct_time.tm_mday-1,struct_time.tm_hour,
                                       struct_time.tm_min,struct_time.tm_sec))



