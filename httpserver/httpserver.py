"""
httpserver v3.0
获取http请求
解析http请求
将请求发送给WebFrame
从WebFrame接收反馈数据
将数据组织为Response格式发送给客户端
"""
from socket import *
import sys
from threading import Thread
from day9_19.httpserver.config import *

class HttpServer:
    def __init__(self):
        self.host = host
        self.port = port
        self.address = (host, port)
        #创建套接字
        self.create_socket()
        self.bind()

    def create_socket(self):
        self.socketfd = socket()
        self.socketfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, DEBUG)

    def bind(self):
        self.socketfd.bind(self.address)

    def serve_forever(self):
        self.socketfd.listen(5)
        print("Listen the port %d"%self.port)
        while True:
            connfd, addr = self.socketfd.accept()
            client = Thread(target=self.handle, args={connfd, })
            client.setDaemon(True)
            client.start()

    def handle(self, connfd):
        request = connfd.recv(4096).decode()
        print(request)

if __name__ == '__main__':
    httpserver = HttpServer()
    httpserver.serve_forever()