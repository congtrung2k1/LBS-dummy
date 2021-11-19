"""
=====================================================
|    Contain the operator with object
|
|    addObject(a: dict, b: dict) -> dict
|    minusObject(a: dict, b: dict) -> dict
|    countObject(a: dict) -> int
|    percentObject(a: dict) -> dict
|    sortObject(a: dict, ord : int = 1) -> dict
|
=====================================================
"""

# adding 2 object together
def addObject(a: dict, b: dict) -> dict:
    ret = {}

    for i in range(10):
        ret[str(i)] = a[str(i)] + b[str(i)]

    return ret


# Minus EXISTED object elements
def minusObject(a: dict, b: dict) -> dict:
    ret = {}

    for i in range(10):
        ret[str(i)] = a[str(i)] - b[str(i)]

    return ret


# Counting the number of element of object
def countObject(a: dict) -> int:
    cnt = 0

    for i in range(10):
        cnt += a[str(i)]

    return cnt


# Calculate percent of all elements on object
def percentObject(a: dict) -> dict:
    cnt = countObject(a)

    ret = {}

    for i in range(10):
        ret[str(i)] = float( a[str(i)] / cnt )

    return ret


# Sort the Object with value, default is decreasing
def sortObject(a: dict, ord : int = 1) -> dict:

    return dict(sorted(a.items(), key= lambda x:x[1], reverse = ord))


""" Debug only
if __name__ == "__main__":
    from randomObject import getRandomValue

    a = getRandomValue()

    print(a)

    a = percentObject(a)

    a = sortObject(a)

    print(a)
"""
