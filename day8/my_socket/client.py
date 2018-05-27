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

import socket
sk = socket.socket(type=socket.SOCK_DGRAM)
while True:
    c_msg = input(">>>:")
    sk.sendto(c_msg.encode("utf-8"), ("127.0.0.1", 9000))
    if c_msg == "q":break
    msg, address = sk.recvfrom(1024)
    print("%s:%s" % (address[0], msg))
sk.close()
