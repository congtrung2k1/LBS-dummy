"""
=====================================================
|	Random number of elements in one object
|
|	getRandomValue() -> dict
|	zeroObject() -> dict
|
=====================================================
"""

# create cell with 0 value for each Object
def zeroObject() -> dict:
	ret = {}

	for i in range(10):
		ret[str(i)] = 0

	return ret


# create cell with random Object
def getRandomValue() -> dict:
	import random
	
	# init dict
	ret = {}
	for i in range(10):
		ret[str(i)] = 0

	# number of existed object
	cnt = random.randint(2, 10)

	# Object no. remaining
	rest = [i for i in range(10)]

	# create object
	for i in range(cnt):
		# chose object no. in remaining list
		x = random.randint(0, len(rest) - 1)

		# chose value of that object
		y = random.randint(1, 4)

		ret[str(rest[x])] = y
		rest.remove(rest[x])

	return ret