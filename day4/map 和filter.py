#!/usr/bin/env python3
# lst1 = [1,2,3,4,5]
# def func1(x):
#     return x % 2 == 1
# res = map(func1, lst1)
# for i in res:
#     print(i)
#
# lst2 = [1,2,3,4,5]
# def func2(x):
#     return x % 2 == 1
# res = filter(func2, lst2)
# for i in res:
#     print(i)

lst1 = [1,2,3,4,5]
def func1(x):
    return x > 3
res = map(func1, lst1)
for i in res:
    print(i)

lst2 = [1,2,3,4,5]
def func2(x):
    return x > 3
res = filter(func2, lst2)
for i in res:
    print(i)