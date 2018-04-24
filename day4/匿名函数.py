#!/usr/bin/env python3
# lambda 表达式
# 普通函数
def func(a, b):
    return a + b

#lambda 表达式
func1 = lambda a,b: a + b

print(func(1, 2))
print(func1(1, 2))

# 示例1
# 普通写法
def func(num):
    return num ** 2
for i in map(func,range(10)):print(i)

# lambda写法
for i in map(lambda num: num ** 2, range(10)): print(i)

# 示例2
# 普通写法
def func(num):
    return num % 2
print(min(-2,3,-4,key=func))

# lambda写法
print(min(-2, 3, -4, key=lambda num: num % 2))

# 示例3
d = lambda p: p*2
t = lambda p: p*3
x = 2
x = d(x)   # x = 4
x = t(x)   # x = 12
x = d(x)   # x = 24
print(x)   # x = 24

# 练习1
# 现有两元组(('a'), ('b')), (('c'), ('d')), 请使用python中匿名函数生成列表[{'a': 'c'}, {'b': 'd'}]
def func1(t):
    return {t[0]:t[1]}
res = map(func1,zip((('a'), ('b')), (('c'), ('d'))))
print(list(res))

res = map(lambda t: {t[0]: t[1]}, zip((('a'), ('b')), (('c'), ('d'))))
print(list(res))

# 练习2
# 以下代码的输出是什么？请给出答案并解释。
def multipliers():
    return (lambda x:i*x for i in range(4)) #

print([m(2) for m in multipliers()])
g = (m(2) for m in multipliers())
for i in g:
    print(i)

# 解析：
# # 第一步分解 def multipliers():
# def multipliers():
#     lst = []
#     for i in range(4):
#         lst.append(lambda x:i*x)
#     return lst
# # 第二步展开 def multipliers():
# def multipliers():
#     lst = []
#     i = 0
#     lst.append(lambda x:i*x)
#     i = 1
#     lst.append(lambda x:i*x)
#     i = 2
#     lst.append(lambda x:i*x)
#     i = 3
#     lst.append(lambda x:i*x)
#     return lst
# # 第三步 分解[m(2) for m in multipliers()]
# lst1 = []
# for m in multipliers(): # multipliers() = lst[lambda x:i*x,lambda x:i*x,lambda x:i*x,lambda x:i*x]
#     m(2) # m = lambda x:i*x
#          # m(2) 执行函数传参2
