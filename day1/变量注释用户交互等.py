#!/usr/bin/env python3
# 格式化输出 方法1
# name = input("请输入用户名：")
# age = int(input("请输入年龄："))
# job = input("请输入工作：")
# hap = input("请输入爱好：")
# meg = """
#     info
#     姓名：%s
#     年龄：%d
#     工作：%s
#     爱好：%s
# """ % (name, age, job, hap)
# print(meg)

# 格式化输出 方法2
# dic = {"name": "XX", "age": 30, "job": "it", "hap": "IT"}
# meg = """
#     info
#     姓名：%(name)s
#     年龄：%(age)d
#     工作：%(job)s
#     爱好：%(hap)s
# """ % dic
# print(meg)

# # 打印1到100，方法1
# i = 0
# while True:
#     print(i+1)
#     i += 1
#     if i == 100:
#         break
# # 打印1到100，方法2
# i = 0
# while i <= 100:
#     print(i)
#     i += 1
#
# # 打印1到100，方法3
# for i in range(1, 101):
#     print(i)

# 从1加到100
# count = 1
# res = 0
# while count < 101:
#     res = res + count
#     count += 1
# print(res)

# 128 64 32 16 8 4 2 1


count = 1
while count <= 100:
    print(count)
    if count == 5:
        continue
    count += 1
