#!/usr/bin/env python3
with open(r"C:\Users\lanpa\Desktop\test.txt", mode="r") as f1:
    li1 = []
    li2 = []
    count = 1
    for i in f1:
        if count % 2 == 1:
            li1.append(i.strip())
        else:
            li2.append(i.strip())
        count += 1
for i in li1:
    with open(r"C:\Users\lanpa\Desktop\ip.txt", mode="a") as f2:
            f2.write(i + "\n")

for i in li2:
    with open(r"C:\Users\lanpa\Desktop\mac.txt", mode="a") as f2:
            f2.write(i + "\n")
# dic = {}
# count = 0
# for i in li1:
#     dic[i] = li2[count]
#     count += 1
# print(dic)
#
# for k, v in dic.items():
#     print(k,v)
#     with open(r"C:\Users\lanpa\Desktop\test1.txt", mode="a") as f2:
#         f2.write("%s  %s\n" % (k, v))
#



