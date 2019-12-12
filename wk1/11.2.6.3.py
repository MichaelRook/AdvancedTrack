
from wk1.point import Point


class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def area(self):
        area = self.width * self.height
        return area

    def perimeter(self):
        perimeter = (self.width + self.height) * 2
        return perimeter

    def flip(self):
        self.width, self.height = self.height, self.width


r = Rectangle(Point(0, 0), 10, 5)
print(r.width, r.height)
r.flip()
print(r.width, r.height)
