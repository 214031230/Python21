#!/usr/bin/env python3
# 内置模块
# collections 在内置数据类型（dict、list、set、tuple）的基础上，collections模块还提供了几个额外的
# 数据类型：Counter、deque、defaultdict、namedtuple和OrderedDict等。
import collections

# 1.namedtuple: 生成可以使用名字来访问元素内容的tuple
# point = collections.namedtuple("point", ["x", "y"])
# res = point(100, 50)
# print(res.x)
# print(res.y)

# 2.deque: 双端队列，可以快速的从另外一侧追加和推出对象  不常用
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。
# lst = collections.deque(["a", "b", "c"])
# lst.append("e")
# lst.appendleft(1)
# lst.popleft()
# print(lst)

# 3.Counter: 计数器，主要用来计数
# Counter类的目的是用来跟踪值出现的次数。它是一个无序的容器类型，以字典的键值对形式存储，其中元素作为key，其计数作为value。计数值可以是任意的Interger（包括0和负数）。Counter类和其他语言的bags或multisets很相似
# c = collections.Counter("abcdeabcdabcaba")
# print(c)
# 输出：Counter({'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1})

# 4.OrderedDict: 有序字典  不常用
# OrderedDict的Key是有序的，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
# dic = collections.OrderedDict([["a", 1], ["b", 1]])
# print(dic)

# 5.defaultdict: 带有默认值的字典
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 元素大于5的添加到字典k1的列表中，元素小于5的添加字典k2的列表中
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 原生字典解决方法
# dic1 = {}
# for i in lst:
#     if i > 5:
#         if dic1.get("k1"):
#             dic1["k1"].append(i)
#         else:
#             dic1["k1"] = []
#             dic1["k1"].append(i)
#     else:
#         if dic1.get("k2"):
#             dic1["k2"].append(i)
#         else:
#             dic1["k2"] = []
#             dic1["k2"].append(i)
# print(dic1)
# 默认值字典解决方法
# dic2 = collections.defaultdict(list)
# for i in lst:
#     if i > 5:dic2["k1"].append(i)
#     else:dic2["k2"].append(i)
# print(dic2)


