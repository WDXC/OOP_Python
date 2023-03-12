import math

class point:
    def __init__(self, x = 0, y = 0):
        self._x = x
        self._y = y

    def rest(self):
        self._x = 0
        self._y = 0

    def calculate_distance(self, other_point):
        return math.sqrt(
            (self._x - other_point._x) ** 2 +
            (self._y - other_point._y) ** 2
        )
p1 = point(2, 3)
p2 = point(4, 3)

print(p1.calculate_distance(p2))

p1.rest()
print(p1.calculate_distance(p2))


