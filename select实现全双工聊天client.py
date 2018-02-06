# Echo client program
import socket
import sys
import select

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

INPUT = [s, sys.stdin]

while True:
    readyInput, readyOutput, readyException = select.select(INPUT, [], [])
    for indata in readyInput:
        if indata == s:
            data = s.recv(10240)
            txt = data.decode('utf-8')
            print(' ' * 30, txt)
            if txt == '88':
                break
        else:
            txt = input('>')
            data = txt.encode('utf-8')
            if txt == '88':
                s.send(data)
                break
            s.send(data)
    if txt == '88':
        break
s.close()
