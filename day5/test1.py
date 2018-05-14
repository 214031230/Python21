#!/usr/bin/env python3
import time
# 时间戳
# print(time.time())
#
# # 字符串类型
# print(time.strftime("%Y-%m-%d %H:%M:%S"))
# print(time.strftime("%x %X"))
#
# # 元组类型
# print(time.localtime())
# print(time.gmtime())
# print(time.gmtime(0))

# 字符串和时间戳进行转换必须先转换成元组

# # 时间戳转换成元组
# time_stamps = time.time()
# print(time.localtime(time_stamps))
#
# # 元组转成时间戳
# time_struct = time.localtime(0)
# print(time.mktime(time_struct))

# 字符串转成元组
# print(time.strptime(time.strftime("%Y-%m-%d"), "%Y-%m-%d"))

# # 元组转字符串
# print(time_struct)
# print(time.strftime("%Y-%m-%d", time_struct))

# # 字符串转元组
# print(time.strptime(time.strftime("%Y-%m-%d"), "%Y-%m-%d"))
# # 元组转字符串
# print(time.strftime("%Y-%m-%d", time.localtime()))

# import random
# print(random.random())
# print(random.randint(1, 9))
# print(random.randrange(1, 9, 2))
# print(random.choice([1, 2, 3]))
# print(random.sample([1, 2, 3], 2))

# import sys
# print(sys.argv)  # 返回一个list 存放程序的路径
# print(sys.version)  # 返回python的版本
# print(sys.path)  # 返回环境变量
# print(sys.platform)  # 操作系统名称
# print(sys.modules)  # 返回加载的所有模块

import os
# print(os.getcwd())
# # os.chdir("/Users/xuxu")
# # print(os.getcwd())
# # os.system("ls -l")
# ret = os.popen("ls -l").read()
# print(ret)
# print(os.path.abspath("../day5"))
# print(os.path.split("/day5/day4/day3"))
# print(os.path.basename("/day5/day4/da"))
# print(os.path.exists("/Users"))
# print(os.stat("../day5"))
import re
s = "1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) ) + ( 4 * 5 )"
print(re.search("\([^()].+\)", s).group())