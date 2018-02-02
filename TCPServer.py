#!/usr/bin/env python
"""
伪代码
	ss = socket()					# 创建服务器套接字
	ss.bind()					    # 套接字与地址绑定
	ss.listen()					  # 监听连接
	inf_loop:					    # 服务器无线循环
		cs = ss.accept()			# 接受客户端连接
		comm_loop:				  # 通信循环
			cs.recv()/cs.send()		# 对话（接收/发送）
		cs.colose()				  # 关闭客户端套接字
	ss.close()					  # 关闭服务端套接字（可选）
  
  所有的套接字都是通过使用socket.socket()函数来创建的。
	因为服务器需要占用一个端口并等待客户端的请求，所以它们必须绑定到一个本地地址。因为TCP是一种面向连接的通信系统，所以在TCP服务器开始操作之前，必须安装一些基础设施。特别的，TCP服务器必须监听（传入）的连接。一旦这个安装过程完成后，服务器就可以开始它的无线循环。
	调用accept（）函数之后，就开始了一个简单的（单线程）服务器，它会等待客户端的连接。默认情况下，accept（）是阻塞的，这意味着执行将被暂停，直到一个连接到达。另外，套接字确实也支持非阻塞模式，可以参考文档或操作系统教材，以了解有关为什么以及如何使用非阻塞套接字的更多细节。
	一旦服务器接受了一个连接，就会返回（利用accept（））一个独立的客户端套接字，用来与即将到来的消息进行交换。使用新的客户端套接字类似与将客户的电话切换给客服代表。当一个客户电话最后接近来时，主要的总机接线员会接到这个电话，并使用另一条线路将这个电话转接给合适的人来处理客户的需求。
	这将能够空出主线（原始服务器套接字），以便接线员可以继续等待新的电话（客户请求），而此时客户及其连接的客服代表能够进行他们自己的谈话。同样的，当一个传入的请求到达时，服务器会创建一个新的通信端口来直接与客户端进行通信，再次空出主要的端口，以便能够接受新的客户端连接。
	一旦创建了临时套接字，通信就可以开始，通过使用这个新的套接字，客户端与服务器就可以开始参与发送和接收的对话中，直到连接终止。当一方关闭连接或者向对方发送一个空字符串时，通常就会关闭连接。
	在代码中，一个客户端连接关闭之后，服务器就会等待另一个客户端连接。最后一行代码是可选的，在这里关闭了服务器套接字。其实，这种情况永远也许不会碰到，因为服务器应该在一个无限循环中运行。在示例中这行代码用来提醒读者，当服务器实现一个只能的退出方案时，建议调用close（）方法。
	例如，当一个处理程序检测到一些外部条件时，服务器就应该关闭。在这些情况下，应该调用一个close（）方法。
  """
  
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
