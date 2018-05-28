import socket
sk = socket.socket(type=socket.SOCK_DGRAM)
while True:
    inp = input('>>>')
    sk.sendto(inp.encode('utf-8'),('127.0.0.1',8899))
    msg,addr = sk.recvfrom(1024)   # 阻塞
    print(msg.decode('utf-8'))
sk.close()