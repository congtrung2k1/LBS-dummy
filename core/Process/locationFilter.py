"""
=================================================================
|	Make a new filter list, return dummy location
|
|	locationFilter(ggmap: object) -> list [dummyX, dummyY]
|	
=================================================================
"""

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#from Shape.classShape import Shape

from firstFilter import firstFilter
from secondFilter import secondFilter
from thirdFilter import thirdFilter


def locationFilter(ggmap: object) -> list:	# [dummyX, dummyY]
	firstFilter(ggmap)
	secondFilter(ggmap)
	thirdFilter(ggmap)

	listUse = []
	if len(ggmap.thirdList) != 0:
		listUse = ggmap.thirdList
	elif len(ggmap.secondList) != 0:
		listUse = ggmap.secondList
	else:
		listUse = ggmap.firstList

	ggmap.dummyX = listUse[0][0]
	ggmap.dummyY = listUse[0][1]

	return [ggmap.dummyX, ggmap.dummyY]



# Debug only
# if __name__ == "__main__":

# 	userX = 10
# 	userY = 11
# 	ggmap = Shape(userX, userY)

# 	print(locationFilter(ggmap))

