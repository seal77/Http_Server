"""
webframe
模拟网站后端应用行为

从httpserver接收具体请求
根据请求进行逻辑处理和数据处理
将需要的数据反馈给httpserver
"""

from socket import *
import json
from day9_19.webframe.settings import *
from threading import Thread
from multiprocessing import Process

class Application:
    def __init__(self):
        self.host = host
        self.port = port
        self.address = (self.host, self.port)
        self.create_socket()
        self.bind()

    def create_socket(self):
        self.socketfd = socket()
        self.socketfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, DEBUG)

    def bind(self):
        self.socketfd.bind(self.address)

    def start(self):
        self.socketfd.listen(5)
        print("application start at port %d"%self.port)
        while True:
            connfd, addr = self.socketfd.accept()
            client = Process(target=self.handle, args={connfd,})
            client.daemon = True
            client.start()

    def handle(self, connfd):
        request = connfd.recv(1024).decode()
        if not request:
            connfd.close()
            return
        request = json.loads(request)
        # print(data_dict)
        if request["method"] == "GET":
            if request["info"] == "/" or request["info"][-5:] == ".html":
                code, data = self.get_resource_data(STATIC_DIR + "/index.html")
                request = {"status": code, "data": data}
            else:
                code, data = self.get_resource_data(STATIC_DIR + request["info"])
                request = {"status": code, "data": data}
            connfd.send(json.dumps(request).encode())
            connfd.close()

        elif request["method"] == "POST":
            pass

    def get_resource_data(self, file_url):
        try:
            file = open(file_url, "rb")
            data = file.read()
            file.close()
            return "200", data.decode()
        except:
            file = open(STATIC_DIR + "/404.html", "rb")
            data = file.read()
            file.close()
            return "404", data.decode()


if __name__ == '__main__':
    app = Application()
    app.start()
