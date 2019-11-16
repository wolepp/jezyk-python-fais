#!/usr/bin/env python3
"""
Zadanie 7.3
Moduł z klasą rectangle.

Wojciech Lepich
"""

import unittest
from points import Point


class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        # Chcemy, aby x1 < x2, y1 < y2.
        if not x1 < x2:
            raise ValueError('x1 musi być mniejsze niż x2')
        if not y1 < y2:
            raise ValueError('y1 musi być mniejsze niż y2')

        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):         # "[(x1, y1), (x2, y2)]"
        return "[{}, {}]".format(self.pt1, self.pt2)

    def __repr__(self):        # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle({}, {}, {}, {})".format(
            self.pt1.x, self.pt1.y,
            self.pt2.x, self.pt2.y)

    def __eq__(self, other): pass   # obsługa rect1 == rect2

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self): pass          # zwraca środek prostokąta

    def area(self): pass            # pole powierzchni

    def move(self, x, y): pass      # przesunięcie o (x, y)

    def intersection(self, other): pass  # część wspólna prostokątów

    def cover(self, other): pass    # prostąkąt nakrywający oba

    def make4(self): pass           # zwraca listę czterech mniejszych

# Kod testujący moduł.


class TestRectangle(unittest.TestCase):

    def setUp(self):
        pass

    def test___init__(self):
        self.assertRaises(ValueError, lambda: Rectangle(9, 0, 5, 3))
        self.assertRaises(ValueError, lambda: Rectangle(0, 8, 3, 4))

    def test___str__(self):
        self.assertEqual(str(Rectangle(0, 1, 3, 4)), '[(0, 1), (3, 4)]')

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
