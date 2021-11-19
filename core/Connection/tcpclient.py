"""
=====================================================
|   TCP of user send location to server and receive dummy location
|
|   sendLocation(X: int, Y: int) -> list    # or Str
|
=====================================================
"""


from socket import *

def sendLocation(state: int, X: int, Y: int, level: int) -> list:   # or Str

        s = socket(AF_INET, SOCK_STREAM)
        try:
            s.connect(('127.0.0.1', 3117))
        except:
            return "Sorry\nSomethings went wrong.\nPlease restart!"

        loc = f'{state}-{str(X)}-{str(Y)}-{level}'
        s.send(loc.encode())
        loc = s.recv(1024).decode()

        s.close()

        if loc == '-1--1':
            return "Sorry\nSomethings went wrong.\nPlease restart!"

        return [int(loc.split('-')[0]), int(loc.split('-')[1])]
