#!/usr/bin/env python3
# 判断下列逻辑语句的True,False.
# 1）1 > 1 or 3 < 4  or    4 >5 and 2 > 1 and 9 > 8     or 7 < 6
# False

# 2）not 2 > 1  and 3 < 4    or     4 > 5 and 2 > 1 and 9 > 8    or    7 < 6
# False

# 2、求出下列逻辑语句的值。
# 1),8 or   3 and 4  or   2 and 0   or   9 and 7
# 8 or 4 or 0 or 9
# 8 or 0 or 9
# 8 or 9
# 8
# print(8 or   3 and 4  or   2 and 0   or   9 and 7)
#
# # 2),0 or 2 and 3 and 4 or 6 and 0    or 3
# # 0 or  4 or 0   or 3
# 4


# # 3、下列结果是什么？
# # 1)、6 or 2 > 1
# print(6 or 2 > 1)
#
# # 2)、3 or 2 > 1
# print(3 or 2 > 1)
#
# # 3)、0 or 5 < 4
# print(0 or 5 < 4)
#
# # 4)、5 < 4 or 3
# print(5 < 4 or 3)
#
# # 5)、2 > 1 or 6
# print(2 > 1 or 6)
#
# #  x or y ,if x = True  ,return  x
#
# # 6)、3 and 2 > 1
# print(3 and 2 > 1)
#
# # 7)、0 and 3 > 1
# print(0 and 3 > 1)
#
# # 8)、2 > 1 and 3
# print(2 > 1 and 3)
#
# # 9)、3 > 1 and 0
# print(3 > 1 and 0)

# 10)、3 > 1 and 2  or  2 < 3 and 3 and 4  or 3 > 2
# 3 > 2  or  2 < 4  or 3 > 2


# 4. 简述变量命名规范
# 不能以数字或者特殊符号开头
# 不能用内置函数当变量
# 变量名具有可读性
# 变量不能使用中文
# 变量不能过长

# 5. name = input(“>>>”) name变量是什么数据类型？
# 字符窜

# # 6. if条件语句的基本结构？
# if "条件":
#     pass
# elif "条件":
#     pass
# else:
#     pass
# # 7. while循环语句基本结构？
# while True:
#     pass
#
# while True:
#     pass
# else:
#     pass
# 8. 写代码：计算 1 - 2 + 3 ... + 99 中除了88以外所有数的总和？
# sums = 0
# count = 1
# while count < 100:
#     if count % 2 == 1:
#         sums = sums + count
#     else:
#         if count == 88:
#             pass
#         else:
#             sums = sums - count
#     count += 1
# print(sums)
#
#
# # 9. ⽤户登陆（三次输错机会）且每次输错误时显示剩余错误次数（提示：使⽤字符串格式化）
#
# count = 1
# while count <= 3:
#     name = input(">>>:")
#     if name == "spf":
#         print("OK")
#     else:
#         print("失败，剩余%d次" % (3 - count))
#     count += 1
# # 10. 简述ascii、unicode、utf-8编码关系？
#

# 11. 简述位和字节的关系？
# 8位 = 1bytes
# 12. “⽼男孩”使⽤UTF-8编码占⽤⼏个字节？使⽤GBK编码占⼏个字节？
#  3个字节  2个字节
# 13. 制作趣味模板程序需求：等待⽤户输⼊名字、地点、爱好，根据⽤户的名字和爱好进⾏任意现实 如：敬爱可亲的xxx，最喜欢在xxx地⽅⼲xxx
# name = input("name:")
# add = input("add:")
# happy = input("happy:")
#
# print("""
# 敬爱可亲的%s，最喜欢在%s⼲%s
# """ % (name, add, happy))

# 14. 等待⽤户输⼊内容，检测⽤户输⼊内容中是否包含敏感字符？如果存在敏感字符提示“存在敏感字符请重新输⼊”，并允许⽤户重新输⼊并打印。敏感字符：“⼩粉嫩”、“⼤铁锤”

# error = ["小粉嫩", "大铁锤"]
# while True:
#     name = input(">").strip()
#     if name in error:
#         print("输入包含敏感字符，请重新输入")
#     else:
#         print("ok")
# 15. 单⾏注释以及多⾏注释？
#
"""
"""
# 16. 简述你所知道的Python3和Python2的区别？
#  编码不同  python2采用acsii  python3 采用 utf-8
#  input 区别
#
# 17. 看代码书写结果：
a = 1>2 or 4<7 and 8 == 8
# a = f or t
# print(a)
#
# 18.continue和break区别？
#
# Day3默写代码：
# Bit,Bytes,Kb,Mb,Gb,Tb之间的转换关系。
# Unicode，utf-8，gbk，每个编码英文，中文，分别用几个字节表示。
