# Echo server program
import socket
import sys

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
conn, addr = s.accept()
with conn:
    print('Connected by', addr)
    while True:
        data = conn.recv(10240)
        if not data: break
        txtin = data.decode('utf-8')
        print(txtin)
        txtout = input('>')
        if not txtout: break
        conn.sendall(txtout.encode('utf-8'))
    conn.close()
    print('byebye')
s.close()
