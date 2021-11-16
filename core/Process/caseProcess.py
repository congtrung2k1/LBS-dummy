"""
=================================================================
|	Main processing.
|	
|	newDummyLocation(x: int, y: int) -> list [ggmap, [dummyX, dummyY]]
|	nextDummyLocation(ggmap: object, x: int, y: int) -> list [dummyX, dummyY]
|	changeDummyLevel(level: int) -> list [dummyX, dummyY]
|
=================================================================
"""

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Shape.classShape import Shape
from locationFilter import locationFilter

# When phone reboot, this will reset the map
# Return list of (ggmap and dummy location)
def newDummyLocation(x: int, y: int) -> list: 	# [ggmap, [dummyX, dummyY]]
	ggmap = Shape(x, y)
	loc = locationFilter(ggmap)
	addingToMemory(ggmap)
	return [ggmap, loc]
	
	
# When user move around, this will calculate next dummy location
# Return dummy location
def nextDummyLocation(ggmap: object, x: int, y: int) -> list: 	# [dummyX, dummyY]
	ggmap.changeUserLocation(x, y)

	for pair in ggmap.memorized:
		if pair[2] == ggmap.level:
			if pair[0] == [ggmap.userX, ggmap.userY]:
				ggmap.dummyX = pair[1][0]
				ggmap.dummyY = pair[1][1]		
				ggmap.userShapeBotX = pair[3][0]
				ggmap.userShapeBotY = pair[3][1]
				
				return pair[1]

			else:
				lvl, tmpx, tmpy = pair[2], pair[3][0], pair[3][1]

				if tmpx - lvl + 1 <= x <= tmpx and tmpy - lvl + 1 <= y <= tmpy:
					ggmap.dummyX = pair[1][0]
					ggmap.dummyY = pair[1][1]		
					ggmap.userShapeBotX = tmpx
					ggmap.userShapeBotY = tmpy

					return pair[1]
		
	ggmap.placeUserShape()
	loc = locationFilter(ggmap)
	addingToMemory(ggmap)
	return loc


# This occurs when user change privacy level
# Check is that situation is occursed
def changePrivacyLevel(level: int = 4) -> list: 	# [dummyX, dummyY]
	existed = ggmap.changeLevel(level)

	if existed:
		return [ggmap.dummyX, ggmap.dummyY]

	loc = locationFilter(ggmap)
	addingToMemory(ggmap)
	return loc


# Saving the state
def addingToMemory(ggmap: object) -> None:
	ggmap.memorized.append([ [ggmap.userX, ggmap.userY], [ggmap.dummyX, ggmap.dummyY], ggmap.level, [ggmap.userShapeBotX, ggmap.userShapeBotY] ])

	return None



# Debug only
# if __name__ == "__main__":
# 	tmp = newDummyLocation(10, 11)
# 	ggmap = tmp[0]

# 	print(ggmap.userShapeBotX, ggmap.userShapeBotY)
# 	print(tmp[1])
# 	print(ggmap.memorized)

	
# 	tmp = nextDummyLocation(ggmap, 11, 12)

# 	print(ggmap.userShapeBotX, ggmap.userShapeBotY)
# 	print(tmp)
# 	print(ggmap.memorized)


# 	tmp = changeDummyLevel(4)

# 	print(ggmap.userShapeBotX, ggmap.userShapeBotY)
# 	print(tmp)
# 	print(ggmap.memorized)