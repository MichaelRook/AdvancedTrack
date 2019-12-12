class Point:

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def reflect_x(self):
        return self.x, self.y * -1

    def slope_from_origin(self):
        return self.y / self.x

    def get_line_to(self, target):
        a = self
        b = target
        i = (b.x - a.x)
        j = (b.y - a.y)
        return i, j

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)


print(Point(4, 11).get_line_to(Point(6, 15)))

"""unclear what to do here"""
