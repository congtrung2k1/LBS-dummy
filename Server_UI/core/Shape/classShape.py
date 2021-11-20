"""
=================================================================
|    Class hold information of all table, calculating all shape
|
|    Shape(userX: int, userY: int, level: int = 3)
|    getShape(self, x: int, y: int, level: int = 3) -> dict
|    placeUserShape(self) -> None
|    changeLevel(self, level: int) -> bool
|    changeUserLocation(self, x: int, y: int) -> None
|
=================================================================
"""
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Object.randomObject import getRandomValue, zeroObject
from Object.operatorObject import addObject, minusObject


class Shape():
    def __init__ (self, userX: int, userY: int, level: int = 3):
        self.table = []
        self.maxN = 100
        self.maxM = 100

        # Information of user: x, y, shape, location of shape
        self.userX = userX
        self.userY = userY
        self.level = level
        self.userShape = []
        self.userShapeBotX, self.userShapeBotY = 0, 0

        # Dummy location
        self.dummyX = -1
        self.dummyY = -1
        self.prevDummyX = -1
        self.prevDummyY = -1


        # Shape Filter
        self.firstList = []
        self.secondList = []
        self.thirdList = []
        self.fourthList = []

        # Saved state
        # [ [X,Y], [dummyX,dummyY], level, [userShapeBotX, userShapeBotY] ]
        self.memorized = []

        # Initialize the map
        self.initTable()
        self.calcAllShape()
        self.placeUserShape()


    # Create the table with random object
    def initTable(self) -> None:
        # row 0
        tmp = [zeroObject() for i in range(self.maxM)]
        self.table.append(tmp)

        for i in range(1, self.maxN):
            tmp = []

            # column 0
            tmp.append(zeroObject())

            for j in range(1, self.maxM):
                tmp.append(getRandomValue())

            self.table.append(tmp)


    # Calculate all shape inside table
    def calcAllShape(self) -> None:

        # [i,j] = [i,j] + [i - 1, j] + [i, j - 1] - [i - 1, j - 1]

        for i in range(1, self.maxN):
            for j in range(1, self.maxM):
                tmp = self.table[i][j]
                tmp = addObject(tmp, self.table[i-1][j])
                tmp = addObject(tmp, self.table[i][j-1])
                self.table[i][j] = minusObject(tmp, self.table[i-1][j-1])

        return None


    # Get shape with level
    def getShape(self, x: int, y: int, level: int = 3) -> dict:
        # Check inside
        if x >= self.maxN | x - level < 0 | y >= self.maxM | y - level < 0:
            return zeroObject()

        # [i,j] = [i,j] - [i - lvl, j] - [i, j - lvl] + [i - lvl, j - lvl]
        ret = self.table[x][y]
        ret = minusObject(ret, self.table[x - level][y])
        ret = minusObject(ret, self.table[x][y - level])
        ret = addObject(ret, self.table[x - level][y - level])

        return ret


    # setting up the shape of user
    def placeUserShape(self) -> None:
        # number of cells in shape (for random choice)
        c = self.level ** 2 - 1

        # list of remaining choice
        tmp = [i for i in range(c + 1)]
        while 1:
            # random choice a cell in remaining choice
            import random
            r = tmp[random.randint(0, len(tmp) - 1)]

            a = r // self.level        # get x of row in user shape
            b = r % self.level        # get y of column in user shape

            # Check if the shape is in the table
            if 0 < self.userX - a and self.userX + (self.level - 1 - a) < self.maxN \
                and 0 < self.userY - b and self.userY + (self.level - 1 - b) < self.maxM:
                break

            # remove the cell order choice if not satisfied
            tmp.remove(r)

        self.userShapeBotX = self.userX + (self.level - 1 - a)
        self.userShapeBotY = self.userY + (self.level - 1 - b)

        self.userShape = self.getShape(self.userShapeBotX, self.userShapeBotY, self.level)


    # Privacy level of user change
    def changeLevel(self, level: int) -> bool:
        self.level = level

        for pair in self.memorized:
            # Check the privacy level first
            if pair[2] == self.level:
                # Return to the previous position
                if pair[0] == [self.userX, self.userY]:
                    self.dummyX = pair[1][0]
                    self.dummyY = pair[1][1]
                    self.userShapeBotX = pair[3][0]
                    self.userShapeBotY = pair[3][1]
                    return True

                else:
                    # Return to the previous userShape
                    lvl, tmpx, tmpy = pair[2], pair[3][0], pair[3][1]

                    if tmpx - lvl + 1 <= self.userX <= tmpx and tmpy - lvl + 1 <= self.userY <= tmpy:
                        self.dummyX = pair[1][0]
                        self.dummyY = pair[1][1]
                        self.userShapeBotX = tmpx
                        self.userShapeBotY = tmpy
                        return True

        # if the position does not have any data in database, create new
        self.placeUserShape()
        return False


    # Location of user change
    def changeUserLocation(self, x: int, y: int) -> None:
        self.userX, self.userY = x, y



# Debug only
# if __name__ == "__main__":
#     ggmap = Shape(5, 5)

#     print(ggmap.userShapeTopX, ggmap.userShapeTopY, ggmap.userShapeBotX, ggmap.userShapeBotY)
#     print(ggmap.userShape)

#     # ggmap.changeUserLocation(9, 9)
#     # print(ggmap.userShapeTopX, ggmap.userShapeTopY, ggmap.userShapeBotX, ggmap.userShapeBotY)
#     # print(ggmap.userShape)

#     for i in range(1, ggmap.maxN):
#         for j in range(1, ggmap.maxM):
#             print(i, j, ggmap.table[i][j])
#             # input()

