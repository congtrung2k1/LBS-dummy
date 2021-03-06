"""
=================================================================
|    Make a new filter list, return dummy location
|
|    locationFilter(ggmap: object) -> list [dummyX, dummyY]
|
=================================================================
"""


#from Shape.classShape import Shape

from .firstFilter import firstFilter
from .secondFilter import secondFilter
from .thirdFilter import thirdFilter
from .fourthFilter import fourthFilter


def locationFilter(ggmap: object) -> list:    # [dummyX, dummyY]
    firstFilter(ggmap)
    print('\nFirst list', ggmap.userX, ggmap.userY, '\n', len(ggmap.firstList), ggmap.firstList)
    secondFilter(ggmap)
    print('\nSecond list', ggmap.userX, ggmap.userY, '\n', len(ggmap.secondList), ggmap.secondList)
    thirdFilter(ggmap)
    print('\nThird list', ggmap.userX, ggmap.userY, '\n', len(ggmap.thirdList), ggmap.thirdList)
    fourthFilter(ggmap)
    print('\nFourth list', ggmap.userX, ggmap.userY, '\n', ggmap.fourthList)

    listUse = []
    if len(ggmap.fourthList) != 0:
        listUse = ggmap.fourthList
    elif len(ggmap.thirdList) != 0:
        listUse = ggmap.thirdList
    elif len(ggmap.secondList) != 0:
        listUse = ggmap.secondList
    else:
        listUse = ggmap.firstList

    ggmap.dummyX = listUse[0][0]
    ggmap.dummyY = listUse[0][1]

    return listUse[0]



# Debug only
# if __name__ == "__main__":

#     userX = 10
#     userY = 11
#     ggmap = Shape(userX, userY)

#     print(locationFilter(ggmap))

