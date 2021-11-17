"""
=====================================================
|   TCP of user receive dummy location to server and send location
|
|   ServerOn() -> None
|
=====================================================
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from socket import *

ggmap = 0

def Processing(state: int, x: int, y: int, lvl: int = 3) -> list:
    from Process.caseProcess import pipeIn
    global ggmap
    return pipeIn(state, x, y, lvl, ggmap)


def ServerOn() -> None:

    s = socket(AF_INET,SOCK_STREAM)
    s.bind(('', 3117))
    s.listen(1)

    print("[+] Server is on...")

    while True:
        ssub, addr = s.accept()
        loc = ssub.recv(1024).decode()

        print(f'Receiving {loc} from {addr[0]}:{addr[1]}')

        state = int(loc.split('-')[0])
        x = int(loc.split('-')[1])
        y = int(loc.split('-')[2])
        lvl = int(loc.split('-')[3])
        dum = Processing(state, x, y, lvl)

        loc = f'{dum[0]}-{dum[1]}'
        ssub.send(loc.encode())

        ssub.close()

    return None
    
#ServerOn()
