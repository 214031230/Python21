# li = [1, 2, 3, 43, 'fdsa', 'alex']
# count = 0
# for i in li:
#     count += 1
# print(count)
#
# s1 = 'fdsgdfkjlgdfgrewioj'
#
# count = 0
# for i in s1:
#     count += 1
# print(count)


# 重复代码多
# 可读性差。
# len()

s1 = 'fdsgdfkjlgdfgrewioj'
def my_len():
    count = 0
    for i in s1:
        count += 1
    # print(count)

my_len()  # 函数名+() 执行函数
'''
def 关键字 函数名（设定与变量相同）:
    函数体
'''
# print(len(s1))

#函数的返回值 return
'''
    1,遇到return，结束函数。
    def func1():
        print(11)
        print(22)
        return
        print(333)
        print(444)
    func1()
    2,给函数的调用者(执行者)返回值。
        无 return 返回None
        return 不写 或者 None 返回None
        return 返回单个数.
        return 返回多个数，将多个数放在元组中返回。
'''


# def my_len():
#     count = 0
#     for i in s1:
#         count += 1
#     return 666
# print(my_len(),type(my_len()))

# def my_len():
#     count = 0
#     for i in s1:
#         count += 1
#     return 666,222,count,'老男孩'
# print(my_len(),type(my_len()))

# def my_len():
#     count = 0
#     for i in s1:
#         count += 1
#     return 666,222,count
# ret1,ret2,ret3 = my_len()  # (666, 222, 19,)
# print(ret1)
# print(ret2)
# print(ret3)

# def my_len():
#     count = 0
#     for i in s1:
#         count += 1
#     return count
# print(my_len())
# print(len(s1))

#函数的传参
li = [1, 2, 3, 43, 'fdsa', 'alex']
s1 = 'fdsgdfkjlgdfgrewioj'

# def my_len(a):  # 函数的定义（）放的是形式参数，形参
#     count = 0
#     for i in a:
#         count += 1
#     return count
# ret = my_len(li)  # 函数的执行（） 实际参数，实参
# print(ret)
# print(len(s1))

# 从实参角度
    #1，位置参数。 必须一一对应，按顺序
# def func1(x,y):
#     print(x,y)
# func1(1, 2)
    #2，关键字参数。必须一一对应，不分顺序。
# def func1(x,y,z):
#     print(x,y,z)
# func1(y=2,x=1,z=5,)

# def max(a,b):
#     if a > b:
#         return a
#     else:
#         return b
# print(max(100,102))
# def max(a,b):return a if a > b else b
# print(max(100,102))
    #3,混合参数。一一对应 且 关键字参数必须在位置参数后面。
# def func2(argv1,argv2,argv3):
#     print(argv1)
#     print(argv2)
#     print(argv3)
# func2(1,2,argv3=4)
# 从形参角度
    #1，位置参数。 必须一一对应，按顺序
# def func1(x,y):
#     print(x,y)
# func1(1,2)
    #2，默认参数。 必须在位置参数后面。
# def register(name,sex='男'):
#     with open('register',encoding='utf-8',mode='a') as f1:
#         f1.write('{} {}\n'.format(name,sex))
#
# while True:
#     username = input('请输入姓名：/q 或者 Q 退出')
#     if username.upper() == 'Q':break
#     if 'a' in username:
#         sex = input('请输入性别：')
#         register(username,sex)
#     else:
#         register(username)

    #3，动态参数 *args，**kwargs 万能参数

# def func2(*args,**kwargs):
#     print(args)  # 元组(所有位置参数)
#     print(kwargs)
# func2(1,2,3,4,5,6,7,11,'alex','老男孩',a='ww',b='qq',c='222')
# 位置参数，*args,默认参数
# def func3(a,b,*args,sex='男'):
#     print(a)
#     print(b)
#     print(sex)
#     print(args)
# func3(1,2,'老男孩','alex','wusir',sex='女')
# 位置参数，*args,默认参数,**kwargs
# def func3(a,b,*args,sex='男',**kwargs):
#     print(a)
#     print(b)
#     print(sex)
#     print(args)
#     print(kwargs)
# func3(1,2,'老男孩','alex','wusir',name='alex',age=46)
def func1(*args,**kwargs):  #　函数的定义 * 聚合。
    print(args)
    print(kwargs)
# l1 = [1,2,3,4]
# l11 = (1,2,3,4)
# l2 = ['alex','wusir',4]
# func1(*l1,*l2,*l11)  # 函数的执行：* 打散功能。
# func1(1,2,3,4,'alex','wusir',4,1,2,3,4)  # 函数的执行：* 打散功能。
# dic1 = {'name1':'alex'}
# dic2 = {'name2':'laonanhai'}
# func1(**dic1,**dic2)


