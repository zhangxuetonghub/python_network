#!/usr/bin/env python
from socket import *
from time import ctime

HOST = '127.0.0.1'
PORT = 12123
BUFSIZE = 1024
ADDR = (HOST,PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print("waiting for message...")
    data, addr = udpSerSock.recvfrom(BUFSIZE)
    udpSerSock.sendto(bytes('[%s] %s' % (ctime(),data.decode('utf-8')),'utf-8'),addr)
    print("...received form and returned to :",addr)
udpSerSock.close()
