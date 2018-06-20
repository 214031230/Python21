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
# import os
# # os.chdir(r"../")
# # print(os.getcwd())
# # import time
# # print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getatime(r"C:\Users\lanpa\Desktop\Python自动化21期\Python21\复习\hosts.ini"))))
# # print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getmtime(r"C:\Users\lanpa\Desktop\Python自动化21期\Python21\复习\hosts.ini"))))
#
# size = 0
# def func(dir_path):
#     global size
#     for i in os.listdir(dir_path):
#         if os.path.isdir(os.path.join(dir_path,i)):
#             func(os.path.join(dir_path, i))
#         else:
#             size += os.path.getsize(os.path.join(dir_path,i))
#             print(os.path.join(dir_path,i),os.path.getsize(os.path.join(dir_path,i)))


# def func(dirs):
#     dir_list = os.listdir(dirs)
#     for i in dir_list:
#         if os.path.isdir(os.path.join(dirs, i)):
#             func(os.path.join(dirs, i))
#         else:
#             print(os.path.join(dirs,i))

# func(r"/Users/xuxu/Desktop/python自动化21期/Python21/day8")



# import re
# s = "hadjfla84u2knladf0239424"
# print(re.findall(r"\d", s))
# print(re.search(r"\d", s).group())
# print(re.match(r"\w", s).group())
# print(re.sub(r"\d","A",s))
# print(re.subn(r"\w","3",s))
# obj = re.compile("\d")
# print(obj.sub("H",s))
# ret = obj.finditer(s)
# print(next(ret).group())
# print(next(ret).group())
#
# lst = [i.group() for i in ret]
# print(lst)



#
# lst = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
#
# def func(lst,num,start=0,end=None):
#     end = len(lst) - 1 if end is None else end
#     if start > end:return None
#     mid = (end - start) // 2 + start
#
#     if lst[mid] > num:
#         return func(lst,num,start,mid-1)
#     elif lst[mid] < num:
#         return func(lst,num,mid+1,end)
#     else:
#         return mid
#
# print(func(lst,2))



menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}
# l = menu
# c = []
# while True:
#     for i in l:
#         print(i)
#     choice = input(">>>:").strip()
#     if not choice:continue
#     if choice in l:
#         c.append(l)
#         l = l[choice]
#     elif choice.lower() == "b":
#         l = c.pop()
#     else:
#         print("你输入的节点不存在")
# def fun(dic):
#     while 1:
#         for i in dic:
#             print(i)
#         choice = input(">>>:")
#         if not choice:continue
#         if choice.lower() == "b":return
#         if choice.lower() == "q":return "q"
#         if choice in dic:
#             ret = fun(dic[choice])
#             if ret == "q":
#                 return "q"
#         else:
#             print("节点不存在")
#
#
# fun(menu)


print(6*5*4*3*2*1)
def fun(num):
    if num == 1:return num
    return fun(num - 1) * num

"""
def fun(6):
    return 120 * 6
    
def fun(5):
    if 5 == 1:return num
    return 24 * 5

def fun(4):
    if 4 == 1:return num
    return 6 * 4
def fun(3):
    if 3 == 1:return num
    return 2 * 3
    
def fun(2):
    if 2 == 1:return num
    return 1 * 2
def fun(1):
    if 1 == 1:return 1
    
"""
