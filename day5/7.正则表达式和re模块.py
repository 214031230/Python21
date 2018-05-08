#!/usr/bin/env python3
import re
# findall
s = "1+2+(1*(1+2))+2+(1*4)"
s1 = "1+1+1+(1*3)+2+(1*4)"
print(re.findall("\(.+?\)\)?", s))
# search
print(re.search("\d", s))
print(re.search("\d", s).group())

# match
print(re.match("\W", s))
print(re.match("\d", s).group())
print(re.split("[+]", s1))



