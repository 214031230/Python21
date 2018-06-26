#!/usr/bin/env python3
import socket
server = socket.socket()
server.bind(("127.0.0.1", 9000))
server.listen()
print("启动server...")
while True:
    conn,addr = server.accept()
    print(conn, addr)
    while True:
        msg = conn.recv(1024).decode("utf-8")
        print(msg)
        conn.send(b"ok")