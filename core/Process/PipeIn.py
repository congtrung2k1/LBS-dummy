"""
=================================================================
|	From here, call all the processing and filter.
|
|	processStart(x: int, y: int) -> list
|	
|
=================================================================
"""
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Shape.classShape import Shape
from Object.operatorObject import percentObject


ggmap = 0


def processStart(x: int, y: int) -> list:

	userShape = ggmap.getShape(x, y)

	print(userShape)




	return [x, y]


def placeShape(x: int, y: int, level : int = 3) -> list:
	c = n*n - 1

	while 1:
		import random
		r = randint(1, c)

		a = r // n
		b = r % n

		if 0 < x + a < ggmap.maxN && 0 < y + b < ggmap.maxM: break

	 






# Debug only
if __name__ == "__main__":

	ggmap = Shape()

	processStart(10, 11)

