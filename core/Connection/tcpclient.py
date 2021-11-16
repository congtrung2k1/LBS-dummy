"""
=====================================================
|	TCP of user send location to server and receive dummy location
|
|	sendLocation(X: int, Y: int) -> list
|
=====================================================
"""


from socket import *

def sendLocation(X: int, Y: int, state: int) -> list:

	s = socket(AF_INET, SOCK_STREAM)
	s.connect(('127.0.0.1', 3117))

	loc = f'{state}-{str(X)}-{str(Y)}'
	s.send(loc.encode())
	loc = s.recv(1024).decode()
 
	s.close()

	return [int(loc.split('-')[0]), int(loc.split('-')[1])]
