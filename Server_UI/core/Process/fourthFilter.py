"""
=================================================================
|	Four filter, find the shape has closet distance to last dummy location
|
|	fourthFilter(ggmap: object) -> None:
|
=================================================================
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Object.operatorObject import percentObject

def fourthFilter(ggmap: object) -> None:
        ggmap.fourthList.clear()

        if ggmap.prevDummyX == -1:
                ggmap.fourthList = ggmap.thirdList
                return None

        lim = len(ggmap.thirdList) // 3
        tmpRange = 19602

        for i in range(lim):
                x = abs(ggmap.thirdList[i][0] - ggmap.prevDummyX)
                y = abs(ggmap.thirdList[i][1] - ggmap.prevDummyY)
                if x**2 + y**2 < tmpRange:
                        tmpRange = x**2 + y**2
                        ggmap.fourthList = ggmap.thirdList[i]

        #print(tmpRange)
        #print(ggmap.fourthList)

        return None
