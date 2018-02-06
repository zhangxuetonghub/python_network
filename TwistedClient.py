#!/usr/bin/env python
from twisted.internet import protocol, reactor

HOST = '127.0.0.1'
PORT = 12123

class TSClntProtocol(protocol.Protocol):
    def sendData(self):
        data = input('>')
        if data:
            print("..sending %s..." % data)
            self.transport.write(data.encode())
        else:
            self.transport.loseConnection()

    def connectionMade(self):
        self.sendData()
    def dataReceived(self, data):
        print(data.decode())
        self.sendData()

class TSClntFactory(protocol.ClientFactory):
    protocol = TSClntProtocol
    clientConnectionLost = clientConnectionFailed = lambda self, connector, reason: reactor.stop()

reactor.connectTCP(HOST, PORT, TSClntFactory())
reactor.run()
