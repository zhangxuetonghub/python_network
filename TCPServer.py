#!/usr/bin/env python

from socket import *
from time import ctime

HOST = '127.0.0.1'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print("...connected from:",addr)

    while True:
        data = tcpCliSock.recv(BUFSIZE)
        print(type(data))
        if not data:
            break
        tcpCliSock.send(('[%s] %s' % (ctime(),data)).encode('utf-8'))

    tcpCliSock.close()
tcpSerSock.close()
