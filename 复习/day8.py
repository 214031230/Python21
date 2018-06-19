#!/usr/bin/env python3
# import time
# while True:
#     msg = input(">>>:")
#     try:
#         while 1:
#             if msg == "q":
#                 break
#             print(int(msg))
#             time.sleep(2)
#
#     except ValueError:
#         print("你输入的不是数字")
#     except Exception as e:
#         print(e)
#     else:
#         print("没有异常执行else")
#     finally:
#         print("不管有没有异常都执行finally")
import socket
# server = socket.socket()
#
# server.listen()
#
# while 1:
#     conn,addr = server.accept()
#     while 1:
#         msg = conn.recv(1024).decode("utf-8")
#         print(msg)
#     conn.close()
# server = socket.socket(type=socket.SOCK_DGRAM)
# server.bind(("127.0.0.1", 9000))
# msg,addr = server.recvfrom(1024)
# print(msg.decode("utf-8"))




