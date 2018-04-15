#!/usr/bin/env python3
# # int
# num = 50
# # 0 0 0 0 0 0 0 0
# # 0 0 32 16 8 4 2 1
# #  bit_length 获取数字的二进制长度
# print(num.bit_length())
#
# # str  字符串方法都是赋值给一个新的字符串，而不是在原有字符串进行操作，因为str是可哈希的
# s = "old_boy"
# # capitalize首字母大写
# s1 = s.capitalize()
# print(s1)
#
# # casefold() 方法是Python3.3版本之后引入的，其效果和 lower() 方法非常相似，都可以转换字符串中所有大写字符为小写。
# # 两者的区别是：lower() 方法只对ASCII编码，也就是‘A-Z’有效，对于其他语言（非汉语或英文）中把大写转换为小写的情况只能用 casefold() 方法。
# s = "OLD_boy"
# s2 = s.casefold()
# print(s2)
#
# # 居中，可以设置长度默认补全为None
# s3 = s.center(30, "-")
# print(s3)
#
# # 统计相同元素的个数
# print(s.count("o"))
#
# # 转换成指定的编码格式
# s = "老男孩_old_boy"
# print(s)
# s4 = s.encode("utf-8")
# print(s4)
#
# # 判断字符串是否以指定字符结尾，返回True或False
# print(s.endswith("孩"))
#
# # 查找元素，返回索引，如果没有找到则返回-1，可以切片查找，切片是顾头不顾尾
# print(s.find("男"))
# print(s.find("0"))
# print(s.find("l", 2, 5))
#
# # 格式化输出
# print("{0}{1}{1}".format(1, 2, 3))
# print("{name}{age}{job}".format(name="spf", age=18, job="IT"))
#
# # 查找元素返回索引，如果元素不存在则报错，可以切片查找
# print(s.index("o"))
# print(s.index("o", 5))
#
# # 是否为字母或者数字
# s = "aaa1123"
# print(s.isalnum())
#
# s = "123"
# # 是否为数字
# print(s.isdigit())
#
# s = "avc"
# # 是否为字母
# print(s.isalpha())

# 主要用于将列表转成字符串
# li = ["1", "2", "3"]
# s = "_".join(li)
# print(s)
#
# # 右边补充
# s = "olD_boY"
# s1 = s.ljust(10, "#")
# print(s1)
#
# # 全部变小写
# print(s.lower())
#
# # 全部变大写
# print(s.upper())
#
# # 去掉左边的空格
# s = " old  boy  "
# print(s.lstrip())
#
# # 去掉两边的空格
# print(s.strip())
#
# # replace 替换字符串，可以知道替换的个数
# print(s.replace("old", "new"))
#
# # 切割返回列表
# s = "alex  spf  wxx"
# print(s.split())
# s = "alex,spf,wxx"
# print(s.split(","))
# s = """
# 1
# 2
# 3
# 5
# """
# print(s.splitlines())
#
# # 字符串是否以指定字符开始，返回True或False
# print(s.startswith("\n"))
#
# # 大小写翻转
# s = "aBcD"
# print(s.swapcase())
#
# # #
# s = "spf#wxx#alex"
# # print(s.title())
#
# #
# print(s.zfill(100))

# bool
# print(bool(0))

# # list
# list
# # 追加元素
# a = ["spf", "wxx", "sxx"]
# a.append("wpf")
# print(a)
#
# # 在指定索引位置加入元素
# a.insert(1, "WWW")
# print(a)
#
# # 迭代追加，可同时增加多个元素
# a.extend([1, 2, 3])
# print(a)
#
# # 根据索引删元素
# a.pop(2)
# print(a)
#
# # 根据元素删除
# a.remove("wpf")
# print(a)
#
# # 清空列表
# a.clear()
# print(a)
#
# # 统计相同元素个数
# l = [1,2,3,1,2,3]
# print(l.count(1))
#
# # 翻转列表
# l.reverse()
# print(l)
#
# # 排序
# l.sort()
# print(l)
#
#
# a = ["spf", "wxx", "sxx"]
#
# #
# del a[0]
# del a
# print(a)

