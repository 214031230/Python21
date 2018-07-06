lst = [1, 2, 3, 4, 5, 6, 7]

# func = lambda x: x ** 2
#
# print(list(map(func, lst)))

# print(list(map(lambda x: x ** 2, lst)))
#
# print(list(filter(lambda x: x % 2 == 0, lst)))

# print([i for i in filter(lambda x: x if x < 68 else None, map(ord, "ABCDEFG"))])
# l = (i for i in filter(lambda x: x if x < 68 else None, map(ord, "ABCDEFG")))
# print(l.__next__())
# print(l.__next__())
# print(l.__next__())
# print(l.__next__())

# _, *args, b = [i for i in range(10)]
# print(_)
# print(b)
# print(args)
l1 = [1, (4, 5)]
a, (c, d) = l1
print(a, c, d)
