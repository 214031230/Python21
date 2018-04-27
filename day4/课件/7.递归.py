# 递归的定义——在一个函数里再调用这个函数本身，实际操作中递归必须要有个可停止的条件。
# 递归解析为递推和回溯两步，先递推当满足条件以后开始回溯
# 递归的最大深度—997
# RecursionError: maximum recursion depth exceeded while calling a Python object
def func():
    print(1)
    func()
func()

#  测试递归的最大深度
def foo(n):
    print(n)
    n += 1
    foo(n)
foo(1)

import sys
#  修改递归的最大深度，一般不修改，如果默认递归深度解决不了 说明这个问题不能用递归解决
sys.setrecursionlimit(2000)

# 用递归计算6*5*4*3*2*1的乘积
print(6*5*4*3*2*1)
def fn(n):
    if n == 1:return 1
    return n*fn(n-1)
print(fn(6))

# 第一次fn(6)  # 返回值 6*fn(6-1)= 720
def fn(n): # n = 6
    if 6 == 1:return 1
    return 6*fn(6-1)

# 第二次fn(6-1) # 返回值 5*fn(5-1) = 120
def fn(n): # n = 5
    if 5 == 1:return 1
    return 5*fn(5-1)

# 第三次fn(5-1)  # 返回值 4*fn(4-1) = 24
def fn(n): # n = 4
    if 4 == 1:return 1
    return 4*fn(4-1)

# 第四次fn(4-1) # 返回值 3*fn(3-1) = 6
def fn(n): # n = 3
    if 3 == 1:return 1
    return 3*fn(3-1)

# 第五次fn(3-1) # 返回值 2*fn(2-1) = 2
def fn(n): # n = 2
    if 2 == 1:return 1
    return 2*fn(2-1)

# 第六次fn(2-1)   返回值 fn(2-1）= 1
def fn(n): # n = 2
    if 1 == 1:return 1
    return 2*fn(2-1)


# 练习 打印列表的元素
li = [1, [2, [3, [4, [5]]]]]

def fun(li):
    for i in li:
        if type(i) == list:
            fun(i)
        else:
            print(i)
fun(li)


