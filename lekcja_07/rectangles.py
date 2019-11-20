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

    def __eq__(self, other):   # obsługa rect1 == rect2
        return (self.pt1 == other.pt1 and self.pt2 == other.pt2)

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):          # zwraca środek prostokąta
        x = (self.pt1.x + self.pt2.x) / 2
        y = (self.pt1.y + self.pt2.y) / 2
        return Point(x, y)

    def area(self):            # pole powierzchni
        width = abs(self.pt1.x) + abs(self.pt2.x)
        length = abs(self.pt1.y) + abs(self.pt2.y)
        return width * length

    def move(self, x, y):      # przesunięcie o (x, y)
        v = Point(x, y)
        self.pt1 += v
        self.pt2 += v
        return self

    def intersection(self, other):  # część wspólna prostokątów
        # TODO: Jezeli się nie pokrywaja - zwrocic wyjatek!
        # jezeli się nie pokrywają zwróć wyjątek

        x1 = max(self.pt1.x, other.pt1.x)
        y1 = max(self.pt1.y, other.pt1.y)
        x2 = min(self.pt2.x, other.pt2.x)
        y2 = min(self.pt2.y, other.pt2.y)
        try:
            return Rectangle(x1, y1, x2, y2)
        except ValueError:
            raise ArithmeticError('Prostokaty sie nie przecinaja')

    def cover(self, other):    # prostąkąt nakrywający oba
        x1 = min(self.pt1.x, other.pt1.x)
        y1 = min(self.pt1.y, other.pt1.y)
        x2 = max(self.pt2.x, other.pt2.x)
        y2 = max(self.pt2.y, other.pt2.y)
        return Rectangle(x1, y1, x2, y2)

    def make4(self):           # zwraca listę czterech mniejszych
        # TODO:
        #  _____________
        # |      |      |
        # |  1   |   2  |
        # |      |      |
        # |------+------|
        # |      |      |
        # |  4   |   3  |
        # |______|______|
        pass

# Kod testujący moduł.


class TestRectangle(unittest.TestCase):

    def setUp(self):
        pass

    def test___init__(self):
        self.assertRaises(ValueError, lambda: Rectangle(9, 0, 5, 3))
        self.assertRaises(ValueError, lambda: Rectangle(0, 8, 3, 4))

    def test___str__(self):
        self.assertEqual(str(Rectangle(0, 1, 3, 4)), '[(0, 1), (3, 4)]')
        self.assertEqual(str(Rectangle(-3, -2, 5, 40)), '[(-3, -2), (5, 40)]')

    def test___repr__(self):
        self.assertEqual(repr(Rectangle(1, 2, 3, 4)), 'Rectangle(1, 2, 3, 4)')
        self.assertEqual(
            repr(Rectangle(-10, 20, 3, 40)),
            'Rectangle(-10, 20, 3, 40)')

    def test___eq__(self):
        self.assertEqual(Rectangle(1, 2, 3, 4), Rectangle(1, 2, 3, 4))
        self.assertEqual(Rectangle(-5, -4, -3, -2), Rectangle(-5, -4, -3, -2))

    def test_center(self):
        self.assertEqual(Rectangle(0, 0, 4, 2).center(), Point(2, 1))
        self.assertEqual(Rectangle(-4, -4, 6, 12).center(), Point(1, 4))

    def test_area(self):
        self.assertEqual(Rectangle(0, 0, 4, 2).area(), 8)
        self.assertEqual(Rectangle(-4, -4, 6, 12).area(), 160)

    def test_move(self):
        self.assertEqual(Rectangle(0, 0, 4, 2).move(3, 5),
                         Rectangle(3, 5, 7, 7))
        self.assertEqual(Rectangle(-4, -4, 6, 12).move(-6, 2),
                         Rectangle(-10, -2, 0, 14))

    def test_intersection(self):
        # nieprzecinające się
        self.assertRaises(ArithmeticError,
                          lambda: Rectangle(0, 0, 1, 1).intersection(Rectangle(2, 2, 3, 3)))

        # w tym samym miejscu
        self.assertEqual(
            Rectangle(0, 0, 4, 4).intersection(Rectangle(0, 0, 4, 4)),
            Rectangle(0, 0, 4, 4))

        # drugi prostokąt na NE
        self.assertEqual(
            Rectangle(0, 0, 4, 4).intersection(Rectangle(2, 2, 6, 6)),
            Rectangle(2, 2, 4, 4))

        # drugi prostokąt na NW
        self.assertEqual(
            Rectangle(0, -2, 4, 2).intersection(Rectangle(-2, 0, 2, 4)),
            Rectangle(0, 0, 2, 2))

        # drugi prostokąt na SE
        self.assertEqual(
            Rectangle(2, 2, 6, 6).intersection(Rectangle(0, 0, 4, 4)),
            Rectangle(2, 2, 4, 4))

        # drugi prostokąt na SW
        self.assertEqual(
            Rectangle(0, 2, 4, 6).intersection(Rectangle(2, 0, 6, 4)),
            Rectangle(2, 2, 4, 4))

    def test_cover(self):
        # w tym samym miejscu
        self.assertEqual(
            Rectangle(0, 0, 4, 4).cover(Rectangle(0, 0, 4, 4)),
            Rectangle(0, 0, 4, 4))

        # drugi prostokąt na NE
        self.assertEqual(
            Rectangle(0, 0, 4, 4).cover(Rectangle(2, 2, 6, 6)),
            Rectangle(0, 0, 6, 6))

        # drugi prostokąt na NW
        self.assertEqual(
            Rectangle(0, -2, 4, 2).cover(Rectangle(-2, 0, 2, 4)),
            Rectangle(-2, -2, 4, 4))

        # drugi prostokąt na SE
        self.assertEqual(
            Rectangle(2, 2, 6, 6).cover(Rectangle(0, 0, 4, 4)),
            Rectangle(0, 0, 6, 6))

        # drugi prostokąt na SW
        self.assertEqual(
            Rectangle(0, 2, 4, 6).cover(Rectangle(2, 0, 6, 4)),
            Rectangle(0, 0, 6, 6))

    def test_make4(self):
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
