#!/usr/bin/env python3
from concurrent.futures import ThreadPoolExecutor
#
#
# def eat(num):
#     return num
#
#
# def play(num):
#     print(num.result())
#
#
# if __name__ == '__main__':
#     t = ThreadPoolExecutor(2)
#     for i in range(10):
#         t.submit(eat, i).add_done_callback(play)
print(3>4 or 4<3 and 1==1) # FALSE
print(1 < 2 and 3 < 4 or 1>2) # True
print(2 > 1 and 3 < 4 or 4 > 5 and 2 < 1) # True
print(1 > 2 and 3 < 4 or 4 > 5 and 2 > 1 or 9 < 8) #  F
                #  f  or f or f
print(1 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6) # f
                 #  f or f or f
print(not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6) # f
      # f              f  or   f or f