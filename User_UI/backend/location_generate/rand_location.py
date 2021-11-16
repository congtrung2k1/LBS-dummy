import random

def random_location() -> list:
        x = random.randint(1, 99)
        y = random.randint(1, 99)
        return [x, y]
