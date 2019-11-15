#!/usr/bin/env python3
"""
Zadanie 6.5

Wojciech Lepich
"""

import unittest
from math import sqrt


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):         # zwraca string "(x, y)"
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):        # zwraca string "Point(x, y)"
        return "Point({}, {})".format(self.x, self.y)

    def __eq__(self, other):   # obsługa point1 == point2
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __sub__(self, other):  # v1 - v2
        x = self.x - other.x
        y = self.y - other.y
        return Point(x, y)

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        """v1 x v2 - iloczyn wektorowy 2D."""
        return self.x * other.y - self.y * other.x

    def length(self):
        """Zwraca długość wektora"""
        return sqrt(self.x ** 2 + self.y ** 2)


# Kod testujący moduł.
class TestPoint(unittest.TestCase):

    def setUp(self):
        pass

    def test___str__(self):
        self.assertEqual(str(Point(1, 2)), '(1, 2)')
        self.assertEqual(str(Point(0, -3)), '(0, -3)')

    def test___repr__(self):
        self.assertEqual(repr(Point(1, 2)), 'Point(1, 2)')
        self.assertEqual(repr(Point(0, -3)), 'Point(0, -3)')

    def test___eq__(self):
        self.assertEqual(Point(1, 2), Point(1, 2))
        self.assertEqual(Point(2, 0), Point(2, 0))

    def test___ne__(self):
        self.assertNotEqual(Point(1, 2), Point(0, -3))
        self.assertNotEqual(Point(2, 0), Point(-7, 1))

    def test___add__(self):
        self.assertEqual(Point(1, 2) + Point(3, 4), Point(4, 6))
        self.assertEqual(Point(-8, 4) + Point(2, 3), Point(-6, 7))

    def test___sub__(self):
        self.assertEqual(Point(1, 2) - Point(3, 4), Point(-2, -2))
        self.assertEqual(Point(-8, 4) - Point(2, 3), Point(-10, 1))

    def test___mul__(self):
        self.assertEqual(Point(1, 2) * Point(3, 4), 11)
        self.assertEqual(Point(-8, 4) * Point(2, 3), -4)

    def test_cross(self):
        self.assertEqual(Point(1, 2).cross(Point(3, 4)), -2)
        self.assertEqual(Point(-8, 4).cross(Point(2, 3)), -32)

    def test_length(self):
        self.assertEqual(Point(-4, 0).length(), 4)
        self.assertEqual(Point(2, 2).length(), sqrt(8))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
