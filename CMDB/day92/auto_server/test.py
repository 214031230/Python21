#!/usr/bin/env python3

l = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9]


def fun(l, num, start=0, end=None):
    end = len(l) - 1 if end is None else end
    if end < start: return None
    mid = (end - start) // 2 + start
    if l[mid] > num:
        return fun(l, num, start, mid - 1)
    elif l[mid] < num:
        return fun(l, num, mid + 1, end)
    else:
        return mid


print(fun(l, 2))
