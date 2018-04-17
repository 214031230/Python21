#!/usr/bin/env python3
# 1.写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组
# 例如：[(‘红心’，2),(‘草花’，2), …(‘黑桃’，‘A’)]


def fun1():
    l1 = ["红心", "草花", "黑桃", "方块"]
    l2 = []
    for i in range(53):
        if i == 0:
            pass
        else:
            for x in l1:
                l2.append((x, i))
    return l2


print(fun1())

#
# 2.写函数，传入n个数，返回字典{‘max’:最大值,’min’:最小值}
# 例如:min_max(2,5,7,8,4)
# 返回:{‘max’:8,’min’:2}


def fun2(*args):
    dic = {"max": max(args),
           "min": min(args)}
    return dic


print(fun2(2,234,23,4,1,5,2,3,523,4))

# 3.
# 写函数，专门计算图形的面积
# 其中嵌套函数，计算圆的面积，正方形的面积和长方形的面积
# 调用函数area(‘圆形’, 圆半径)  返回圆的面积
# 调用函数area(‘正方形’, 边长)  返回正方形的面积
# 调用函数area(‘长方形’, 长，宽)  返回长方形的面积
#
#


def area(graphic, argv1, argv2 = 0):
    if graphic == "圆形":
        def round():
            print (2*3.14*argv1)
        round()
    elif graphic == "正方形":
        def square():
            print(argv1*argv1)
        square()
    elif graphic == "长方形":
        def rectangle():
            print(argv1*argv2)
        rectangle()

area("正方形",4)






