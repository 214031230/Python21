#!/usr/bin/env python3
# 基于TCP协议的socket的client
import socket
sk = socket.socket()   # 创建客户套接字
sk.connect(("127.0.0.1", 9000))  # 尝试连接服务器
sk.send("server说：你好".encode("utf-8"))  # 给server发送消息
msg = sk.recv(1024).decode("utf-8")  # 接受server发来的消息
print(msg)
sk.close() # 关闭客户套接字

# 基于UDP协议的socket的client
import socket
sk = socket.socket(type=socket.SOCK_DGRAM)
sk.sendto("你好".encode("utf-8"), ("127.0.0.1", 9000))
msg, address = sk.recvfrom(1024)
print(address, msg.decode("utf-8"))
sk.close()

# QQ聊天
import socket
sk = socket.socket(type=socket.SOCK_DGRAM)
while True:
    msg = input(">>>:")
    sk.sendto(msg.encode("utf-8"), ("127.0.0.1", 9000))
    msg, address = sk.recvfrom(1024)
    print("%s[%s]:%s" % (address[0], address[1], msg.decode("utf-8")))

# 执行远程命令
import socket
sk = socket.socket()
sk.connect(("127.0.0.1", 9000))
while True:
    cmd = input(">>>:")
    if not cmd:continue
    sk.send(cmd.encode("utf-8"))
    if cmd.upper() == "Q":break
    ret = sk.recv(1024).decode("utf-8")
    print(ret)
print("1")
sk.close()

# 粘包  发送方的缓存机制
# 发送端需要等缓冲区满才发送出去，造成粘包（发送数据时间间隔很短，数据了很小，会合到一起，产生粘包）
import socket
BUFSIZE = 1024
ip_port = ('127.0.0.1', 8080)

s = socket.socket()
s.connect(ip_port)


s.send('hello'.encode('utf-8'))
s.send('egg'.encode('utf-8'))
s.close()

# 粘包  接受方的缓存及时
# 接收方不及时接收缓冲区的包，造成多个包接收（客户端发送了一段数据，服务端只收了一小部分，服务端下次再收的时候还是从缓冲区拿上次遗留的数据，产生粘包）
# import socket
# BUFSIZE = 1024
# ip_port = ('127.0.0.1', 8080)
#
# s = socket.socket()
# s.connect(ip_port)
#
#
# s.send('hello'.encode('utf-8'))
# s.send('egg'.encode('utf-8'))


# 解决粘包 初级版
# 解决一些小数据在连续发送时候的粘包问题
import socket
import struct
sk = socket.socket()
sk.connect(("127.0.0.1", 9000))


data1 = "aaaaaaaa"
header1 = struct.pack("i", len(data1))  # 使用struct把真实数据长度固定4的bytes类型
sk.send(header1)                        # 发送长度为4的bytes类型
sk.send(data1.encode("utf-8"))          # 发送真实的数据

data2 = "bbbbbbbb"
header2 = struct.pack("i", len(data2))
sk.send(header2)
sk.send(data2.encode("utf-8"))

sk.close()


# 解决粘包，高级版（主要解决大文件的传输）
import socket
import json
import struct
import os

sk = socket.socket()
sk.connect(("127.0.0.1", 9000))

file_path = r"C:\Users\lanpa\Desktop\Python自动化21期\Python21\day8\课件\4.包.py"
header = {"name": os.path.basename(file_path),
          "size": os.path.getsize(file_path)}

header_json = json.dumps(header)    # 把字典转换成字符串格式
header_struck = struct.pack("i", len(header_json))  # 把字符串长度转换成struck类型固定长度为4的bytes类型

sk.send(header_struck)      # 发送header长度
sk.send(header_json.encode("utf-8"))        # 发送报头信息

with open(file_path, "rb") as f:    # 循环发送真实的数据
    for line in f:
        sk.send(line)