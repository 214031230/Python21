#!/usr/bin/env python3
# 模块的定义
# 模块就是py文件
# 模块是写好了但不直接使用的功能代码

#  导入模块的方法
import time  # 导入整个time模块
import time,os  # 导入多个模块
from time import sleep  # 导入time模块的sleep方法
from time import sleep,time  # 导入time模块的多个方法

# print() len() 这些模块为什么不需要导入也可以使用？
# python启动默认会加载一些必备模块到内存中，如果去掉这些模块会影响python的编程方式

# 为什么不在python启动的时候把所有模块都加载到内存中？
# 模块是有大小的，如果全部加载到内存中会把内存撑爆

# 模块分为三种： 内置模块 扩展模块 自定义模块

# 内置模块
# collections 在内置数据类型（dict、list、set、tuple）的基础上，collections模块还提供了几个额外的
# 数据类型：Counter、deque、defaultdict、namedtuple和OrderedDict等。
import collections

# 1.namedtuple: 生成可以使用名字来访问元素内容的tuple
point = collections.namedtuple("point", ["x", "y"])
res = point(100, 50)
print(res.x)
print(res.y)

# 2.deque: 双端队列，可以快速的从另外一侧追加和推出对象
#
# 3.Counter: 计数器，主要用来计数
#
# 4.OrderedDict: 有序字典
#
# 5.defaultdict: 带有默认值的字典

# os模块
# time模块
#

