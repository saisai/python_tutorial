import socket
import threading
import time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(("127.0.0.1",9999))

s.listen(5)
print "wating for connection...."

def tcplink(sock,addr):
	print "Accept new connection from %s:%s"%(addr)
	sock.send("welcome!")
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if data == "break" or not data:
			break
		sock.send("Hello ,%s"%data)
	sock.close()
	print "connection from %s:%s closed."%addr

while True:
	sock,addr = s.accept()
	print "addr",addr
	t = threading.Thread(target=tcplink, args=(sock, addr))
	t.start()


