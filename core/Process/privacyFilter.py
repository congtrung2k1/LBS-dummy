"""
=================================================================
|	Get new shape, which changed privacy, overlapse with the older.
|	
|	privacyCheck(ggmap: object) -> bool
|
=================================================================
"""

def checkInbound(value: int) -> bool:
	maxValue = 100
	return 0 < value < maxValue

def checkUserIn(x, y, topX, botX, topY, botY) -> bool:
	return topX <= x <= botX and topY <= y <= botY

def addList(ggmap: object) -> None:
	dX = [0, 0, 1, 1, 0, 1, 2, 2, 2]
	dY = [0, 1, 0, 1, 2, 2, 0, 1, 2]

	uX = ggmap.userShape[0]
	uY = ggmap.userShape[1]
	c = ggmap.level - ggmap.lastl
	tempList = []

	for i in range((c + 1) * (c + 1) + 1):
		topX = uX + dX[i] - ggmap.level + 1
		botX = uX + dX[i]
		topY = uY + dY[i] - ggmap.level + 1
		botY = uY + dY[i]
		if checkInbound(topX):
			if checkInbound(topY):
				tempList.append(ggmap.getShape(botX, botY, ggmap.level))

def minusList(ggmap: object) -> None:
	dX = [0, 0, 1, 1, 0, 1, 2, 2, 2]
	dY = [0, 1, 0, 1, 2, 2, 0, 1, 2]

	uX = ggmap.userShape[0]
	uY = ggmap.userShape[1]
	c = ggmap.level - ggmap.lastl
	tempList = []

	for i in range((c + 1) * (c + 1) + 1):
		topX = uX - dX[i] - ggmap.level + 1
		botX = uX - dX[i]
		topY = uY - dY[i] - ggmap.level + 1
		botY = uY - dY[i]
		if checkInbound(topX):
			if checkInbound(topY):
				tempList.append([botX, botY])

#				if checkUserIn(ggmap.userX, ggmap.userY, topX, botX, topY, botY):


def privacyCheck(ggmap: object) -> bool:
	tempList = []
	if ggmap.level > ggmap.lastl:
		tempList = addList(ggmap)
	else:
		tempList = minusList(ggmap)

	tmpPrivList = []
	tempUser = percentObject(ggmap.userShape)

	for loc in tempList:
		x = abs(ggmap.userX - loc[0])
		y = abs(ggmap.userY - loc[1])
		
		tmp = ggmap.getShape(loc[0], loc[1], ggmap.level)
		tmpPer = percentObject(tmp)

		total = 0.0
		for key in tempUser:
			total += abs(tmpPer[key] - tempUser[key])
		tmpPrivList.append([total, loc])

	tmpPrivList = sorted(tmpPrivList, key= lambda x:x[0])
	if tmpPrivList != None:
		ggmap.dummyX = tmpPrivList[0][1][0]
		ggmap.dummyy = tmpPrivList[0][1][1]
		return True

	return False