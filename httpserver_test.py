#!/usr/bin/env python3
import json
from socket import *

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
s.bind(("0.0.0.0", 8080))
s.listen(3)

c, addr = s.accept()
data = c.recv(1024).decode()
print(data)
c.send(json.dumps({"status":"200","data":"http test"}).encode())