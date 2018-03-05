"""
   date: 2018-03-05 23:50 
"""

__author__ = "WXGALY"

# 客户端
import socket
from datetime import datetime

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.send(data)
    print(datetime.now(), s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
