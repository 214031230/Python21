#_*_coding:utf-8_*_
import socket
BUFSIZE=1024
ip_port=('127.0.0.1',8080)

s=socket.socket()
res=s.connect_ex(ip_port)

s.send('hello'.encode('utf-8'))
s.send('egg'.encode('utf-8'))
s.close()