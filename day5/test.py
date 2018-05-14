#!/usr/bin/env python3
# def func(n):
#     if n == 3:
#         return n
#     else:
#         return func(n+1) + 2
#
# func(10)


# lst = []
# for i in range(100):
#     if i % 2 == 0:
#         lst.append(i)
# print(lst)


#  二分之一算法
# lst = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
# def func(lst,num,start=0,end=None):
#     end =len(lst) - 1 if end is None else end
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
#
# #  解析
# lst = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
# def func(lst,2,start=0,end=None):
#     end =len(lst) - 1 if end is None else end  # end = 49
#     print(end)
#     if 0 > 49:
#         return None
#     mid = (49 - 0) // 2 + 0  # mid = 24
#     if lst[24] > 2:
#         return func(lst, 2, 0, 23)
#
# lst = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
# def func(lst,2,0,24):
#     end =len(lst) - 1 if end is None else end  # end = 23
#     print(end)
#     if 0 > 23:
#         return None
#     mid = (23 - 0) // 2 + 0  # mid = 11
#     if lst[11] > 2:
#         return func(lst, 2, 0, 10)
#
# lst = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
# def func(lst,2,0,10):
#     end =len(lst) - 1 if end is None else end  # end = 10
#     print(end)
#     if 0 > 10:
#         return None
#     mid = (12 - 0) // 2 + 0  # mid = 5
#     if lst[6] > 2:
#         return func(lst, 2, 0, 4)
#
# lst = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
# def func(lst,2,0,4):
#     end =len(lst) - 1 if end is None else end  # end = 4
#     print(end)
#     if 0 > 4:
#         return None
#     mid = (4 - 0) // 2 + 0  # mid = 2
#     if lst[2] > 2:
#         return func(lst, 2, 0, 1)
#
# lst = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
# def func(lst,2,0,1):
#     end =len(lst) - 1 if end is None else end  # end = 1
#     print(end)
#     if 0 > 1:
#         return None
#     mid = (1 - 0) // 2 + 0  # mid = 0
#     elif lst[0] < 2:
#         return func(lst, 2, 1, 1)
#     else:
#         return mid

# lst = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
# def func(lst,2,1,1):
#     end =len(lst) - 1 if end is None else end  # end = 1
#     print(end)
#     if 1 > 1:
#         return None
#     mid = (1 - 0) // 2 + 1  # mid = 1
#     if lst[1] > 2:
#         return func(lst, 2, 0, 4)
#     elif lst[1] < 2:
#         return func(lst, 2, mid + 1, 1)
#     else:
#         return mid



# 练习题1： 计算目录大小
import os
sum_size = 0
def func(dirs):
    global sum_size
    if not os.path.exists(dirs):return "ERROR：路径不存在"
    dirs_list = os.listdir(dirs)
    for i in dirs_list:
        if os.path.isdir(os.path.join(dirs, i)):
            return func(os.path.join(dirs, i))
        else:
            sum_size += os.path.getsize(os.path.join(dirs, i))
    return "目录大小：%sbyte" % sum_size
print(func(r"..\day5\test"))


# 练习题2：计算时间差
import time
def func1(last_year):
    last_stamp = time.strptime(last_year, "%Y-%m-%d")
    curr_stamp = time.gmtime()
    stamp_time = time.mktime(curr_stamp) - time.mktime(last_stamp)
    curr_struct = time.gmtime(stamp_time)
    print("距离今天%s年%s月%s天" % (curr_struct.tm_year-1970, curr_struct.tm_mon-1, curr_struct.tm_mday - 1))
func1("1992-08-17")


# 练习题3：三级菜单
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
# 堆栈版
def func2():
    current_layer = []
    last_layer = menu
    while True:
        for k in last_layer:
            print(k)
        choice = input(">>>:").strip()
        if not choice:continue
        if choice in last_layer:
            current_layer.append(last_layer)
            last_layer = last_layer[choice]
        elif choice == "b":
            if len(current_layer) == 0:
                continue
            last_layer = current_layer.pop()
        elif choice == "q":
            break
        else:
            print("节点不存在！")
# func2()
# 递归版
def func3(dic):
    while True:
        for i in dic:
            print(i)
        choice = input(">>>:")
        if not choice:continue
        if choice == "b":return
        if choice == "q":return "q"
        if choice in dic:
             ret = func3(dic[choice])
             if ret == "q":return "q"
        else:
            print("节点不存在！")
# func3(menu)

# 练习题4：验证码
import random
def func4(num):
    s = ""
    for i in range(num):
        char = random.choice([random.randint(0, 9), chr(random.randint(65, 90)), chr(random.randint(97, 122))])
        s += str(char)
    return s
# print(func4(5))

























