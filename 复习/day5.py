#!/usr/bin/env python3
# import collections
# point = collections.namedtuple("point", {"x","y"})
# p1 = point(3,2)
# print(p1.y)
#
# lst = collections.deque(["a","b","c"])
# lst.append("e")
# lst.appendleft("0")
# lst.pop()
# lst.popleft()
# print(lst)
#
#
# c = collections.Counter("aaabbccceedd")
# print(c)
#
# # lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 元素大于5的添加到字典k1的列表中，元素小于5的添加字典k2的列表中
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# dic = collections.defaultdict(list)
# for i in lst:
#     if i > 5:
#         dic["k1"].append(i)
#     else:
#         dic["k2"].append(i)
# print(dic)



import time
# # print(time.time())
# # print(time.localtime())
# # print(time.strftime("%Y-%m-%d %H:%M:%S"))
# # print(time.strftime("%X %x"))
# t = time.time()
# print(time.localtime(t))
# print(time.gmtime(t))
#
# s  = time.localtime()
# print(time.mktime(s))
#
# s = time.strftime("%Y-%m-%d", s)
# print(time.strptime(s,"%Y-%m-%d"))
#
# print(time.asctime(time.localtime()))
# print(time.ctime(time.time()))

# spf_day = "1991-05-06"
# spf_day_s = time.strptime(spf_day, "%Y-%m-%d")
# t1 = time.localtime()
# print("距离今天%s年%s月%s日" %(t1[0] - spf_day_s[0], t1[1] - spf_day_s[1],t1[2] - spf_day_s[2]))
import random
# print(random.random())
# print(random.uniform(1,3))
#
# print(random.randint(1,10))
# print(random.randrange(0,10,2))
#
# print(random.choice([1,2,3]))
# print(random.sample([1,2,3],2))


# def code(count):
#     s = ""
#     for i in range(count):
#         num = random.randint(0, 9)
#         chr1 = chr(random.randint(65, 90))
#         chr2 = chr(random.randint(97, 122))
#         s += random.choice([str(num),chr1,chr2])
#     return s
#
# print(code(6))
# import sys
# print(sys.path)
# print(sys.modules)
# print(sys.version)
# print(sys.platform)
import os
# os.chdir(r"../")
# print(os.getcwd())
# import time
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getatime(r"C:\Users\lanpa\Desktop\Python自动化21期\Python21\复习\hosts.ini"))))
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getmtime(r"C:\Users\lanpa\Desktop\Python自动化21期\Python21\复习\hosts.ini"))))
# size = 0
# def func(dir_path):
#     global size
#     if not os.path.exists(dir_path):return "目录不存在"
#     if not os.path.isdir(dir_path):return "不是目录"
#     for i in os.listdir(os.path.abspath(dir_path)):
#         if os.path.isfile(os.path.join(os.path.abspath(dir_path),i)):
#             size += os.path.getsize(os.path.join(os.path.abspath(dir_path),i))
#             print(os.path.join(os.path.abspath(dir_path),i),size)
#         else:
#             return func(os.path.join(os.path.abspath(dir_path),i))
# func(r"C:\Users\lanpa\Desktop\Python自动化21期\Python21\day8")
# print(size)