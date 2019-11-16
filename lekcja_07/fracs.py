#!/usr/bin/env python3
"""
Zadanie 7.1

Wojciech Lepich
"""

from math import gcd


class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        if y == 0:
            raise ValueError('Mianownik musi być różny od 0')

        self.x = x
        self.y = y

    def __str__(self):         # zwraca "x/y" lub "x" dla y=1
        if self.y == 1:
            return '{}'.format(self.x)
        return '{}/{}'.format(self.x, self.y)

    def __repr__(self):        # zwraca "Frac(x, y)"
        return "Frac({}, {})".format(self.x, self.y)

    def simplify(self):
        """Zwraca uproszczony ułamek."""

        x = self.x // gcd(self.x, self.y)
        y = self.y // gcd(self.x, self.y)

        if y < 0:
            x, y = -x, -y

        return Frac(x, y)

    @staticmethod
    def _lcm(a, b):
        """Najmniejsza wspólna wielokrotność a i b."""
        return abs(a * b) // gcd(a, b)

    def __add__(self, other):  # frac1 + frac2, frac + int
        if isinstance(other, int):
            y = self.y
            x = self.x + other * self.y
        else:
            y = Frac._lcm(self.y, other.y)
            x = (self.x * y // self.y) + (other.x * y // other.y)
        return Frac(x, y).simplify()

    __radd__ = __add__

    def __sub__(self, other):  # frac1 - frac2, frac - int
        if isinstance(other, int):
            y = self.y
            x = self.x - other * self.y
        else: 
            y = Frac._lcm(self.y, other.y)
            x = (self.x * y // self.y) - (other.x * y // other.y)
        return Frac(x, y).simplify()

    def __rsub__(self, other):  # int - frac
        return Frac(self.y * other - self.x, self.y)

    def __mul__(self, other):  # frac1 * frac2, frac * int
        if isinstance(other, Frac):
            return Frac(self.x * other.x, self.y * other.y).simplify()
        return Frac(self.x * other, self.y).simplify()

    __rmul__ = __mul__

    def __truediv__(self, other):  # frac1 / frac2, frac / int
        if other == 0:
            raise ZeroDivisionError('Nie mozna dzielic przez zero')

        if isinstance(other, int):
            return self * Frac(1, other)
        return self * ~other

    def __rtruediv__(self, other): # int / frac
        return float(other * ~self)

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __lt__(self, other):    	# <
        if float(self) < float(other):
            return True
        return False

    def __gt__(self, other):    	# >
        if float(self) > float(other):
            return True
        return False

    def __le__(self, other):    	# <=
        if float(self) <= float(other):
            return True
        return False

    def __ge__(self, other):    	# >=
        if float(self) >= float(other):
            return True
        return False

    def __eq__(self, other):    	# ==
        if float(self) == float(other):
            return True
        return False

    def __ne__(self, other):            # !=
        if float(self) != float(other):
            return True
        return False

    def __float__(self):       # float(frac)
        return self.x / self.y


import unittest

class TestFrac(unittest.TestCase):

    def setUp(self):
        pass

    def test___init__(self):
        self.assertRaises(ValueError, lambda: Frac(4, 0))

    def test___str__(self):
        self.assertEqual(str(Frac(1, 2)), '1/2')
        self.assertEqual(str(Frac(-1, 2)), '-1/2')
        self.assertEqual(str(Frac(-1, -2)), '-1/-2')
        self.assertEqual(str(Frac(1, -2)), '1/-2')
        self.assertEqual(str(Frac(4, 1)), '4')

    def test___repr__(self):
        self.assertEqual(repr(Frac(1, 2)), 'Frac(1, 2)')
        self.assertEqual(repr(Frac(-9, 4)), 'Frac(-9, 4)')
        self.assertEqual(repr(Frac(1, 1)), 'Frac(1, 1)')

    def test___add__(self):
        # frac + frac
        self.assertEqual(Frac(1, 2) + Frac(1, 3), Frac(5, 6))
        self.assertEqual(Frac(1, 2) + Frac(6, 4), Frac(2, 1))
        self.assertEqual(Frac(-3, 4) + Frac(3, 4), Frac(0, 1))

        # frac + int
        self.assertEqual(Frac(1, 2) + 3, Frac(7, 2))
        self.assertEqual(Frac(1, 2) + (-5), Frac(-9, 2))

    def test___radd__(self):
        # int + frac
        self.assertEqual(3 + Frac(1, 2), Frac(7, 2))
        self.assertEqual(-5 + Frac(1, 2), Frac(-9, 2))

    def test___sub__(self):
        # frac - frac
        self.assertEqual(Frac(3, 4) - Frac(1, 4), Frac(1, 2))
        self.assertEqual(Frac(3, 4) - Frac(4, 5), Frac(-1, 20))
        self.assertEqual(Frac(1, 3) - Frac(-2, 3), Frac(1, 1))
        self.assertEqual(Frac(-2, 4) - Frac(-3, 4), Frac(1, 4))

        # frac - int
        self.assertEqual(Frac(3, 4) - 2, Frac(-5, 4))
        self.assertEqual(Frac(1, 2) - 5, Frac(-9, 2))

    def test___rsub__(self):
        # int - frac
        self.assertEqual(2 - Frac(3, 4), Frac(5, 4))
        self.assertEqual(5 - Frac(1, 2), Frac(9, 2))

    def test___mul__(self):
        # frac * frac
        self.assertEqual(Frac(3, 4) * Frac(1, 2), Frac(3, 8))
        self.assertEqual(Frac(3, 4) * Frac(0, 2), Frac(0, 1))
        self.assertEqual(Frac(3, 4) * Frac(-1, 2), Frac(-3, 8))

        # frac * int
        self.assertEqual(Frac(3, 4) * 2, Frac(3, 2))
        self.assertEqual(Frac(-5, 8) * 3, Frac(-15, 8))

    def test___rmul__(self):
        # int * frac
        self.assertEqual(2 * Frac(3, 4), Frac(3, 2))
        self.assertEqual(3 * Frac(-5, 8), Frac(-15, 8))


    def test___div__(self):
        self.assertEqual(Frac(3, 4) / Frac(1, 2), Frac(3, 2))
        self.assertEqual(Frac(3, 4) / Frac(-1, 2), Frac(-3, 2))

        self.assertRaises(ZeroDivisionError, lambda: Frac(1, 3) / Frac(0, 1))

    def test___pos__(self):
        self.assertEqual(+Frac(2, 5), Frac(2, 5))
        self.assertEqual(+Frac(-1, 3), Frac(-1, 3))

    def test___neg__(self):
        self.assertEqual(-Frac(2, 5), Frac(-2, 5))
        self.assertEqual(-Frac(-1, 3), Frac(1, 3))
        self.assertEqual(-Frac(-5, -8), Frac(5, -8))

    def test___invert__(self):
        self.assertEqual(~Frac(2, 4), Frac(4, 2))
        self.assertEqual(~Frac(9, -5), Frac(-5, 9))

    def test_lt(self):
        self.assertLess(Frac(1, 2), Frac(3, 4))
        self.assertLess(Frac(-4, 5), Frac(1, 4))

    def test_gt(self):
        self.assertGreater(Frac(6, 10), Frac(1, 5))
        self.assertGreater(Frac(0, 1), Frac(-1, 3))

    def test_le(self):
        self.assertLessEqual(Frac(1, 2), Frac(3, 4))
        self.assertLessEqual(Frac(4, 2), Frac(4, 2))

    def test_ge(self):
        self.assertGreaterEqual(Frac(7, 8), Frac(3, 4))
        self.assertGreaterEqual(Frac(-1, 3), Frac(-1, 3))
        self.assertGreaterEqual(Frac(-1, 3), Frac(-2, 6))

    def test_eq(self):
        self.assertEqual(Frac(1, 5), Frac(1, 5))
        self.assertEqual(Frac(1, 5), Frac(3, 15))
        self.assertEqual(Frac(1, 3), Frac(-3, -9))

    def test_ne(self):
        self.assertNotEqual(Frac(1, 3), Frac(2, 3))
        self.assertNotEqual(Frac(0, 1), Frac(-5, 5))

    def test___float__(self):
        self.assertEqual(float(Frac(1, 2)), 0.5)
        self.assertEqual(float(Frac(-3, 2)), -1.5)
        self.assertAlmostEqual(float(Frac(1, 3)), 0.3333333)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
