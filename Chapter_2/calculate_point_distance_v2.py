class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

def move(self, x, y):
    self._x = x
    self._y = y

def reset(self, x, y):
    self._x = 0
    self._y = 0

pt = Point(3, 4)
move(pt, 4, 3)
print(pt._x, pt._y)