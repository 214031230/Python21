#!/usr/bin/env python3

# 递归函数之二分查找算法,有序的数字集合的查找问题
# 生成一个测试列表
# res = [i for i in range(50) if i % 2 == 0 ]
# print(res)

# lst = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
# def func(lst,num,start=0,end=None):
#     end = len(lst) - 1 if end is None else end  # is 和 ==
#     if start > end: return None
#     mid = (end - start) // 2 + start
#     if lst[mid] > num:
#         return func(lst, num, start, mid - 1)
#     elif lst[mid] < num:
#         return func(lst, num, mid + 1, end)
#     else:
#         return mid
#
# print(func(lst,2))

# 解析
# def func(lst,2,start=0,end=None):
#     end = 24
#     if 0 > 24: return None
#     mid = 12
#     if lst[12] > 0:
#         return func(lst, 2, 0, 11)  #
#
# def func(lst,2,start=0,end=11):
#     end = 11
#     if 0 > 11: return None
#     mid = 5
#     if lst[5] > num:
#         return func(lst, 2, 0, 4)
#
# def func(lst,2,start=0,end=4):
#     end = 4
#     if 0 > 4: return None
#     mid = 2
#     if lst[2] > num:
#         return func(lst, 2, 0, 1)
#
# def func(lst,2,start=0,end=1):
#     end = 1
#     if 0 > 1: return None
#     mid = 0
#     if lst[mid] > num:
#         return func(lst, num, start, mid - 1)
#     elif lst[0] < 2:
#         return func(lst, 2, 1, 1)
#     else:
#         return mid
#
# def func(lst,2,start=1,end=1):
#     end = 1
#     if 0 > 1: return None
#     mid = 1
#     if lst[mid] > num:
#         return func(lst, num, start, mid - 1)
#     elif lst[mid] < num:
#         return func(lst, num, mid + 1, end)
#     else:
#         return 1   # 匹配成功

# 三级菜单
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
# 堆栈实现
# current_layer = menu  # 当前层
# last_layer = []  # 上一层
# while True:
#     for k in current_layer:print(k)
#     choice = input(">>>:").strip()
#     if not choice:continue
#     if choice in current_layer:
#         last_layer.append(current_layer)
#         current_layer = current_layer[choice]
#     elif choice.lower() == "b":
#         if len(last_layer) == 0:
#             print("ERROR：已经到顶层")
#             continue
#         current_layer = last_layer.pop()
#     elif choice.lower() == "q":
#         break
#     else:
#         print("ERROR：节点不存在")
# 递归实现
# def func(dic):
#     while True:
#         for k in dic:
#             print(k)
#         choice = input(">>>:").strip()
#         if not choice:continue
#         # 当choice等于b的时候结束当前递归对应次数的函数
#         if choice.lower() == "b":return
#         # 当choice等于q的时候返回一个q进行判断。
#         if choice.lower() == "q":return "q"
#         if choice in dic:
#             res = func(dic[choice])
#             # 如果返回值为q，则回溯到函数结束
#             if res == "q":return "q"
#         else: print("ERROR:节点不存在")
# func(menu)

# 计算年龄
# def age(n):
#     if n == 1:return 30
#     return age(n - 1) + 2
#
# print(age(3))  #  34

# 解析
# def age(3):
#     if 3 == 1:return 30
#     return age(2) + 2  #  return 32 + 2

# def age(2):
#     if 2 == 1:return 30
#     return age(1) + 2  #  return 30 + 2

# def age(1):
#     if 1 == 1:return 30
