#!/usr/bin/env python3

d = {"1": "123", "2": "123", "3": "456", "4": "456", "5": "123"}

print(sorted(d.keys(), reverse=True))
# l1 = []
# l2 = []
# for k, v in d.items():
#     # 循环所有key和value
#     # 判断值在不在l1中,如果在则添加key到l2中
#     if v in l1:
#         l2.append(k)
#     l1.append(v)
# print(l2)
# print(",".join(l2))
