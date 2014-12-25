import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(("127.0.0.1",9999))

s.send("laozhikun")

# buffer = []
# while True:
msg = s.recv(1024)
	# if data:
	# 	buffer.append(data)
	# else:
	# 	break

# msg = "".join(buffer)

s.send("break")
s.close()
print msg