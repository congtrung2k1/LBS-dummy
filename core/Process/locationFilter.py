"""
=================================================================
|	Make a new filter list, return dummy location
|
|	locationFilter(ggmap: object) -> list [dummyX, dummyY]
|	
=================================================================
"""


#from Shape.classShape import Shape

from .firstFilter import firstFilter
from .secondFilter import secondFilter
from .thirdFilter import thirdFilter
from .fourthFilter import fourthFilter


def locationFilter(ggmap: object) -> list:	# [dummyX, dummyY]
	firstFilter(ggmap)
	secondFilter(ggmap)
	thirdFilter(ggmap)
	fourthFilter(ggmap)

	listUse = []
	if len(ggmap.fourthList) != 0:
		listUse = ggmap.fourthList
	elif len(ggmap.thirdList) != 0:
		listUse = ggmap.thirdList
	elif len(ggmap.secondList) != 0:
		listUse = ggmap.secondList
	else:
		listUse = ggmap.firstList

	ggmap.preDummyX = ggmap.dummyX
	ggmap.preDummyY = ggmap.dummyY
	ggmap.dummyX = listUse[0][0]
	ggmap.dummyY = listUse[0][1]

	return listUse[0]



# Debug only
# if __name__ == "__main__":

# 	userX = 10
# 	userY = 11
# 	ggmap = Shape(userX, userY)

# 	print(locationFilter(ggmap))

