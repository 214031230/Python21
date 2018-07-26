#!/usr/bin/env python3
import socket
# server = socket.socket()
# server.bind(("127.0.0.1", 9000))
# server.listen()
#
# con,addr = server.accept()
#
# ret = con.recv(1024).decode("utf-8")
# print(ret)
# con.close()
# server.close()
# server = socket.socket(type=socket.SOCK_DGRAM)
# server.bind(("127.0.0.1", 9001))
# msg, addr = server.recvfrom(1024)
# print(addr, msg.decode("utf-8"))
# server.close()
# import socket
#
#
# class QQServer:
#     __isinstance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not cls.__isinstance:
#             obj = object.__new__(cls)
#             cls.__isinstance = obj
#         return cls.__isinstance
#
#     def __init__(self, ip, port):
#         self.ip = ip
#         self.port = port
#         self.server = socket.socket(type=socket.SOCK_DGRAM)
#         self.__code = "utf-8"
#
#     def bind(self):
#         self.server.bind((self.ip, self.port))
#
#     def run(self):
#         print("QQServer start...")
#         self.bind()
#         while 1:
#             msg, address = self.server.recvfrom(1024)
#             if msg:
#                 print("%s:%s" % (address, msg.decode(self.__code)))
#             to_msg = input(">>>:").encode(self.__code)
#             self.server.sendto(to_msg,address)
#
#
# server = QQServer("127.0.0.1", 9000)
# # server.run()
# import struct
# server = socket.socket()
# server.bind(("127.0.0.1",9000))
# server.listen()
# con, address = server.accept()
# # 接受数据长度
# header_len_bytes = con.recv(4)
# # 获取获取的真实长度
# header_len = struct.unpack("i", header_len_bytes)[0]
# # 接受真实的数据
# print(con.recv(header_len).decode("utf-8"))
# server.close()
# import struct
# import json
# server = socket.socket()
# server.bind(("127.0.0.1",9000))
# server.listen()
# con, address = server.accept()
# # 接受数据长度
# header_len_bytes = con.recv(4)
# # 获取获取的真实长度
# header_len = struct.unpack("i", header_len_bytes)[0]
# print("header_len",header_len)
# header_info = con.recv(header_len).decode("utf-8")
# print("header_info",header_info)
# header_info = json.loads(header_info)
# print("header_info",header_info)
# # 接受真实的数据
# with open("./day1.bak", "wb") as f:
#     size = 0
#     while size < header_info["size"]:
#         ret = con.recv(1024)
#         f.write(ret)
#         size += len(ret)

import socketserver


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        address = self.client_address
        while 1:
            msg = conn.recv(1024).decode("utf-8")
            if hasattr(self, msg):
                print("%s:%s" % (address, msg))
                getattr(self, msg)()

    def ls(self):
        print("in ls")

    def du(self):
        print("in du")


server = socketserver.ThreadingTCPServer(("127.0.0.1", 9000), MyServer)
server.serve_forever()
