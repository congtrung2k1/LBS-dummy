"""
=================================================================
|    Get new shape, which changed privacy, overlapse with the older.
|
|    privacyCheck(ggmap: object) -> bool
|
=================================================================
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.Object.operatorObject import percentObject

# Check if the position is in table or not
def checkInbound(value: int) -> bool:
    maxValue = 100
    return 0 < value < maxValue

# Check if user is in new shape or not
def checkUserIn(x: int, y: int, topX: int, botX: int, topY: int, botY: int):
    return topX <= x <= botX and topY <= y <= botY


# Get new dummy shape contain the old dummy shape
def getNewDummyShapeList(ggmap: object) -> list:
    dX = [0, 0, 1, 1, 0, 1, 2, 2, 2]
    dY = [0, 1, 0, 1, 2, 2, 0, 1, 2]

    sign = 1
    if ggmap.level - ggmap.lastl < 0: sign = -1

    uX = ggmap.dummyX
    uY = ggmap.dummyY

    tempList = []
    for i in range((abs(ggmap.level - ggmap.lastl) + 1)**2):
        topX = uX + sign * dX[i] - ggmap.level + 1
        botX = uX + sign * dX[i]
        topY = uY + sign * dY[i] - ggmap.level + 1
        botY = uY + sign * dY[i]
        if checkInbound(topX):
            if checkInbound(botX):
                if checkInbound(topY):
                    if checkInbound(botY):
                        tempList.append([botX, botY])
    return tempList


# Get new user shape contain the old user shape
def getNewUserShapeList(ggmap: object) -> list:
    dX = [0, 0, 1, 1, 0, 1, 2, 2, 2]
    dY = [0, 1, 0, 1, 2, 2, 0, 1, 2]

    sign = 1
    if ggmap.level - ggmap.lastl < 0: sign = -1

    uX = ggmap.userShapeBotX
    uY = ggmap.userShapeBotY

    tempList = []
    for i in range((abs(ggmap.level - ggmap.lastl) + 1)**2):
        topX = uX + sign * dX[i] - ggmap.level + 1
        botX = uX + sign * dX[i]
        topY = uY + sign * dY[i] - ggmap.level + 1
        botY = uY + sign * dY[i]
        if checkInbound(topX):
            if checkInbound(botX):
                if checkInbound(topY):
                    if checkInbound(botY):
                        if checkUserIn(ggmap.userX, ggmap.userY, topX, botX, topY, botY):
                            tempList.append([botX, botY])
    return tempList


# Get new shape contain or overlapse the older
def privacyCheck(ggmap: object) -> bool:
    tempList = getNewDummyShapeList(ggmap)
    userList = getNewUserShapeList(ggmap)

    tmpPrivList = []

    # With each user shape, find shape have less different percent.
    for each in userList:
        tempPerUser = percentObject(ggmap.getShape(each[0], each[1], ggmap.level))

        for loc in tempList:
            tmp = ggmap.getShape(loc[0], loc[1], ggmap.level)
            tmpPer = percentObject(tmp)

            # Check for second Filter and third Filter with new shape
            check = 1
            total = 0.0
            for key in ggmap.userShape:
                total += abs(tmpPer[key] - tempPerUser[key])
                if abs(tmpPer[key] - tempPerUser[key]) > 0.060:
                    check = 0
                    break
            if check:
                tmpPrivList.append([total, loc, each])
            else:
                continue

    tmpPrivList = sorted(tmpPrivList, key=lambda x: x[0])
    if len(tmpPrivList) != 0:
        ggmap.userShapeBotX = tmpPrivList[0][2][0]
        ggmap.userShapeBotY = tmpPrivList[0][2][1]
        ggmap.userShape = ggmap.getShape(ggmap.userShapeBotX, ggmap.userShapeBotY, ggmap.level)
        ggmap.dummyX = tmpPrivList[0][1][0]
        ggmap.dummyY = tmpPrivList[0][1][1]
        return True

    return False
