
import socket
import sys

port= 1212

if len(sys.argv)==2:
	port= int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('127.0.0.1', port))

s.listen(0)

s1 = s.accept()[0]
while True:

	data = s1.recv(65535)
	if not data: break
	print data


