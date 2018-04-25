#!/usr/bin/env python3
#
#
# 1.使用lamda表达下面函数。
#
# ```
#   def func(x, y):
#     return x+y
# ```
# res = lambda x, y: x+y

# 2.
#
# 	def foo():
# 	　　print('hello foo')
# 	　　return()
#
# 	def bar():
# 	　　print('hello bar')
#
# （1）为这些基础函数加一个装饰器，执行对应函数内容后，将当前时间写入一个文件做一个日志记录。
# import time
# def wrapper(f):
#     def inner(*args, **kwargs):
#         res = f(*args, **kwargs)
#         with open("tmp_log", mode="a", encoding="utf-8") as f1:
#             f1.write("%s 运行了 %s\n " % (time.time(), f))
#         return res
#     return inner
# @wrapper
# def foo():
#     print('hello foo')
#     return()
# foo()
# @wrapper
# def bar():
#     print('hello bar')
# bar()
# （2）改成参数装饰器，即可以根据调用时传的参数决定是否记录时间，比如@logger(True)
# import time
# FLAG = False
# def outer(FLAG):
#     def wrapper(f):
#         def inner(*args, **kwargs):
#             if FLAG == True:
#                 res = f(*args, **kwargs)
#                 with open("tmp_log", mode="a", encoding="utf-8") as f1:
#                     f1.write("%s 运行了 %s\n " % (time.time(), f))
#                 return res
#             else:
#                 res = f(*args, **kwargs)
#                 return res
#         return inner
#     return wrapper
# @outer(FLAG)
# def foo():
#     print('hello foo')
#     return()
# foo()
# @outer(FLAG)
# def bar():
#     print('hello bar')
# bar()

#
# 3. 通过内置函数计算5除以2的余数
# print(divmod(5,2)[1])
# # 4. 现有两元祖  (('a'),('b'),('c'),('d') ) ,请使用Python中的匿名函数生成列表 [ {'a':'c',{'c':'d'}]
# def fun(t):
#     return {t[0]: t[1]}
# res = map(fun,zip((('a'),('b')),(('c'),('d'))))
# print(list(res))
# res = zip((('a'),('b'),('c'),('d')))
# res = res.__next__()
# print(res)


# 5. list 对象 alist [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]，
# 请按 alist 中元素的age  由大到小排序；
# alist = [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]


# alist.sort(key=lambda x:x['age'], reverse=True)



# 6.
# l1=[1,2,3,4]
# s='hel'
# # 	使用内置函数输出 [(1, 'h'), (2, 'e'), (3, 'l')]
# res = zip(l1, s)
# print(list(res))
# # 7.
# shares = {
# 	    'IBM': 36.6,
# 	    'Lenovo': 23.2,
# 	    'oldboy': 21.2,
# 	    'ocean': 10.2,
# 	}
#
# 	输出钱大于20的人名  结果为['IBM', 'Lenovo', 'oldboy']
# def func(x):
#     if shares[x] > 20:
#         return x
# res = filter(func,shares)
# print(list(res))
# res = filter(lambda x: shares[x] > 20, shares)
# print(list(res))
# ret = [i[0] for i in shares.items() if i[1] > 20]
# print(ret)
# [i[0] for i in shares.items() if i[1] > 20]
# lst = []
# for i in shares.items():
#     if i[1] > 20:
#         lst.append(i[1])
# print(lst)

#
# 8. name=['alex','wupeiqi','yuanhao']   将每个人名后加_sb 结果为['alex_sb','wupeiqi_sb','yuanhao_sb']
# name=['alex','wupeiqi','yuanhao']
# res = map(lambda x: "%s_sb" % (x,),name)
# print([i+"_sb" for i in name])
# print(list(res))
# 9.
salaries={
	    'egon':3000,
	    'alex':100000000,
	    'wupeiqi':10000,
	    'yuanhao':250
	}
# for i in salaries:
#     print(i)
#


res = max(salaries, key=lambda x:salaries[x])
print(res)
#
# print(res)

# li = [2,3,-1,3]
# res = max(li,key=abs)
# print(res)
#
# 	输出钱最多的人名  结果为alex

# li = [2,3,-1,3]
# def func(x):
#     print(x)
# res = map(func,li)
# print(list(res))
# alist.sort(key=lambda x:x['age'], reverse=True)
#
# 10.
salaries={
	    'egon':3000,
	    'alex':100000000,
	    'wupeiqi':10000,
	    'yuanhao':250
	}
# 	1. 按字典的key去排序，结果salaries={'alex':100000000,'egon':3000,'wupeiqi':10000,'yuanhao':250}
# alist.sort(key=lambda x:x['age'], reverse=True)
def func(x):
    return x,salaries[x]
res = map(func,sorted(salaries,key=lambda x:salaries[x],reverse=True))
dic = {}
for i in res:
    dic[i[0]] = i[1]
print(dic)
# 	2. 按照值排序，按照从小到大的顺序打印出key 结果为['yuanhao', 'egon', 'wupeiqi', 'alex']
res = sorted(salaries, key=lambda x: salaries[x])
print(res)

#
#
#
#
#
#
#
