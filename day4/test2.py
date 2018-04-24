#!/usr/bin/env python3
# import time
# count = 1
# while True:
#     with open("tmp", mode="a") as f1:
#         f1.write("我是第%s行\n" % (count,))
#     count += 1
#     time.sleep(1)
def func_g(num = 0):
    sums = 0
    day = 0
    avg = 0
    while True:
        yield avg  # 返回avg，并接受seed传进来的money
          # sums = sums + money
        # day += 1
        avg += 1
        # avg = sums/day


g = func_g()
print(next(g))
print(next(g))
print(next(g))
print(next(g))