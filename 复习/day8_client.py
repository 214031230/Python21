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
# import socket
# client = socket.socket()
# client.connect(("127.0.0.1", 9000))
#
# while 1:
#     msg = input(">>>:").encode("utf-8")
#     client.send(msg)
# import socket
# client = socket.socket(type=socket.SOCK_DGRAM)
# client.sendto(b"nihao",("127.0.0.1", 9000))

