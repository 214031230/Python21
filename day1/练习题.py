#!/usr/bin/env python3
# 　　1、使用while循环输出 1 2 3 4 5 6 8 9 10
count = 1
while count <= 10:
    print(count)
    count += 1
# 　　2、求1-100的所有数的和
count = 1
sums = 0
while count <= 100:
    sums = count + sums
    count += 1
print(sums)
# 　　3、输出 1-100 内的所有奇数
count = 1
while count <= 100:
    if count % 2 == 1:
        print(count)
    count += 1
# 　　4、输出 1-100 内的所有偶数
count = 1
while count <= 100:
    if count % 2 == 0:
        print(count)
    count += 1
# 　　5、求1-2+3-4+5 ... 99的所有数的和
count = 1
sums = 0
while count <= 100:
    if count % 2 == 0:
        sums = sums - count
    if count % 2 == 1:
        sums = count + sums
    count += 1
print(sums)
