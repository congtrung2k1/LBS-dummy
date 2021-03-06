"""
=================================================================
|	Third filter, sort with increase total different percent
|
|	secondFilter(ggmap: object) -> None:
|
=================================================================
"""

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.Object.operatorObject import percentObject

def thirdFilter(ggmap: object) -> None:
        tmpThirdlist = []
        ggmap.thirdList.clear()

        tempUser = percentObject(ggmap.userShape)

        for loc in ggmap.secondList:
                x = abs(ggmap.userX - loc[0])
                y = abs(ggmap.userY - loc[1])
                if x**2 + y**2 < 70:
                    continue

                tmp = ggmap.getShape(loc[0], loc[1], ggmap.level)
                tmpPer = percentObject(tmp)

                total = 0.0
                for key in tempUser:
                        total += abs(tmpPer[key] - tempUser[key])
                tmpThirdlist.append([total, loc])

        tmpThirdlist = sorted(tmpThirdlist, key=lambda x: x[0])
        ggmap.thirdList = [i[1] for i in tmpThirdlist]

        #print('\n', len(tmpThirdList))
        #for i in tmpThirdlist:
        #    print(i)
        #print(ggmap.thirdList)
