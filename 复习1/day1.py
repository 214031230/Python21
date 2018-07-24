#!/usr/bin/env python3
# i = 4
# print(i.bit_length())
# s = "python自动化运维21期"
# print(s[0])
# print(s[0::2])
# print(s[-1:-5:-1])
# print(s.capitalize())
# print(s.center(50))
# print(s.count("p"))


# age = 20
# while 1:
#     try:
#         num = int(input(">>>:"))
#         if num > 20:
#             print("大了")
#         elif num < 20:
#             print("小了")
#         else:
#             print("猜对了")
#             break
#     except ValueError:
#         print("你输入的不是数字！")


# for i in range(1, 101):
#     print(i)

# for i in range(1, 101):
#     if i % 2 == 1:
#         print(i)
# sums = 0
# for i in range(1, 101):
#     # if i % 2 == 1:
#     sums += i
# print(sums)
# count = 1
# while count < 100:
#     print(count)
#     if count == 10:
#         break
#     count += 1
# else:
#     print("循环没有被break")


# print(3 > 4 or 4 < 3 and 1 == 1)
# # F
# print(1 < 2 and 3 < 4 or 1 > 2)
# # T
# print(2 > 1 and 3 < 4 or 4 > 5 and 2 < 1)
# # T
# print(1 > 2 and 3 < 4 or 4 > 5 and 2 > 1 or 9 < 8)
# # F
# print(1 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)
# # F
# print(not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)
# # F
# # 在没有括号的情况下优先级别not > and > or

# print(5 or 6)
# print(0 or 6)
# x or y if x=True return x else return y
# x and y if x = T return y else return x

# 10
# 20
# 128 64 32 16 8 4 2 1
#  0  0  0  0  1 0 1 0
# #  0  0  0  1  0 1 0 0
# print(chr(10))

# print(ord("Z"))

# 求1-2+3-4+5 ... 99的所有数的和

# sums = 0
# for i in range(1, 100):
#     if i % 2 == 0:
#         sums -= i
#     else:
#         sums += i
# print(sums)


"""
功能描述：
1、用户登陆，三次机会重试。
2、可以支持多用户登录
3、用户输入了三次机会，都没成功，给它一个选择，让它在试试(必须是同一个用户输入3次错误)
如果用户选择继续则再给他三次机会；如果选择退出则退出程序并打印 print('臭不要脸.....')
4、使用列表+字典存用户名和密码
"""

# max_count = 0
# user_info = {"spf": "123", "wxx": "456"}
# while max_count < 3:
#     username = input("User:")
#     password = input("Password:")
#     if username in user_info:
#         if password == user_info[username]:
#             print("INFO:登录成功！")
#             break
#         else:
#             print("用户名或者密码错误")
#     else:
#         print("Error:用户不存在!")
#     if max_count == 2:
#         print("Error:3次机会已经用完")
#         choice = input("是否继续尝试？Y/N:")
#         if choice.upper() == "Y":
#             max_count = -1
#         elif choice.upper() == "N":
#             max_count = 2
#         else:
#             print("请输入正确的指令")
#     max_count += 1
