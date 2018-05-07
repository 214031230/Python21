#!/usr/bin/env python
# -*- coding:utf-8 -*-
# import time
# import os
# import sys

# 模块 py文件
# 模块是写好了但不直接使用的功能
# print()
# time()
# sleep()

# 为什么 这些模块中提供的方法 不能像print这些内置函数一样直接使用？
# 需要先导入模块再使用呢？
# 常用的 和某个操作相关的 根据相关性分类
# 分成不同的模块
# 模块还分为三种： 内置模块 扩展模块 自定义模块

# 内置模块
# import collections
# d = collections.OrderedDict()
# print(d)
#
# d['电脑'] = 10000
# d['苹果'] = 10
# print(d)
# for i in d:
#     print(i,d[i])
# print(d['电脑'])

# l= [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
# my_dict = {}
# for value in  l:
#     if value>66:
#         if my_dict.has_key('k1'):
#             my_dict['k1'].append(value)
#         else:
#             my_dict['k1'] = [value]
#     else:
#         if my_dict.has_key('k2'):
#             my_dict['k2'].append(value)
#         else:
#             my_dict['k2'] = [value]
# import time
# time.sleep()
# from time import sleep
# sleep()

# from collections import defaultdict
# values = [11, 22, 33,44,55,66,77,88,99,90]
# my_dict = defaultdict(list)
# for value in  values:
#     if value>66:
#         my_dict['k1'].append(value)
#     else:
#         my_dict['k2'].append(value)
# 默认这个字典的value是一个空列表
# d = {}
# print(my_dict)
# my_dict['a'].append(1)
# my_dict['b'].append(2)
# my_dict['c'] = 10
# print(my_dict)

from collections import namedtuple
# Point = namedtuple('Point',['x','y'])
# p = Point(1,2)
# print(p.x)
# print(p.y)
# Card = namedtuple('card',['rank','suit'])
# c = Card('2','红心')
# print(c.rank,c.suit)

# from collections import deque
# q = deque()
# q.append(1)
# q.append(2)
# q.append(3)
# q.append(3)
# print(q)
# print(q.pop())
# print(q)
# q.appendleft('a')
# q.appendleft('b')
# q.appendleft('c')
# print(q)
# print(q.popleft())
# print(q.popleft())

import time
# print(time.time())   # 时间戳时间 英国伦敦时间 1970 1 1 0 0 0
# print(time.time())   # 时间戳时间 北京时间 1970 1 1 8 0 0
# 二进制 十进制
# 年月日时分秒
# 格式化时间  用字符串表示的时间
# print(time.strftime('%H:%M:%S'))
# print(time.strftime('%Y-%m-%d %H:%M:%S'))
# print(time.strftime('%x'))
# print(time.strftime('%c'))

# print('{0},{1}'.format(1,2))

# 结构化时间
# t = time.localtime()
# print(t)

# 时间戳 - 结构化时间 - 格式化时间
# import time
# print(time.time())
# print(time.localtime(1500000000))
# print(time.localtime(1600000000))
# print(time.localtime(2000000000))
# struct_time = time.gmtime(2000000000)
# print(time.strftime('%Y-%m-%d %H:%M:%S'))
# print(time.strftime('%Y-%m-%d %H:%M:%S',struct_time))
#
# # '2015-12-3 8:30:20' 时间戳时间
# s = '2015-12-3 8:30:20'
# ret = time.strptime(s,'%Y-%m-%d %H:%M:%S')
# print(ret)
# print(time.mktime(ret))

# 1.拿到当前时间的月初1号的0点的时间戳时间
# 2.计算任意 两个时间点之间经过了多少年月日时分秒

# time
# datetime

# import random
# s = ''
# for i in range(4):
#     s += str(random.randint(0,9))
# print(s)

# 数字 字母
# print(chr(98))   # (65,90)A (97,122)a
# import random
# num = random.randint(65,90)
# print(chr(num))
# num = random.randint(97,122)
# print(chr(num))

# 某一位 到底是一个字母 还是一个数字的事儿也是随机的
# import random
# id = ''
# for i in range(6):
#     num = random.randint(65,90)
#     alpha1 = chr(num)
#     num = random.randint(97,122)
#     alpha2 = chr(num)
#     num3 = str(random.randint(0,9))
#     print(alpha1,alpha2,num3)
#     s = random.choice([alpha1,alpha2,num3])
#     id+=s
# print(id)

import sys  # python解释器
# sys.exit()   # 解释器退出 程序结束
# print('*'*10)
# print(sys.path)
# 一个模块是否能够被导入 全看在不在sys.path列表所包含的路径下
# print(sys.modules)  # 放了所有在解释器运行的过程中导入的模块名

# print(sys.argv)
# if sys.argv[1] == 'alex' and sys.argv[2] == 'alex3714':
#     print('可以执行下面的n行代码')
# else:
#     sys.exit()
# 在执行python脚本的时候，可以传递一些参数进来
# mysql username password

# os模块
# import os
# print(os.getcwd())
# os.chdir(r'D:\EVA')
# print(os.getcwd())
# open('aaaaaaa','w').close()   # 文件创建到了当前工作目录下

# import os
# 'path1%spath2'%os.pathsep

import os
# os.system("dir")   # exec
# ret = os.popen('dir').read()
# print(ret)

# win linux
    # 操作系统自己有的一种简单的语言

print(os.path.abspath('4.模块.py'))
print(os.path.dirname(r'D:\EVA\周末班python21\day5\4.模块.py'))
print(os.path.split(r'D:\EVA\周末班python21\day5\4.模块.py'))
print(os.path.basename(r'D:\EVA\周末班python21\day5\4.模块.py'))
# print('\\n\\t\\t\\n')
# print(r'\n\t\t\n')   # real
# print(os.path.dirname(r'D:\EVA\周末班python21\day5'))
#
# print(os.path.join('D:\\','EVA','PYTHON','AAA'))

# print(os.path.getsize(r'D:\EVA\周末班python21\day5\4.模块.py'))
# print(os.path.getsize(r'D:\EVA\周末班python21\day5'))
# ret = os.listdir(r'D:\EVA\周末班python21\day5')
# print(ret)
# sum = 0
# for path in ret:
#     if os.path.isfile(path) is True:
#         sum+= os.path.getsize(path)
# print(sum)

# 计算文件夹的总大小