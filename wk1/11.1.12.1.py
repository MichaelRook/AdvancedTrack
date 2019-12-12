class Point:

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y


def distance(point1, point2):
    dx = point2.x - point1.x
    dy = point2.y - point1.y
    dsquared = dx ** 2 + dy ** 2
    result = dsquared ** 0.5
    return result


one = Point(1, 1)
two = Point(2, 2)

print(distance(one, two))
