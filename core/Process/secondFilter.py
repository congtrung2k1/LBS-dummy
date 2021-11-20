"""
=================================================================
|    Second filter, get all the shape which have +-6% of object like userShape
|
|    secondFilter(ggmap: object) -> None:
|
=================================================================
"""

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Object.operatorObject import percentObject

def secondFilter(ggmap: object) -> None:
    temp = percentObject(ggmap.userShape)
    ggmap.secondList.clear()

    for loc in ggmap.firstList:
        tmp = ggmap.getShape(loc[0], loc[1], ggmap.level)
        tmpPer = percentObject(tmp)

        check = 1
        for key in temp:
            if abs(tmpPer[key] - temp[key]) > 0.060:
                check = 0
                break
        if check:
            ggmap.secondList.append(loc)
