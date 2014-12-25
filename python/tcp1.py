# -*- coding:utf-8 -*-

import socket

# AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6
# SOCK_STREAM指定使用面向流的TCP协议
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("www.sina.com.cn",80))

# TCP连接创建的是双向通道，双方都可以同时给对方发数据。但是谁先发谁后发，怎么协调，要根据具体的协议来决定。
# 例如，HTTP协议规定客户端必须先发请求给服务器，服务器收到后才发数据给客户端。
s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

buffer = []
while True:
    # 每次 最多 接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = ''.join(buffer)

header, html = data.split('\r\n\r\n', 1)
print header
# 把接收的数据写入文件:
with open('../resource/sina.html', 'wb') as f:
    f.write(html)
    
# ***********************************************
# 服务器要给哪个客户端发数据，只要发到分配的端口就行。
# ***********************************************