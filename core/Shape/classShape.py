"""
=================================================================
|	Class hold information of all table, calculating all shape
|
|	initTable(self) -> None
|	calcAllShape(self) -> None
|	getShape(self, x: int, y: int, level: int = 3) -> dict
|
=================================================================
"""
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Object.randomObject import getRandomValue, zeroObject
from Object.operatorObject import addObject, minusObject


class Shape():
	def __init__ (self):
		self.table = []
		self.maxN = 100
		self.maxM = 100

		self.initTable()		
		self.calcAllShape()


	# Create the table with random object
	def initTable(self) -> None:

		# row 0
		tmp = [zeroObject() for i in range(self.maxM)]
		self.table.append(tmp)

		for i in range(1, self.maxN):
			tmp = []

			# column 0
			tmp.append(zeroObject())

			for j in range(1, self.maxM):
				tmp.append(getRandomValue())

			self.table.append(tmp)


	# Calculate all shape inside table
	def calcAllShape(self) -> None:
		for i in range(1, self.maxN):
			for j in range(1, self.maxM):
				tmp = self.table[i][j]
				tmp = addObject(tmp, self.table[i-1][j])
				tmp = addObject(tmp, self.table[i][j-1])
				self.table[i][j] = minusObject(tmp, self.table[i-1][j-1])

		return None


	# Get shape with level
	def getShape(self, x: int, y: int, level: int = 3) -> dict:
		if x >= self.maxN | x - level < 0 | y >= self.maxM | y - level < 0: 
			return zeroObject()

		ret = self.table[x][y]
		ret = minusObject(ret, self.table[x - level][y])
		ret = minusObject(ret, self.table[x][y - level])
		ret = addObject(ret, self.table[x - level][y - level])

		return ret


""" Debug only
if __name__ == "__main__":
	ggmap = Shape()
	
	for i in range(1, ggmap.maxN):
		for j in range(1, ggmap.maxM):
			print(i, j, ggmap.table[i][j])
			input()

"""