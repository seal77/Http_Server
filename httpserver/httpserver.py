"""
httpserver v3.0
获取http请求
解析http请求
将请求发送给WebFrame
从WebFrame接收反馈数据
将数据组织为Response格式发送给客户端
"""
import re
import json
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
        # connfd.send(b"OK")
        pattern = r"(?P<method>[A-Z]+)\s+(?P<info>/\S*)"
        try:
            env = re.match(pattern, request).groupdict()
        except Exception as e:
            print(e)
            connfd.close()
            return
        # print(env)
        response = connect_frame(env)
        # print(response)
        if response:
            self.send_response(response, connfd)

    def send_response(self, response, connfd):
        data = ""
        if not response:
            return
        if response["status"] == "200":
            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type:text/html\r\n"
            data += "\r\n"
            data += response["data"]
        elif response["status"] == "404":
            data = "HTTP/1.1 404 Not Found\r\n"
            data += "Content-Type:text/html\r\n"
            data += "\r\n"
            data += response["data"]
        elif response["status"] == "500":
            pass
        connfd.send(data.encode())

def connect_frame(env):
    s = socket()
    address = (frame_ip, frame_port)
    try:
        s.connect(address)
    except:
        return
    data = json.dumps(env)
    s.send(data.encode())
    data = s.recv(1024*1024*10).decode()
    return json.loads(data)


if __name__ == '__main__':
    httpserver = HttpServer()
    httpserver.serve_forever()