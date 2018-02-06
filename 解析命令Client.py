# Echo client program
import socket
import sys

HOST = '127.0.0.1'    # The remote host
PORT = 50007              # The same port as used by the server
s = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except OSError as msg:
        s = None
        continue
    try:
        s.connect(sa)
    except OSError as msg:
        s.close()
        s = None
        continue
    break
if s is None:
    print('could not open socket')
    sys.exit(1)

with s:
    while True:
        cmd = input('cmd:')
        if not cmd:
            break
        s.sendall(cmd.encode('utf-8'))
        data = s.recv(10240)
        print( data.decode('utf-8'))
    s.close()
