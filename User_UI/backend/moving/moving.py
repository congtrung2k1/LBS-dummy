"""
=====================================================
|	Get next random location for user
|
|	movingLocation(coor: list) -> list
|
=====================================================
"""

import random

def checkCollision(x: int, y: int):
    if 0 < x < 100 and 0 < y < 100:
        return True
    return False

def movingLocation(coor: list) -> list:
    coX = [-1, -1, -1, 0, 0, 1, 1, 1]
    coY = [-1, 0, 1, -1, 1, -1, 0, 1]

    while True:
        tmp = random.randrange(0, 7)

        if checkCollision(coor[0] + coX[tmp], coor[1] + coY[tmp]):
            return [coor[0] + coX[tmp], coor[1] + coY[tmp]]
