#!/usr/bin/env python3
import socket
client = socket.socket()
client.connect(("127.0.0.1", 9000))
while True:
    msg = input(">>>：").encode("utf-8")
    if not msg:continue
    client.send(msg)
    if msg == "q":
        break
client.close()
