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

ggmap = None

def pipeIn(ggmap, state: int, x: int, y: int, lvl: int = 3) -> list:
    from Process.caseProcess import pipeIn
    return pipeIn(state, x, y, lvl, ggmap)


def ServerOn() -> None:
    global ggmap

    s = socket(AF_INET,SOCK_STREAM)
    s.bind(('', 3117))
    s.listen(1)

    print("[+] Server is on...")

    while True:
        ssub, addr = s.accept()
        loc = ssub.recv(1024).decode()

        #print(f'Receiving {loc} from {addr[0]}:{addr[1]}')

        state = int(loc.split('-')[0])
        x = int(loc.split('-')[1])
        y = int(loc.split('-')[2])
        level = int(loc.split('-')[3])
        ret = pipeIn(ggmap, state, x, y, level)

        if state == 0:
            ggmap = ret[0]
            dum = ret[1]
        else:
            dum = ret

        loc = f'{dum[0]}-{dum[1]}'
        ssub.send(loc.encode())
        ssub.close()

        if ret == [-1, -1]:
            continue

        #self.updateLocation.emit(f'{x}-{y}-{dum[0]}-{dum[1]}')
        #self.updateMap.emit(self.ggmap)

    s.close()

    return None

#ServerOn()
