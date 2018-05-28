import socket
sk = socket.socket()
sk.connect(('127.0.0.1',9000))
while True:
    ret = sk.recv(1024).decode('utf-8')  # 接收一个数据
    if ret == 'q':break
    print(ret)
    msg = input('>>>')
    sk.send(msg.encode('utf-8'))
    if msg == 'q':break
sk.close()


