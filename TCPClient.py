#!/usr/bin/env python

from socket import *

HOST = '127.0.0.1'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)
print(tcpCliSock.proto)

while True:
    data = input('>')
    if not data:
        break
    c = tcpCliSock.send(data.encode('utf-8'))
    print(c)
    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        break
    print(data.decode('utf-8'))

tcpCliSock.close()
