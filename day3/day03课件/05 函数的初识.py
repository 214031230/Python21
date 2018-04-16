# # 分别计算列表和字符串的长度，不适用内置函数len()的情况下
#
# li = [1, 2, 3, 43, 'fdsa', 'alex']
# count = 0
# for i in li:
#     count += 1
# print(count)
#
# s1 = 'fdsgdfkjlgdfgrewioj'
# count = 0
# for i in s1:
#     count += 1
# print(count)
#
# # 发现问题，计算列表和字符串长度代码是重复的。
# li = [1, 2, 3, 43, 'fdsa', 'alex']
# s1 = 'fdsgdfkjlgdfgrewioj'
# # 定义my_len函数
# def my_len(argv):
#     count = 0
#     for i in argv:
#         count += 1
#     return count
#
# print(my_len(li))
# print(my_len(s1))

# '''
# def 关键字 函数名（设定与变量相同）:
#     函数体
# '''
# print(len(s1))



# 函数的返回值 return
# 1、遇到return，结束函数。不执行return下面的代码和break类型
# 下面代码不会的打印3和4
# def func1():
#     print(1)
#     print(2)
#     return
#     print(3)
#     print(4)
# func1()
#
# # 2、给函数的调用者(执行者)返回值。
# """
#     无 return 则返回None
#     return 不写 或者 None 返回None
#     return 返回单个数.
#     return 返回多个数，将多个数放在元组中返回。
# """
#
# # 示例1：
# s1 = "1235sdafadf234afsfdafas"
# def my_len(argv):
#     count = 0
#     for i in argv:
#         count += 1
#     return count
# print(my_len(s1),type(my_len(s1))) # 返回值类型和原来保持一致
#
# # 示例2（返回多个值，多个值存储在元组中返回）：
# def my_len():
#     count = 0
#     for i in s1:
#         count += 1
#     return 666, 222, count, '老男孩'
# print(my_len(),type(my_len()))
#
# # 示例3，返回值的分别赋值：
# def my_len():
#     count = 0
#     for i in s1:
#         count += 1
#     return 666, 222, count
# ret1, ret2, ret3 = my_len()  # (666, 222, 23,)
# print(ret1)
# print(ret2)
# print(ret3)

#
# def my_len():
#     count = 0
#     for i in s1:
#         count += 1
#     return count
# print(my_len())
# print(len(s1))



#函数的传参
# li = [1, 2, 3, 43, 'fdsa', 'alex']
# s1 = 'fdsgdfkjlgdfgrewioj'
#
# def my_len(argv):  # 函数的定义（）放的是形式参数，形参
#     count = 0
#     for i in argv:
#         count += 1
#     return count
# ret = my_len(li)  # 函数的执行（） 放的是实际参数，实参
# print(ret)
# print(len(s1))

# 从实参角度
# 1、位置参数。 必须按顺序一一对应，按顺序
# def func1(x,y):
#     print(x,y)
# func1(1, 2)
#
# #2、关键字参数。可以不分顺序，但参数必须一一对应。
# def func1(x, y, z):
#     print(x, y, z)
# func1(y=2, x=1, z=5,)
#
# # 三元运算
# # 比较两个数的大小，普通写法
# def max(a, b):
#     if a > b:
#         return a
#     else:
#         return b
# print(max(100, 102))
# # 三元运算写法
# def max(a, b):return a if a > b else b
# print(max(100,102))

#3,混合参数。位置参数顺序一一对应 且关键字参数必须在位置参数后面。
# def func2(argv1,argv2,argv3):
#     print(argv1)
#     print(argv2)
#     print(argv3)
# func2(1, 2, argv3=4)

# 从形参角度
# 1、位置参数。 必须一一对应，按顺序
# def func1(x,y):
#     print(x,y)
# func1(1,2)

# 2、默认参数。 必须在位置参数后面。
# 统计姓名和性别
# def register(name, sex='男'):
#     with open('register', encoding='utf-8', mode='a') as f1:
#         f1.write('{} {}\n'.format(name, sex))
#
# while True:
#     username = input('请输入姓名 q退出：')
#     if not username:continue
#     if username.upper() == 'Q':break
#     sex = input('请输入性别：')
#     if not sex:
#         register(username)
#     else:
#         register(username, sex)

# 3、动态参数 *args，**kwargs 万能参数
# *args 以元组的方式存储所有的位置参数 , **kwargs 以字典的方式存储所有关键字参数
# def func2(*args, **kwargs):
#     print(args)  # 元组(所有的位置参数)
#     print(kwargs) # 字典(所有的关键字参数)
# func2(1, 2, 3, 4, 5, 6, 7, 11, 'alex', '老男孩', a='ww', b='qq', c='222')
#
#
# # 当有位置参数，默认参数,动态参数（*args）的时候,顺序如下：
# # 位置参数--->*args--->默认参数
# def func3(a, b, *args, sex='男'):
#     print(a)
#     print(b)
#     print(sex)
#     print(args)
# func3(1,2,'老男孩','alex','wusir',sex='女')
#
# # 当有位置参数，默认参数,动态参数（*args和**kwargs）的时候,顺序如下：
# # 位置参数--->*args--->默认参数--->**kwargs
# def func3(a,b,*args,sex='男',**kwargs):
#     print(a)
#     print(b)
#     print(sex)
#     print(args)
#     print(kwargs)
# func3(1,2,'老男孩','alex','wusir',name='alex',age=46)
#
# #　函数的定义： * 聚合。
# def func1(*args,**kwargs):
#     print(args)
#     print(kwargs)
#
# # 把以下数据类型以元素的方式分别传给动态参数
# l1 = [1, 2, 3, 4]
# t1 = (1, 2, 3, 4)
# l2 = ['alex', 'wusir', 4]
# dic1 = {'name1': 'alex'}
# dic2 = {'name2': 'laonanhai'}
#
# # 函数的执行：* 打散功能。
# func1(l1, t1, l2, dic1, dic2)  # 错误写法
# func1(*l1, *l2, *t1, **dic1, **dic2)  # 正确写法等于 func1(1,2,3,4,'alex','wusir',4,1,2,3,4,"name1"="alex","name2"="laonanhai")



