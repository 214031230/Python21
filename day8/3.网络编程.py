#!/usr/bin/env python3
# 为什么要有网络编程？
# 两个文件之间如何实现通信？
    #  基于文件通信--> 两个程序都在同一台机器上
    #  基于网络--> 两个不同机器上的程序


# 交换机是用于在一个局域网内的机器之间的通信
# 路由器是用于不同局域网之间的机器的通信
# arp协议：一台机器通过IP地址和交换机找到另一台机器的mac地址的过程

# ip地址能够找到网络中的唯一一台机器，临时的

# 如何在一台机器上精准的找到要和我通信的服务？？？
# 操作系统端口范围： 0-65535
# 在一台机器上 每一个服务所使用的端口不能相同

# 通过什么能够找到网络世界里的一个服务？ ip+端口
# 两种通信协议
# TCP：（Transmission Control Protocol）可靠的、面向连接的协议（eg:打电话）、传输效率低全双工通信（发送缓存&接收缓存）、面向字节流。使用TCP的应用：Web浏览器；电子邮件、文件传输程序。
# UDP：（User Datagram Protocol）不可靠的、无连接的服务，传输效率高（发送前时延小），一对一、一对多、多对一、多对多、面向报文，尽最大努力服务，无拥塞控制。使用UDP的应用：域名系统 (DNS)；视频流；IP语音(VoIP)


# 基于TCP协议的socket
# import socket
# sk = socket.socket()
# sk.bind(("127.0.0.1", 9000))
# sk.listen()
#
# con, address = sk.accept()
# msg = con.recv(1024)
# print(msg)
# con.send("你好".encode("utf-8"))
#
# con.close()
# sk.close()



















