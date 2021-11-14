"""
=====================================================
|	Random number of elements in one object
|
|	getRandomValue() -> dict
|	zeroObject() -> dict
|
=====================================================
"""

# Define value
numElement = 10
numMin = 1
numMax = 2


# create cell with 0 value for each Object
def zeroObject() -> dict:
	ret = {}

	for i in range(numElement):
		ret[str(i)] = 0

	return ret


# create cell with random Object
def getRandomValue() -> dict:
	import random
	
	# init dict
	ret = {}
	for i in range(numElement):
		ret[str(i)] = 0

	# number of existed object
	cnt = random.randint(2, numElement//2)

	# Object no. remaining
	rest = [i for i in range(numElement)]

	# create object
	for i in range(cnt):
		# chose object no. in remaining list
		x = random.randint(0, len(rest) - 1)

		# chose value of that object
		y = random.randint(numMin, numMax)

		ret[str(rest[x])] = y
		rest.remove(rest[x])

	return ret