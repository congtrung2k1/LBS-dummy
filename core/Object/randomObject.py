import random

def getRandomValue() -> dict:
	
	ret = {}
	for i in range(10):
		ret[str(i)] = 0

	cnt = random.randint(2, 10)

	for i in range(cnt):
		x = random.randint(0, 9)
		y = random.randint(1, 6)

		ret[str(x)] = y

	return ret