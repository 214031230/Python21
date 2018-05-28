import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1',8899))
while True:
    msg,addr = sk.recvfrom(1024)
    print(addr,msg.decode('utf-8'))
    inp = input(">>>")
    sk.sendto(inp.encode('utf-8'),addr)
sk.close()