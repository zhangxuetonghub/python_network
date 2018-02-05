#!/usr/bin/env python
from socketserver import TCPServer as TCP, StreamRequestHandler as SRH
from time import ctime

HOST = '127.0.0.1'
PORT = 12123
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
    def handle(self):
        print('...connected from :',self.client_address)
        self.wfile.write(bytes('[%s] %s' % (ctime(), self.rfile.readline().decode('utf-8')),'utf-8'))

tcpServ = TCP(ADDR, MyRequestHandler)
print('waiting for connection...')
tcpServ.serve_forever()
