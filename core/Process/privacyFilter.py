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


# Check if user in new shape or not
def checkUserIn(x, y, topX, botX, topY, botY) -> bool:
    return topX <= x <= botX and topY <= y <= botY


# Privacy change from smaller to bigger
def addList(ggmap: object) -> None:
    dX = [0, 0, 1, 1, 0, 1, 2, 2, 2]
    dY = [0, 1, 0, 1, 2, 2, 0, 1, 2]

    uX = ggmap.userShape[0]
    uY = ggmap.userShape[1]
    c = ggmap.level - ggmap.lastl
    tempList = []

    for i in range((c + 1) * (c + 1) + 1):
        topX = uX + dX[i] - ggmap.level + 1
        botX = uX + dX[i]
        topY = uY + dY[i] - ggmap.level + 1
        botY = uY + dY[i]
        if checkInbound(topX):
            if checkInbound(topY):
                tempList.append(ggmap.getShape(botX, botY, ggmap.level))


# Privacy change from bigger to smaller
def minusList(ggmap: object) -> None:
    dX = [0, 0, 1, 1, 0, 1, 2, 2, 2]
    dY = [0, 1, 0, 1, 2, 2, 0, 1, 2]

    uX = ggmap.userShape[0]
    uY = ggmap.userShape[1]
    c = ggmap.level - ggmap.lastl
    tempList = []

    for i in range((c + 1) * (c + 1) + 1):
        topX = uX - dX[i] - ggmap.level + 1
        botX = uX - dX[i]
        topY = uY - dY[i] - ggmap.level + 1
        botY = uY - dY[i]
        if checkInbound(topX):
            if checkInbound(topY):
                tempList.append([botX, botY])


# Get new shape contain or overlapse the older
def privacyCheck(ggmap: object) -> bool:
    tempList = []
    if ggmap.level > ggmap.lastl:
        tempList = addList(ggmap)
    else:
        tempList = minusList(ggmap)

    tmpPrivList = []

    # User shape and percent of element in userShape
    tempUser = ggmap.getShape(ggmap.userShape)
    tempPerUser = percentObject(tempUser)

    for loc in tempList:
        tmp = ggmap.getShape(loc[0], loc[1], ggmap.level)
        tmpPer = percentObject(tmp)

        # Check for second Filter and third Filter with new shape
        check = 1
        total = 0.0
        for key in tempUser:
            total += abs(tmpPer[key] - tempUser[key])
            if abs(tmpPer[key] - tempPerUser[key]) > 0.060:
                check = 0
                break
        if check:
            tmpPrivList.append([total, loc])
        else:
            continue

    tmpPrivList = sorted(tmpPrivList, key=lambda x: x[0])
    if tmpPrivList != None:
        ggmap.dummyX = tmpPrivList[0][1][0]
        ggmap.dummyy = tmpPrivList[0][1][1]
        return True

    return False
