"""
=====================================================
|   TCP of user receive dummy location to server and send location
|
|   ServerOn()
|
=====================================================
"""


from socket import *

def Processing(X: int, Y: int) -> list:
    return [X, Y]


def ServerOn() -> None:
    
    s = socket(AF_INET,SOCK_STREAM)
    s.bind(('', 3117))
    s.listen(1)
    
    print("[+] Server is on...")

    while True:
        ssub, addr = s.accept()
        loc = ssub.recv(1024).decode()

        print(f'Receiving {loc} from {addr[0]}:{addr[1]}')

        dum = Processing(int(loc.split('-')[0]), int(loc.split('-')[1]))

        loc = f'{dum[0]}-{dum[1]}'
        ssub.send(loc.encode())

        ssub.close()

    return None