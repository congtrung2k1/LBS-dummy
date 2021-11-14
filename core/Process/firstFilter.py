"""
=================================================================
|	First filter, get all the shape which have existed object like userShape
|
|	firstFilter(ggmap) -> list:
|	
|	
|
=================================================================
"""


def firstFilter(ggmap) -> list:
	# Get the list of existed object of userShape
	temp = {}
	for key in ggmap.userShape:
		if ggmap.userShape[key] != 0:
			temp[key] = ggmap.userShape[key]

	ggmap.userElementObject = temp

	# Get all the same shape which have existed object like temp
	for i in range(ggmap.level, ggmap.maxN):
		for j in range(ggmap.level, ggmap.maxM):
			tmpShape = ggmap.getShape(i, j, ggmap.level)
			check = 1
			for key in temp:
				if tmpShape[key] == 0:
					check = 0
					break

			if check:
				ggmap.firstList.append([i,j])