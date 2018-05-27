#!/usr/bin/env python3
import socket
# sk = socket.socket()
# sk.bind(("127.0.0.1", 9000))
# sk.listen()
#
# con, addr = sk.accept()
# con.send(b"hellp")
# con.close()
# sk.close()


# sk = socket.socket()
# sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# sk.bind(("127.0.0.1", 9000))
# while True:
#     sk.listen()
#     con, address = sk.accept()
#     print(con.recv(1024))
#     msg = input(">>>:")
#     msg = msg.encode("utf-8")
#     con.send(msg)
#     con.close()
# sk.close()


sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(("127.0.0.1", 9000))
while True:
    msg, address = sk.recvfrom(1024)
    print("%s:%s" % (address[0], msg))
    if msg == "q":break
    s_msg = input(">>>:")
    sk.sendto(s_msg.encode("utf-8"), address)
sk.close()