#!/usr/bin/env python3
# 1. 字符编码的发展背景，历程做简要概述
# 二进制  十进制  ascii (gbk等其等其他国家编码) unicode  utf-8
# 2. python运算符有哪些？每种运算符下有哪些方法？
# 数学运算：+ - * / %
# 比较运算：> < == >= <=  !=
# 逻辑运算  and  or  not
# 3. python的数据类型有哪些？每种数据类型的特征？
# str 字符串
# int 数字类型
# float 浮点类型
# 列表
# 元组（不可变列表）
# 字典
# 集合
# 4. 列举字符串的10种常用方法
# s = "5  AbcA123 45"
# s1 = s.replace("A", "a")  # 默认替换所有
# print(s1)
# s2 = s.replace("A", "a", 1)  # 只替换第一个
# print(s2)
# s3 = s.strip() # 默认去掉空格
# print(s3)
# s4 = s.strip("45") #
# print(s4)
# print(s.index("A"))  # 通过元素取索引
# s = "abc#def^gh"
# print(s.title())
# s = "aBcDeF"
# print(s.swapcase())
# 5. 列举列表的10种常用方法
# 6. 已知字符串 name = “aahhh113244ADD.,/'[@#$hhhhTTTTTT666”,要求如下:
# 	1.请将name字符串的数字取出，并输出成一个新的字符串。
# 	2.请去除name字符串多次出现的字母，仅留最先出现的一个。例 ‘abcabb’，经过去除后，输出 ‘abc’
# 	3.请将name字符串反转并输出。例：’abc’的反转是’cba’
# name = "aahhh113244ADD., / '[@#$hhhhTTTTTT666"
# # name2 = "".join([i for i in name if i.isdigit()])
# # print(name2)
# lst = list(name)
# lst.reverse()
# print("".join(lst))

# name1 = "".join(lst)
# print(name1)
# 7. 8<<2等于？
# print(8 << 2)
# 8. s=[1,"h",2,"e",[1,2,3],"l",(4,5),"l",{1:"111"},"o"],将s中的5个字符提取出来并拼接成字符串。
# s=[1,"h",2,"e",[1,2,3],"l",(4,5),"l",{1:"111"},"o"]
# s1 = "".join([i for i in s if str(i).isalpha()])
# print(s1)
# 9.
# a = [1,2,[3,"hello"],{"egon":"aigan"}]
# b = a[:]
# c = a
#
# a[0] = 5  # [5,2,[3,"hello"],{"egon":"aigan"}]
# a[2][0] = 666 # [5,2,[666,"hello"],{"egon":"aigan"}]
# #
# print(a)  # [5,2,[666,"hello"],{"egon":"aigan"}]   正常修改后的结果
# print(b)  # [1,2,[666,"hello"],{"egon":"aigan"}]   b 等于 a的值并不是等于a,所以索引0不会变，但列表里面的列表又共享内存地址所以会跟着变
# print(c)  # [5,2,[666,"hello"],{"egon":"aigan"}]   c 等于 a 所以c和a共享内存地址，所有c会随着a进行变化
# # 	#计算结果以及为什么？
# # 10.
# list1 = [2, 3, 8, 4, 9, 5, 6]
# list2 = [5, 6, 10, 17, 11, 2]
# # 	升序合并并去重在 list3 列表中
# print(set(list1) | set(list2))  # 并集
# print(set(list1) & set(list2))  # 交集
# print(set(list1) ^ set(list2))  # 反交集
# print(set(list1) - set(list2))  # 差集
# print(set(list1) < set(list2))  # 子集
# print(set(list1) > set(list2))  # 超集

# 11. 用至少2种不同的方式删除一个list里面的重复元素
# lst = [6,1,1,2,3,4,5,6,6,5]
# lst1 = set(lst)
# print(lst1)
# count = 0
# 10. 通过函数化编程实现5的阶乘
# 5*4*3*2*1
# def func(argv):
#     if argv == 1:return 1
#     return func(argv-1) * argv
# print(func(5))
# 11. 编写代码实现9*9乘法口诀表
# 	1 * 1 = 1
# 	2 * 1 = 2   2 * 2 = 4
# 	3 * 1 = 3   3 * 2 = 6   3 * 3 = 9
# for i in range(1, 10):
#     for x in range(1, i + 1):
#         print("%s * %s = %s" % (x, i, i * x), end=" ")
#     print()

# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('%s * %s = %2s' % (j, i, i*j), end=' ')
#     print()
# # 12. 输入一个年份，判断是否是闰年？
# def func(argv):
#     if argv % 4 == 0 and argv % 100 != 0:
#         return "闰年"
#     else:
#         return "平年"
#
# print(func(1900))
# # 13. 任意输入三个数，判断大小？
# def func(x, y, z):
#     return max(x, y, z)
# print(func(5,7,9))
# 14. 写三层循环，用户在最里层退出，整个程序终止。


# 15. a = 12，b = 13，不用中间变量交换a和b的值？
# a = 12
# b = 13
# a, b = b, a
# print(a, b)
# 16.
# def f(x, l = [] ): # x = 2    # x =  3  l = [3,2,1]
#     for i in range(x):  # x = 2  range = 0,1  #  x = 3  range = 0,1,2
#         l.append(i*i)   # 0, 1    # [3,2,1,0,1,4]
#     print(l)  # l = [0,1]  # [3,2,1,0,1,4] # [0,1,0,1,4]
#
# f(2)
# f(3,[3,2,1])
# f(3)
# 	输出结果
# 17. 请将 "1,2,3"，变成 ["1","2","3"]
# s = "1,2,3"
# lst = s.split(",")
# print(lst)
# 18. is和==的区别是？ is 是比较内存地址  == 是比较数值
# 19. 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
# s = "asdf 7LKS&65lfdhKB LGN;lg"
# def func(x):
#     print("数字:%s" % len([i for i in x if i.isdigit()]))
#     print("字母:%s" % len([i for i in x if i.isalpha()]))
#     print("空格:%s" % len([i for i in x if i.isspace()]))
#     print("其他:%s" % len([i for i in x if not i.isspace() and not i.isdigit() and not i.isalpha()]))
# func(s)

# s = "123T"
# for i in s:
#     if i.isdigit():
#         print(i)
# res = filter(func,s)
# print(list(res))

# 20. 求1～100间所有偶数的和（亦可奇数和，使用while循环写）
# count = 1
# sum = 0
# while count <= 100:
#     if count % 2 == 0:
#         sum += count
#     count += 1
# print(sum)

# 21. 将列表['alex', 'steven', 'egon'] 中的每一个元素使用 ‘\_’ 连接为一个字符串
# lst = ['alex', 'steven', 'egon']
# s = "_".join(lst)
# print(s)














































