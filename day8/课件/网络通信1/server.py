import socket

sk = socket.socket()  #拿到一个socket实例化对象
sk.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sk.bind(('127.0.0.1',9000))   # 一台电脑 65535 - > 操作系统
sk.listen()  # 监听
while True: # 无限的接电话
    conn,addr = sk.accept()   # 阻塞  三次握手完毕
    while True:   # 接到电话之后无限聊
        msg = input('>>>')
        conn.send(msg.encode('utf-8'))  # 发送数据
        if msg == 'q':break
        ret = conn.recv(1024).decode('utf-8')
        if ret == 'q':break
        print(ret)
    conn.close()
sk.close()