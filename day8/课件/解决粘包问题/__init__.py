import struct
ret = struct.pack('i',102400000)
print(ret,len(ret))   # 无论多大 都能转成4位的

res = struct.unpack('i',ret)
print(res[0])