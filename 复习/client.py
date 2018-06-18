#!/usr/bin/env python3
import socket
client = socket.socket()
client.connect(("127.0.0.1", 9001))
while 1:
    msg = input(">>>：").encode("utf-8")
    if not msg:continue
    client.send(msg)
    if msg.lower() == "q":break
client.close()