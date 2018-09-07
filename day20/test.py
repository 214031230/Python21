#!/usr/bin/env python3
lst = [1, 2, 3, 4, 5]
ret = list(filter(lambda x: x if x else None, map(lambda x: x + 3 if x % 2 == 0 else None, [1, 2, 3, 4, 5])))
print(ret)