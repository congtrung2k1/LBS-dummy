"""
=================================================================
|	First filter, get all the shape which have existed object like userShape
|
|	firstFilter(ggmap: object) -> None:
|
=================================================================
"""

def firstFilter(ggmap: object) -> None:
	# Get the list of existed object of userShape
	temp = {}
	for key in ggmap.userShape:
		if ggmap.userShape[key] != 0:
			temp[key] = ggmap.userShape[key]

	ggmap.userElementObject = temp

	# Get all the same shape which have existed object like temp
	for i in range(ggmap.level, ggmap.maxN):
		for j in range(ggmap.level, ggmap.maxM):
			if i != ggmap.userShapeBotX or j != ggmap.userShapeBotY:
				tmpShape = ggmap.getShape(i, j, ggmap.level)
				
				check = 1
				for key in temp:
					if tmpShape[key] == 0:
						check = 0
						break

				if check:
					ggmap.firstList.append([i,j])