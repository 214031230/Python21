#!/usr/bin/env python3
import re
s = "1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) ) + ( 4 * 5 )"
print(re.findall("-?\d+\.?\d*", s))
print(re.findall("[+\-*/]", s))
print(re.findall("\(.+\)", s))

def func(s):
    pass