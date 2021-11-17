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
        if ggmap.prevDummyX == -1:
                ggmap.fourthList = ggmap.thirdList
                return None

        lim = len(ggmap.thirdList) // 3
        tmpRange = 19602

        for i in range(lim):
                x = abs(ggmap.thirdList[i][0] - ggmap.prevDummyX)
                y = abs(ggmap.thirdList[i][1] - ggmap.prevDummyY)
                if x**x + y**y < tmpRange:
                        tmpRange = x**x + y**y
                        ggmap.fourthList = ggmap.thirdList[i]

        #print(tmpRange)
        #print(ggmap.fourList)

        return None
