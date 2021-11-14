"""
=================================================================
|	From here, call all the processing and filter.
|
|	processStart(ggmap) -> list
|	
|
=================================================================
"""

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Shape.classShape import Shape
from Object.operatorObject import percentObject



def processStart(ggmap) -> list:
	from firstFilter import firstFilter

	firstFilter(ggmap)


	print(ggmap.userShape)
	print(ggmap.userElementObject)
	print(len(ggmap.firstList))
	print(ggmap.firstList)


	return []






# Debug only
if __name__ == "__main__":

	userX = 10
	userY = 11
	ggmap = Shape(userX, userY)

	processStart(ggmap)

