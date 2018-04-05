#!/usr/bin/env python3

# 列表转字符串，用"_"拼接
# li = ['alex', 'eric', 'rain']
# li_str = "_".join(li)
# print(li_str)

# 去掉元素的空格 并查找以a开头以c结尾的元素
# li = ["alec", " aric", "Alex", "Tony", "rain"]
# tu = ("alec", " aric", "Alex", "Tony", "rain")
# dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}

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

# li = ['alex', 'eric', 'rain']
# li.remove("eric")
#
# li = ['alex', 'eric', 'rain']
# print(len(li))
# li.append("seven")
# li.insert(1, "Tony")
# li[2] = "Kelly"
# print(li)
#
# print(li.pop(2))
# li.append("seven")
# print(li)
# # del li[2:5]
# li.reverse()
# print(li)
#
# for i in range(len(li)):
#     print(i)
# print(li)
# for i, v in enumerate(li, 100):
#     print("%s.%s" % (i, v))
# for i in li:
#     print(i)
# li = ["hello", 'seven', ["mon", ["h", "kelly"], 'all'], 123, 446]
#
# print(li[2][1][1])
#
# li[2][2] = "ALL"
# print(li)
#
# tu = ('alex', 'eric', 'rain')
# print(len(tu))
#
# print(tu[2])
#
# print(tu[:2])
#
# for i in tu:
#     print(i)
#
# for i in range(len(tu)):
#     print(i)
#
# for i, v in enumerate(tu, 10):
#     print("%s.%s" % (i, v))

# tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])
# # 元组不可变
# # 不能
# tu[1][2]["k2"].append("Seven")
# print(tu)
# # 不能

# dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
#
# for i in dic.keys():
#     print(i)
# for i in dic.values():
#     print(i)
# dic["k4"] = "v4"
# print(dic)
#
# dic["k1"] = "alex"
# print(dic)
# dic["k3"].append(44)
# print(dic)
#
# dic["k3"].insert(1, 18)
# print(dic)

# s = "alex"
# print(list("%s" % (s,)))
# print(tuple(s))
# li = ["alex", "seven"]
# dic = {}
# for i,v in enumerate(li, 10):
#     dic[i] = v
# print(dic)

# s1 = [11,22,33,44,55,66,77,88,99,90]
# dic = {
#     "k1": [],
#     "k2": []
# }
# for i in s1:
#     if i > 66:
#         dic["k1"].append(i)
#     else:
#         dic["k2"].append(i)
# print(dic)

# li = ["自行车", "书", '美女', '电脑']
#
# while True:
#     print("------info------")
#     for i, v in enumerate(li, 0):
#         print("%s.%s" % (i, v))
#     choice = input(">>>:")
#     if choice.isdigit():
#         print(li[int(choice)])
#     else:
#         li.append(choice)






