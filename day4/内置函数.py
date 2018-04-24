#!/usr/bin/env python3
# 内置函数
#   基础数据类型相关
#       和数字相关的
#           数字类型
                # bool
print(bool(1)) # True
print(bool(0)) # False
print(bool("")) # False
print(bool(" ")) # True
print(bool([])) # False
#               # int
a = "123"
print(type(int(a)))  # <class 'int'>
#               # float
a = 100
print(float(a)) # 100.0 转换成浮点类型
#           进制转换
#               bin 二进制
a = 100
print(bin(a))   # 0b1100100
#               oct 八进制
print(oct(a))   # 0o144
#               hex 十进制
print(hex(a))   # 0x64
#           数学运算
#               abs 绝对值
a = -100
print(abs(a)) # 100
#               divmod 返回（除，余）
print(divmod(100, 3))  # (33, 1)
#               round 小数精确
a = 3.145236
print(round(a)) # 3
print(round(a, 2)) # 3.15 可以指定精确位数，四舍五入
#               pow  幂运算（x,y,z）
print(pow(1, 2, 3))
#               sum 求和
res = sum(i for i in range(10))  # 生成器表达式可以用在sum求值
print(res)
lst = [1,2,3,4,5]
print(sum(lst)) # 所有可迭代int类型对象都可以求和
print(sum([1,2,3,4,5],10))
#               min 最小值
print(min(lst))
print(min(lst, key=lambda x: abs(x - 5)))
#               max 最大值
# print(max(lst))
#           数据结构相关
#               序列
#                   列表和元组
#                       list 列表
list()
tuple()
#                       tuple 元组
#                   相关内置函数
#                       reversed  反转可迭代对象，返回一个迭代器
lst = [1, 2, 3, 4, 5]
res = reversed(lst)
print(dir(reversed(lst)))
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())
#                   字符串

# str 字符串

# bytes
s = "abcd"
s1 = s.encode(encoding="utf-8") # unicode转换成bytes(utf-8)的类型
print(s1)  # b'abcd'
s2 = s1.decode(encoding="utf-8") # 把 bytes（以utf-8存储）转换成unicode类型
print(s2)  # abcd

# repr
print(1)
print('1')
print(repr(1))
print(repr('1'))

# ord 和  chr 对应ascii码表
# print(ord('a'))    # 小写的a-z 97+26  A-Z 65+26
# print(chr(97))

#               数据集合
#                   dict 字典
#                   set 集合
#                       frozenset 冻结集合，不可变集合
#               相关内置函数
#                   all  判断是否有布尔值为false的值
#                   any  判断是否有布尔值为True的值
#                   zip 返回一个迭代器
lst1 = [1,2,3,4]
lst2 = [4,5,6,7]
# lst3 = ["a","b","c","d"]
lst3 = ["a", "b"]
print(zip(lst1, lst2, lst3))
for i in zip(lst1, lst2, lst3):
    print(i)
l1 = [[1,2,3],[4,5,6],[7,8,9]]
print(*l1)
for i in zip(*l1):  # * + 可迭代对象是返回可迭代对象的元素
    print(i)
#                   filter 对元素进行处理过滤，返回处理前的元素
lst4 = [1, 2, 3, 4, 5]
def func(x):
        return x > 4
def func1(x):
    return x % 2 == 1
res = filter(func1,lst4)
for i in res:
    print(i)
lst5 = ['test', None, '', 'str', '  ', 'END']
def func2(x):
    return x and x.strip()
res = filter(func2,lst5)
for i in res:
    print(i)
# 请利用filter()过滤出1~100中平方根是整数的数，即结果应该是：
def func3(x):
    return x % 2 == 1
res = filter(func3,range(1,101))
print(dir(res))
for i in res:
    print(i)
#               map 把元素进行处理，并返回处理过的元素
lst6 = [1,2,3,4,5]
def func4(x):
    return x % 2 == 1
# print(map(func4, lst6))
res = map(func4, lst6)
for i in res:
    print(i)
#               sorted
li1 = [3,2,4,2,5,3,51]
print(sorted(li1))
#   迭代器/生成器相关
#       range()
#       iter()
#       next()
#   作用域相关
#   其他
#       eval
print(eval("1+1"))
#       exec
print(exec("1+1"))
#       input()
#       print()
print(123, end="")
print(123, end="")
print(123, end="")
import time
# for i in range(1,101):
#     print("\r%s %%%s" % (i, "#"*i), end="")
#     time.sleep(0.3)
# print(sum([1,2,3,4,5],10))
#         hash
print(hash("1231231"))

# 对可hash的数据类型进行hash之后会得到一个数字
# 在一次程序的执行过程中 对相同的可哈希变量 哈希之后的结果永远相同的
# 在一次程序的执行过程中 对不相同的可哈希变量 哈希之后的结果几乎总是不相同的

# def func():
#     a = 1
#     b = 2
#     print(locals())
#     print(globals())
# 全局命名空间中的名字
# print(locals())   # 本地的命名空间
# print(globals())  # 全局的命名空间
# func()