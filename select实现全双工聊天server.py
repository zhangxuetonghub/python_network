# Echo server program
import socket
import sys
import select

HOST = None  # Symbolic name meaning all available interfaces
PORT = 50007  # Arbitrary non-privileged port
s = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC,
                              socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except OSError as msg:
        s = None
        continue
    try:
        s.bind(sa)
        s.listen(1)
    except OSError as msg:
        s.close()
        s = None
        continue
    break
if s is None:
    print('could not open socket')
    sys.exit(1)

INPUT = [s, sys.stdin]
while True:
    print('waiting for connection...')
    tcpCliSock, addr = s.accept()
    print('...connected from:', addr)
    INPUT.append(tcpCliSock)  # 将服务套接字加入到input列表中
    while True:
        readyInput, readyOutput, readyException = select.select(INPUT, [],
                                                                [])  # 从input中选择，轮流处理client的请求连接（tcpSerSock），client发送来的消息(tcpCliSock)，及服务器端的发送消息(stdin)
        for indata in readyInput:
            if indata == tcpCliSock:  # 处理client发送来的消息
                data = tcpCliSock.recv(10240)
                txt = data.decode('utf-8')
                print(' ' * 30, txt)
                if txt == '88':
                    INPUT.remove(tcpCliSock)
                    break
            else:  # 处理服务器端的发送消息
                txt = input('>')
                data = txt.encode('utf-8')
                if txt == '88':
                    tcpCliSock.send(data)
                    INPUT.remove(tcpCliSock)
                    break
                tcpCliSock.send(data)
        if txt == '88':
            break
    tcpCliSock.close()
tcpSerSock.close()
