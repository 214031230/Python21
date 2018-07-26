#!/usr/bin/env python3
import socket
# client = socket.socket()
# client.connect(("127.0.0.1",9000))
# client.send("你好".encode("utf-8"))
# client.close()

#
# class QQClient:
#     def __init__(self,ip,port):
#         self.ip = ip
#         self.port = port
#
# client = socket.socket(type=socket.SOCK_DGRAM)
# while 1:
#     to_msg = input(">>>:")
#     client.sendto(to_msg.encode("utf-8"), ("127.0.0.1",9000))
#     msg, address = client.recvfrom(1024)
#     print("%s:%s" % (address, msg.decode("utf-8")))
# import struct
# client = socket.socket()
# client.connect(("127.0.0.1", 9000))
# data = "aadffsdfasdfsdfasdfasdfasfasdfasdfsadfasdfasdfsdafsaf"
# # 发送数据长度
# header = struct.pack("i", len(data))
# client.send(header)
# # 发送真实的数据
# client.send(data.encode("utf-8"))
# client.close()

# import struct
# import os
# import json
# client = socket.socket()
# client.connect(("127.0.0.1", 9000))
# file = "../day1.py"
# # 发送报头长度
# header_info = {"name": os.path.basename(file),
#                "size": os.path.getsize(file)}
# header_info_bytes = json.dumps(header_info)
# header_len = struct.pack("i", len(header_info_bytes))
# client.send(header_len)
# # 发送报头
# client.send(header_info_bytes.encode("utf-8"))
# # 发送真实的数据
# with open(file, "rb") as f:
#     for i in f:
#         client.send(i)
# client.close()
import socket
client = socket.socket()
client.connect(("127.0.0.1", 9000))
while 1:
    msg = input(">>>:").strip()
    if not msg:continue
    client.send(msg.encode("utf-8"))
