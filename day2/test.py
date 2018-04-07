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


# s = 'python自动化运维21期'
# s1 = s[0]
# print(s1)
# s2 = s[:3]
# print(s2)
# s3 = s[:]
# print(s3)
# s4 = s[::2]
# print(s4)
# s5 = s[-1:-4:-1]
# print(s5)

# list
# li = ["alex", "老男孩", "光头", "wusir"]
# # 增
# li.append("孙鹏飞")
# li.insert(1, "spf")
# li.extend([1,2,3])
# print(li)

# # 删
# # 按索引删,有返回值
# li.pop(1)
# # 按元素删
# li.remove("孙鹏飞")
# # 按切片删
# del li[:2]
# print(li)

# # 改
# li[0] = "孙鹏飞"
# li[4:] = [1, 2, 3, 4]
# print(li)

# # 查
# print(li[0])
# print(li[:3])
# print(li.index(4))

# 其他
# li = [4,1,2,3]
# # print(len(li))
# # print(li.count(2))
# li.sort()
# print(li)
# li.reverse()
# print(li)
#
# l1 = [1, 2, 'alex', 'wusir',['oldboy', 'ritian', 99], 'taibai']
# l1[2] = l1[2].upper()
# print(l1)
# li = [3,5,2,2,1]
# li.sort()
# print(li)

# str操作
# s = "sunpengFei"
# s1 = s.upper()
# s2 = s.capitalize()
# s3 = s.lower()
# s4 = s.index("u")
# s5 = s.count("n")
# s6 = s.isdigit()
# s7 = s.strip()
# s8 = s.strip("si")
# s9 = s.startswith("sun")
# s10 = s.split()
# s2 = list(s)
# s11 = s.center(30, "*")
# s12 = s.find("n")
# s = "{0} {1} {2}"
# s13 = s.format("name", "age", "hoppy")
# s14 = s.replace("n", "WWW")
# print(s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s2, s11)
# print(s12, s13, s14)
# print(s14)
# print(len(s))

# dict
# dic = {'name': 'taibai', 'age': 21, 'hobby': 'girl', }
# # 增
# dic["high"] = 180
# dic.setdefault("job", "IT")
# dic.setdefault("job", "IT")
# print(dic)

# # 删
# dic.pop("name") # 有返回值
# dic.popitem() # 随机删除 有返回值
# del dic["name"]

# 改
# dic["name"] = "spf"
# print(dic)
# dic2 = {"name": "spf", "Job": "IT"}
# dic2.update(dic)
# print(dic2)

# # 查
# print(dic.get("name"))
# print(dic.items())
# print(dic.get("name1",)) # 返回值为None ,可以修改返回值
# print(dic.get("name1", "没有此键"))
#
# dic3 = dict.fromkeys([1, 2, 3], "spf")
# print(dic3)
#
#
# for k, v in dic.items():
#     print(k, v)


# dic = {
#     'name_list': ['b哥', '张帝', '人帅', 'kitty'],
#     '老男孩': {
#         'name': '老男孩',
#         'age': 46,
#         'sex': 'ladyboy',
#     },
# }
# # 1,['b哥', '张帝', '人帅', 'kitty']追加一个元素，'骑兵'
# dic["name_list"].append("骑兵")
# print(dic)
# # 2，将kitty全部变成大写。
# dic["name_list"][3] = dic["name_list"][3].upper()
# print(dic)
# # 3，将老男孩 改成oldboy。
# dic["老男孩"]["name"] = "oldboy"
# print(dic)
# # 4，将ladyboy首字母大写。
# dic["老男孩"]["sex"] = dic["老男孩"]["sex"].capitalize()
# print(dic)


# l1 = ['alex', 'wusir', 'taibai', 'barry', '老男孩']
#
# del l1[::2]
#
# dic = {'k1':'v1','k2':'v2','k3':'v3',"4":666}
#
# for i in dic.keys():
#     # print(type(i))
#     if i.isalnum():
#         if i.startswith("k"):
#             print(i)
#             dic.pop(i)
# print(dic)
