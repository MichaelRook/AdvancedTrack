class Point:

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def reflect_x(self):
        return self.x, self.y * -1

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)


a = Point(1, 1)
print(a)

b = a.reflect_x()
print(b)
