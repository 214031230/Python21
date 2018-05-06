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
#     if start > end:
#         return None
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
















































