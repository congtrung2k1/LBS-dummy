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


	return [x, y]	 






# Debug only
if __name__ == "__main__":

	ggmap = Shape(10, 11)

	processStart(10, 11)

