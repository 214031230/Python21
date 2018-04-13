#!/usr/bin/env python3
# 三级菜单
# data = {
#     '北京': {
#         '海淀': {
#             '五道口': {
#                 'soho': {},
#                 '网易': {},
#                 'Google': {}
#             },
#             '中关村': {
#                 '爱奇艺': {},
#                 '汽车之家': {},
#                 'youku': {},
#             },
#             '上地': {
#                 '百度': {},
#             }
#         },
#         '昌平': {
#             '沙河': {
#                 '老男孩': {},
#                 '北航': {}
#             },
#             '天通苑': {},
#             '回龙观': {}
#         },
#         '朝阳': {},
#         '东城': {}
#     },
#     '上海': {},
#     '湖北': {},
#     '广东': {}
# }
#
# current_layer = data
# last_layer = []
# while True:
#     for k in current_layer:
#         print(k)
#     choice = input(">>>:")
#     if not choice:continue
#     if choice in current_layer:
#         last_layer.append(current_layer) # 进入下一层之前保存当前层
#         current_layer = current_layer[choice] # 进入下一层
#     if choice == "b":
#         current_layer = last_layer.pop() # 返回上一层，并删除上一层记录


# li = ['alex', 'eric', 'rain']
#
# print(len(li))
#
# li.append("seven")
#
# li.insert(1, "Tony")
#
# # li.pop(1)
#
# li[1] = "Kelly"
#
# # li.remove("eric")
#
# # li.pop(1)
#
# print(li)

# del li[2]

# del li[1:5]

# print(li)

# li.reverse()
# print(li)

# for i in range(len(li)):
#     print(i, li[i])
# for i, v in enumerate(li, 100):
#     print(i, v)

# for k in li:
#     print(k)


# li = ["hello", 'seven', ["mon", ["h", "kelly"], 'all'], 123, 446]
#
# print(li[2][1][1])
#
# li[2][2] = li[2][2].upper()
#
# print(li)


# tu = ('alex', 'eric', 'rain')
# print(len(tu))
#
# print(tu[1])
#
# print(tu[1:3])
#
# for i in tu:
#     print(i)
#
# for i in range(len(tu)):
#     print(i, tu[i])
#
# for i, v in enumerate(tu, 100):
#     print(i, v)
#
# tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])
#
# #
# tu[1][2]["k2"].append("Seven")
# print(tu)

# # 　　2、求1-100的所有数的和
# sum = 0
# for i in range(1,101):
#     sum = sum + i
# print(sum)
#
# # 　　3、输出 1-100 内的所有奇数
# for i in range(1,101):
#     if i % 2 == 1:
#         print(i)
#
# # 　　4、输出 1-100 内的所有偶数
# for i in range(1,101):
#     if i % 2 == 0:
#         print(i)
#
# # 　　5、求1-2+3-4+5 ... 99的所有数的和
#
# sum = 0
# for i in range(1,100):
#     if i % 2 == 1:
#         sum += i
#     else:
#         sum -= i
# print(sum)
# li = list(range(1,101))
# print(li[::2])
# print(li[1::2])
# print(li[-1::-1])

# li = ["alex", "spf", "wxx"]
# s = "_".join(li)
# print(s)

# a = 123
# b = a
# a = 456
# print(b)


# l1 = [1, 2, 3]
#
# l2 = l1.copy()
#
# l1.append(4)
# print(l2)

# import  copy
# l1 = [1, [1, 2], 3]
# l2 = copy.deepcopy(l1)
#
# l1[1].append(3)
# print(l2)

# a = " 123 "
# b = a.split()
# c = a.strip().split(" ")
# d = a.split("2")
# print(b)
# print(c)
# print(d)

data = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'Google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            }
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {}
            },
            '天通苑': {},
            '回龙观': {}
        },
        '朝阳': {},
        '东城': {}
    },
    '上海': {},
    '湖北': {},
    '广东': {}
}
f1 = data
f2 = []
f2 [data,data[choice]]
while True:
    for k in f1: # f1["北京"]  # f1["北京"]["昌平"]
        print(k)
    choice = input(">:").strip()
    if not choice:continue
    if choice in f1:
        # 保存当前层
        f2.append(f1) # f1 = data  #  f1  = f1["北京"]
        print(f2)
        f1 = f1[choice] # 进入下一层 f1[choice] = f1["北京"]  f1["北京"]  = f1["北京"]["昌平"]
    elif choice == "b":
        f1 = f2.pop()
    else:
        print("节点不存在！")