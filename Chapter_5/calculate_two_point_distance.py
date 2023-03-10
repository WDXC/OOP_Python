import math

class Point:

    def __init__(self, points=[]):
        self.vertices = []
        for point in points:
            if isinstance(point, tuple):
                point = Point(*point)
            self.vertices.append(point)

    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
    """

    def distance(self, other):
        return math.sqrt(
            (self.x - other.x) ** 2 +
            (self.y - other.y)**2
        )

class Polygon:
    def __init__(self):
        self.vertices = []

    def add_point(self, point):
        self.vertices.append((point))

    def permiter(self):
        perimeter = 0
        points = self.vertices + [self.vertices[0]]
        for i in range(len(self.vertices)):
            perimeter += points[i].distance(points[i+1])
        return perimeter

# driver
square = Polygon()
square.add_point(Point(1,1))
square.add_point(Point(1, 2))
square.add_point(Point(2,2))
square.add_point(Point(2, 1))
print(square.permiter())
