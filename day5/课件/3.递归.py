#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 递归 —— 在函数的内部调用自己
# 递归的最大深度 : 998
# 小例子：
# 猜年龄
# alex多大了     alex 比 wusir 大两岁  40+2+2
# wusir多大了    wusir 比 金老板大两岁   40+2
# 金老板多大了   40了
# age(1)
# n = 1 age(2)+2
# n = 2 age(3)+2
# n = 3 age(3) = 40

# def age(n):
#     if n == 3:
#         return 40
#     else:
#         return age(n+1)+2
#
# print(age(1))

# # n = 1
# def age(1):
#     if 1 == 3:
#         return 40
#     else:
#         return age(2)+2
#
# # n = 2
# def age(2):
#     if 2 == 3:
#         return 40
#     else:
#         return age(3)+2
#
# # n = 3
# def age(3):
#     if 3 == 3:
#         return 40

# 递归求解二分查找算法
# 算法
# 99*99 = 99*(100-1) = 9900-99 = 9801
# 人类的算法
# 99 * 99

# 算法 计算一些比较复杂的问题
    # 所采用的 在空间上（内存里） 或者时间上（执行时间） 更有优势的方法
# 排序 500000万个数 快速排序 堆排序 冒泡排序
# 查找

# 递归求解二分查找算法 : 有序的数字集合的查找问题
# l = [2,3,5,10,15,16,18,22,26,30,32,35,41,42,43,55,56,66,67,69,72,76,82,83,88]
# # 列表不能变
# def cal(l,num,start,end):
#     mid = (end - start)//2 + start
#     if l[mid] > num :
#         cal(l, num, start, mid-1)
#     elif l[mid] < num:      # 13  24
#         cal(l,num,mid+1,end)
#     else:
#         print('找到了',mid,l[mid])
#
# cal(l,60,0,len(l)-1)
# #
# # def cal(l,num=66):
# #     length = len(l)
# #     mid = length//2
# #     if num > l[mid]:
# #         l = l[mid+1:]
# #         cal(l,num)
# #     elif num < l[mid]:
# #         l = l[:mid]
# #         cal(l, num)
# #     else:
# #         print('找到了',l[mid],mid)
# # cal(l,66)
#
# l = [2,3,5,10,15,16,18,22,26,30,32,35,41,42,43,55,56,66,67,69,72,76,82,83,88]
# def cal(l,66,0,24):
#     mid = 12 + 0
#     if 41 > 66 :
#         cal(l, num, start, mid-1)
#     elif 41 < 66:      # 13  24
#         cal(l,66,13,24)
#     else:
#         print('找到了',mid,l[mid])
#
# l = [2,3,5,10,15,16,18,22,26,30,32,35,41,42,43,55,56,66,67,69,72,76,82,83,88]
# def cal(l,66,13,24):
#     mid = 5 + 13
#     if 67 > 66 :
#         cal(l, 66, 13, 17)
#     elif l[mid] < num:      # 13  24
#         cal(l,num,mid+1,end)
#     else:
#         print('找到了',mid,l[mid])
#
# l = [2,3,5,10,15,16,18,22,26,30,32,35,41,42,43,55,56,66,67,69,72,76,82,83,88]
# def cal(l,66,13,17):
#     mid = 2 + 13
#     if 55 > 66 :
#         cal(l, num, start, mid-1)
#     elif 55 < 66:
#         cal(l,66,16,17)
#     else:
#         print('找到了',mid,l[mid])
#
# l = [2,3,5,10,15,16,18,22,26,30,32,35,41,42,43,55,56,66,67,69,72,76,82,83,88]
# def cal(l,60,16,17):
#     mid =0 + 16
#     if 56 > 60 :
#         cal(l, num, start, mid-1)
#     elif 56 < 60:      # 13  24
#         cal(l,60,17,17)   #None
#     else:
#         print('找到了',mid,l[mid])
# #
# # l = [2,3,5,10,15,16,18,22,26,30,32,35,41,42,43,55,56,66,67,69,72,76,82,83,88]
# def cal(l,60,17,17):
#     mid = 0 + 17
#     if 60 > 66 :
#         cal(l, num, start, mid-1)
#     elif 60 < 66:      # 13  24
#         return cal(l,60,18,17)
#     else:
#         print('找到了',17,66)
#
# def cal(l, 60, 18, 17):
#     if start <end:
#         mid = 0+18
#         if 67 > 66:
#             cal(l, 60, 18,17)
#         elif 60 < 66:  # 13  24
#             cal(l, 60, 18, 17)
#         else:
#             print('找到了', 17, 66)
#     else:
#         print('没找到')


# 算法
# def cal(l,num,start=0,end=None):
#     # if end is None:end = len(l)-1
#     end = len(l)-1 if end is None else end
#     if start <= end:
#         mid = (end - start)//2 + start
#         if l[mid] > num :
#             return cal(l, num, start, mid-1)
#         elif l[mid] < num:      # 13  24
#             return cal(l,num,mid+1,end)
#         else:
#             return mid
#     else:
#         return None
# l = [2,3,5,10,15,16,18,22,26,30,32,35,41,42,43,55,56,66,67,69,72,76,82,83,88]
# print(cal(l,56))

# 参数太多       -------- ???
# 找的数不存在   ———— 解决了
# print   return  ------- 解决

# 三级菜单

# 视频
# 作业(计算器)(SQL模拟器)（博客园 员工信息表）
# 三级菜单的递归的讲解
# 递归的练习题

# 算法 —— 递归



