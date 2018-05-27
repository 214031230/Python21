#!/usr/bin/env python3
# import socket
# sk = socket.socket()
# sk.connect(("127.0.0.1", 9000))
# while True:
#     msg = input(">>>:")
#     msg = msg.encode("utf-8")
#     sk.send(msg)
#     print(sk.recv(1024))
# sk.close()

# import socket
# sk = socket.socket(type=socket.SOCK_DGRAM)
# while True:
#     c_msg = input(">>>:")
#     sk.sendto(c_msg.encode("utf-8"), ("127.0.0.1", 9000))
#     if c_msg == "q":break
#     msg, address = sk.recvfrom(1024)
#     print("%s:%s" % (address[0], msg))
# sk.close()
# import socket
# import json
# sk = socket.socket(type=socket.SOCK_DGRAM)
# while True:
#     username = input("请输入账号:")
#     password = input("请输入密码:")
#     msg = (username, password)
#     sk.sendto(json.dumps(msg).encode("utf-8"), ("127.0.0.1", 9000))
#     msg, address = sk.recvfrom(1024)
#     print("%s.%s:%s" % (address[0], address[1], msg.decode("utf-8")))
# sk.close()

# t1 = (1,2,3)
# import json
# ret = json.dumps(t1).encode("utf-8")
#
# print(json.loads(ret))