# # tuple
# t = (1,2,3,4)
# print(t[0])
# print(t.index(3))
# print(t.count(1))
#
# # dict
# dic = {"name": "spf",
#        "age": 18,
#        "job": "SA"
#        }
# # 获取key对应的value，如果key不存在返回None,可以指定返回值
# print(dic.get("name1"))
# print(dic.get("name1", "没有key"))
#
# # 以元组的方式返回key和value
# print(dic.items())
#
# # 获取所有的key
# print(dic.keys())
#
# # 获取所有的value
# print(dic.values())
#
# # 删除key，并返回删除的value
# print(dic.pop("name"))
#
# # 随机删除
# dic.popitem()
# print(dic)
#
# # 增加
# dic["happy"] = "美女"
# print(dic)
#
# # setdefault 和 dic["happy"] 区别   前者无则增加，有则不变。后者有则覆盖，无则增加
# dic.setdefault("add", "北京")
# dic.setdefault("add", "河南")
# print(dic)
#
# dic1 = {"k1": "v1", "k2": "v2"}
# dic2 = {"k1": "v2", "k3": "v3"}
# # {"k1": "v1", "k2": "v2", "k3": "v3"}
#
# dic2.update(dic1)
# print(dic2)


# # 集合
#
# s1 = {1,2,3}
# s2 = {2,3,4}
# # 并集
# print(s1 | s2)
# # 差集合
# print(s1 - s2)
# # 交集
# print(s1 & s2)
# # 反交集
# print(s1 ^ s2)
# # 超集
# print(s1 > s2)
# # 子集
# print(s1 < s2)



#  计算 1+2+3 +100的和
#
# sum = 0
# for i in range(101):
#     sum += i # sum = sum + i
# print(sum)
#
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
#
# while True:
#     for k in current_layer:
#         print(k)
#     choice = input(">:")
#     if not choice:continue
#     if choice in current_layer:
#         last_layer.append(current_layer)
#         current_layer = current_layer[choice]
#     elif choice == "b":
#         if len(last_layer) == 0:
#             print("已经到最顶层！")
#             continue
#         current_layer = last_layer.pop()
#     else:
#         print("节点不存在！")

#
# goods = [{"name": "电脑", "price": 1999},
#            {"name": "鼠标", "price": 10},
#          {"name": "游艇", "price": 20},
#          {"name": "美女", "price": 998},]
#
# shopping_car = []
# flag = True
# while flag:
#     print("商品列表".center(30, "-"))
#     for i in range(len(goods)):
#         print("%s.%s %s" % (i, goods[i]["name"], goods[i]["price"]))
#     money = input("请输入你要充值的金额：").strip()
#     if money.isdigit():
#         money = int(money)
#         while flag:
#             choice = input("请输入您要购买的商品ID（Q退出）：").strip()
#             if choice.isdigit():
#                 choice = int(choice)
#                 if choice < len(goods):
#                     choice_num = input("请输入你要购买的数量：").strip()
#                     if choice_num.isdigit():
#                         choice_num = int(choice_num)
#                         if (goods[choice]["price"] * choice_num) < money:
#                             shopping_car.append({"name": goods[choice]["name"],
#                                                  "price": goods[choice]["price"],
#                                                  "个数": choice_num})
#                             money = money - (goods[choice]["price"] * choice_num)
#                             print("余额：%s" % (money,))
#                             go_no = input("是否继续购买Y/N：").strip().upper()
#                             if go_no == "Y":
#                                 continue
#                             else:
#                                 print("购物车".center(30, "-"))
#                                 for i in range(len(shopping_car)):
#                                     print("%s.%s %s￥ %s个" % (i, shopping_car[i]["name"],
#                                                              shopping_car[i]["price"],
#                                                              shopping_car[i]["个数"]))
#                                 flag = False
#                         else:
#                             print("余额不足！")
#
#                     else:
#                         print("请输入正确的金额！")
#
#                 else:
#                     print("你输入的商品ID不存在！")
#             elif choice == "q" or choice == "Q":
#                 print("购物车".center(30, "-"))
#                 for i in range(len(shopping_car)):
#                     print("%s.%s %s￥ %s个" % (i, shopping_car[i]["name"],
#                                                 shopping_car[i]["price"],
#                                                 shopping_car[i]["个数"]))
#                     flag = False
#             else:
#                 print("请输入正确的商品ID！")
#     else:
#         print("请输入正确的金额！")

pdf = open("./基础数据类型练习题/第二章练习题_1509863276.3079565", "rb")
pdf.read()
pdf.close()

