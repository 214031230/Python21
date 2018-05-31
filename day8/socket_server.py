#!/usr/bin/env python3
# 基于TCP协议的socket
# tcp是基于链接的，必须先启动服务端，然后再启动客户端去链接服务端
import socket
sk = socket.socket()
sk.bind(("127.0.0.1", 9000)) # 把地址绑定到套接字
sk.listen()   # 监听链接

con, address = sk.accept()  # 接受客户端链接
msg = con.recv(1024).decode("utf-8") # 接收客户端信息
print(msg)  # 打印客户端信息
con.send("client说：你好".encode("utf-8"))  # 向客户端发送信息

con.close() # 关闭客户端套接字
sk.close() # 关闭服务器套接字(可选)



# OSError: [WinError 10048] 通常每个套接字地址(协议/网络地址/端口)只允许使用一次。
import socket
sk = socket.socket()
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 就是它，在bind前加。端口重用
sk.bind(("127.0.0.1", 9000)) # 把地址绑定到套接字
sk.listen()   # 监听链接

con, address = sk.accept()  # 接受客户端链接
msg = con.recv(1024).decode("utf-8") # 接收客户端信息
print(msg)  # 打印客户端信息
con.send("client说：你好".encode("utf-8"))  # 向客户端发送信息

con.close() # 关闭客户端套接字
sk.close() # 关闭服务器套接字(可选)


# 基于UDP协议的socket的server
# udp是无链接的，启动服务之后可以直接接受消息，不需要提前建立链接
import socket
sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(("127.0.0.1", 9000))
msg, address = sk.recvfrom(1024)
print(address, msg.decode("utf-8"))
sk.sendto("你好".encode("utf-8"), address)
sk.close()

# QQ聊天
import socket
sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(("127.0.0.1", 9000))
while True:
    msg, address = sk.recvfrom(1024)
    print("%s[%s]:%s" % (address[0], address[1], msg.decode("utf-8")))
    to_msg = input(">>>:").strip()
    sk.sendto(to_msg.encode("utf-8"), address)

# 执行远程命令
import socket
import os
sk = socket.socket()
sk.bind(("127.0.0.1", 9000))
sk.listen()
while True:
    con, address = sk.accept()
    while True:
        msg = con.recv(1024).decode("utf-8")
        if msg.upper() == "Q":
            con.close()
            break
        ret = os.popen(msg).read()
        con.send(ret.encode("utf-8"))

# 粘包 发送方的缓存机制
from socket import *
ip_port = ('127.0.0.1', 8080)

tcp_socket_server = socket()
tcp_socket_server.bind(ip_port)
tcp_socket_server.listen()

conn, address = tcp_socket_server.accept()

data1 = conn.recv(10)
data2 = conn.recv(10)

print('----->', data1.decode('utf-8'))
print('----->', data2.decode('utf-8'))

conn.close()


# 粘包 接收方的缓存机制
# 接收方不及时接收缓冲区的包，造成多个包接收（客户端发送了一段数据，服务端只收了一小部分，服务端下次再收的时候还是从缓冲区拿上次遗留的数据，产生粘包）
#


# 黏包现象只发生在tcp协议中：
# 1.从表面上看，黏包问题主要是因为发送方和接收方的缓存机制、tcp协议面向流通信的特点。
# 2.实际上，主要还是因为接收方不知道消息之间的界限，不知道一次性提取多少字节的数据所造成的


# 解决粘包 初级版
# 解决一些小数据在连续发送时候的粘包问题
import socket
import struct
sk = socket.socket()
sk.bind(("127.0.0.1", 9000))
sk.listen()
con, addr = sk.accept()

header_len_bytes = con.recv(4)                          # 接受客户端发来的struct类型长度为4的数据
header_len = struct.unpack("i", header_len_bytes)[0]    # unpack获取真实数据长度
print(con.recv(header_len))                             # 接受真实数据

header_len_bytes = con.recv(4)
header_len = struct.unpack("i", header_len_bytes)[0]
print(con.recv(header_len))

con.close()
sk.close()

# 解决粘包，高级版（主要解决大文件的传输）
import socket
import struct
import json
sk = socket.socket()
sk.bind(("127.0.0.1", 9000))
sk.listen()
con,addr = sk.accept()

header_struct = con.recv(4)      # 接受报头长度struct类型
header_len = struct.unpack("i", header_struct)[0]     # 获取unpack后的报头长度

header_str = con.recv(header_len).decode("utf-8")   # 获取字符串格式报头
header = json.loads(header_str)    # 反序列化字符串，获取字典格式的报头

recv_size = 0
with open(header["name"], "wb") as f:   # 循环接受真实数据
    while recv_size < header["size"]:
        line = con.recv(1024)
        f.write(line)
        recv_size += len(line)

con.close()
sk.close()



