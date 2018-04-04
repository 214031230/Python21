#!/usr/bin/env python3

# 列表转字符串，用"_"拼接
# li = ['alex', 'eric', 'rain']
# li_str = "_".join(li)
# print(li_str)

# 去掉元素的空格 并查找以a开头以c结尾的元素
li = ["alec", " aric", "Alex", "Tony", "rain"]
tu = ("alec", " aric", "Alex", "Tony", "rain")
dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}

# for i, value in enumerate(li, 0):
#     value = value.strip()
#     if value.startswith("a") and value.endswith("c"):
#         print(value)
#     li[i] = value
# print(li)

# li1 = []
# for i, value in enumerate(tu, 0):
#     value = value.strip()
#     if value.endswith("c") and value.startswith("a"):
#         print(value)
#     li1.append(value)
#     tu = tuple(li1)
# print(tu)


# for key in dic.keys():
#     value = dic[key].strip()
#     if value.startswith("a") and value.endswith("c"):
#         print("%s:%s" % (key, dic[key].strip()))
#         dic[key] = value
# print(dic)
