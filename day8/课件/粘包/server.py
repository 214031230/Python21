#_*_coding:utf-8_*_
from socket import *
sk=socket()
sk.bind(('127.0.0.1',8080))
sk.listen(5)

conn,addr=sk.accept()

data1=conn.recv(5)
data2=conn.recv(3)

print('----->',data1.decode('utf-8'))
print('----->',data2.decode('utf-8'))

conn.close()

sk.close()

# 粘包只会发生在tcp协议中
# 什么时候会发生粘包现象呢？ 在连续send的过程中 就容易发生粘包现象





















