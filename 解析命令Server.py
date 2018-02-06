# Echo server program
import socket
import sys
import time
import os

HOST = None               # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
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
conn, addr = s.accept()
with conn:
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data: break
        txt = data.decode('utf-8')
        if txt == 'date':
            conn.send(time.ctime().encode('utf-8'))
        elif txt == 'os':
            conn.send(os.name.encode('utf-8'))
        elif txt == 'ls' :
            conn.send(repr(os.listdir(os.curdir)).encode('utf-8'))
        elif txt[0:2] == 'ls' and txt[2] == ' ':
            dirctory = txt[2:].strip()
            conn.send(repr(os.listdir(dirctory)).encode('utf-8'))
        else:
            conn.send(b'command not found!')
            continue
    conn.close()
s.close()
