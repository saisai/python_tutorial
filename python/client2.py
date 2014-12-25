# -*- coding:utf-8 -*-
import socket

# ***********************************************
# 此外，服务器绑定UDP端口和TCP端口互不冲突
# 也就是说，UDP的9999端口与TCP的9999端口可以各自绑定。
# ***********************************************

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in ['Michael', 'Tracy', 'Sarah']:
	# 发送数据:
	s.sendto(data, ('127.0.0.1', 9999))
	# 接收数据:
	print s.recv(1024)
s.close()

# 直接sendto和recv