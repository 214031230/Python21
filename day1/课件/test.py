#!/usr/bin/env python3
# 逻辑运算符  在没有（）的情况下 优先级别  not > and > or
# print(2 > 1 and 3 < 4 or 4 > 5 and 2 < 1) # True
# print(1 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6) # False
#
# # x or y , if x = True , return x
# print(3 or 2)
# print(0 or 1)
#
# # x and y , if x = True , return y
# print(0 and 1)

'''
1、使用while循环输入 1 2 3 4 5 6 8 9 10

2、求1-100的所有数的和

3、输出 1-100 内的所有奇数

4、输出 1-100 内的所有偶数

5、求1-2+3-4+5 ... 99的所有数的和


'''
# count = 1
# while count <= 10:
#     print(count)
#     count += 1 # count = count +1
#
#
# count = 1
# sums = 0
# while count <= 100:
#     sums += count
#     count += 1 # count = count +1
# print(sums)

# count = 1
# while count <= 100:
#     if count % 2 == 0:
#         print(count)
#     count += 1 # count = count +1

# count = 1
# sums = 0
# while count <= 100:
#     # 0 + 1 - 2 + 3 - 4
#     if count % 2 == 1:
#         sums += count
#     if count % 2 == 0:
#         sums -= count
#     count += 1 # count = count +1
#     print(sums)



