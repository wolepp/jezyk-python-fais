#!/usr/bin/env python3

"""
Moduł z funkcjami do działań na ułamkach.
Ułamek reprezentowany przez listę dwóch liczb całkowitych [licznik, mianownik].

Wojciech Lepich
"""

import unittest
from math import gcd    # fractions.gcd is deprecated


def is_frac(*args):
    """
    Sprawdza czy frac jest ułamkiem i zwraca True lub False.

    >>> is_frac([1, 2])
    True
    >>> is_frac([1, 2], [-4, 3])
    True
    >>> is_frac([1, 2, 3])
    False
    >>> is_frac(5)
    False
    """

    for arg in args:
        if not isinstance(arg, list) \
                or not len(arg) == 2 \
                or not isinstance(arg[0], int) \
                or not isinstance(arg[1], int):
            return False
    return True


def lcm(a, b):
    """
    Least common multiple of a and b.
    Najmniejsza wspólna wielokrotność

    >>> lcm(2, 3)
    6
    >>> lcm(21, 6)
    42
    """

    return abs(a * b) // gcd(a, b)


def simplify_frac(frac):
    """
    Upraszcza ułamek.

    >>> simplify_frac([2, 4])
    [1, 2]
    >>> simplify_frac([-8, -10])
    [4, 5]
    >>> simplify_frac([1, -3])
    [-1, 3]
    >>> simplify_frac([0, 4])
    [0, 1]
    """

    if not is_frac(frac):
        raise TypeError("frac nie jest ulamkiem")

    licznik, mianownik = frac[0], frac[1]
    dzielnik = gcd(licznik, mianownik)

    if mianownik > 0:
        return [licznik // dzielnik, mianownik // dzielnik]
    return [-licznik // dzielnik, -mianownik // dzielnik]


def abs_frac(frac):
    """
    Zwraca wartość bezwzględną ułamka.

    >>> abs_frac([2, 4])
    [2, 4]
    >>> abs_frac([-1, 2])
    [1, 2]
    >>> abs_frac([1, -2])
    [1, 2]
    """

    if not is_frac(frac):
        raise TypeError("frac nie jest ulamkiem")

    return [abs(frac[0]), abs(frac[1])]


def reverse_frac(frac):
    """
    Odwraca zwrócony ułamek.

    >>> reverse_frac([1, 2])
    [2, 1]
    >>> reverse_frac([8, -4])
    [-4, 8]
    """

    if not is_frac(frac):
        raise TypeError("frac nie jest ulamkiem")

    return [frac[1], frac[0]]


def add_frac(frac1, frac2):
    """
    Zwraca ułamek będący sumą frac1 i frac2.

    >>> add_frac([1, 2], [1, 3])
    [5, 6]
    >>> add_frac([1, 2], [6, 4])
    [2, 1]
    >>> add_frac([-3, 4], [3, 4])
    [0, 1]
    """

    if not is_frac(frac1, frac2):
        raise TypeError("argumenty musza byc ulamkami")

    mianownik = lcm(frac1[1], frac2[1])
    licznik = frac1[0] * mianownik // frac1[1] + \
        frac2[0] * mianownik // frac2[1]
    return simplify_frac([licznik, mianownik])


def sub_frac(frac1, frac2):
    """
    Zwraca ułamek będący różnicą frac1 i frac2.

    >>> sub_frac([3, 4], [1, 4])
    [1, 2]
    >>> sub_frac([3, 4], [4, 5])
    [-1, 20]
    >>> sub_frac([1, 3], [-2, 3])
    [1, 1]
    >>> sub_frac([-2, 4], [-3, 4])
    [1, 4]
    """

    if not is_frac(frac1, frac2):
        raise TypeError("argumenty musza byc ulamkami")

    mianownik = lcm(frac1[1], frac2[1])
    licznik = frac1[0] * mianownik // frac1[1] - \
        frac2[0] * mianownik // frac2[1]
    return simplify_frac([licznik, mianownik])


def mul_frac(frac1, frac2):
    """
    Zwraca ułamek będący wynikiem mnożenia frac1 przez frac2.

    >>> mul_frac([3, 4], [1, 2])
    [3, 8]
    >>> mul_frac([3, 4], [0, 2])
    [0, 1]
    >>> mul_frac([3, 4], [-1, 2])
    [-3, 8]
    """

    if not is_frac(frac1, frac2):
        raise TypeError("argumenty musza byc ulamkiem")

    return simplify_frac([frac1[0] * frac2[0], frac1[1] * frac2[1]])


def div_frac(frac1, frac2):
    """
    Zwraca ułamek będący wynikiem dzielenia frac1 przez frac2.

    >>> div_frac([3, 4], [1, 2])
    [3, 2]
    >>> div_frac([3, 4], [-1, 2])
    [-3, 2]
    >>> div_frac([3, 4], [0, 2])
    Traceback (most recent call last):
        ...
    ValueError: Nie mozna dzielic przez zero
    """

    if not is_frac(frac1, frac2):
        raise TypeError("argumenty musza byc ulamkiem")
    if is_zero(frac2):
        raise ValueError('Nie mozna dzielic przez zero')

    return mul_frac(frac1, reverse_frac(frac2))


def is_positive(frac):
    """
    Sprawdza czy ułamek ma dodatnią wartość.

    >>> is_positive([1, 2])
    True
    >>> is_positive([-1, -2])
    True
    >>> is_positive([-1, 2])
    False
    >>> is_positive([1, -2])
    False
    """

    if not is_frac(frac):
        raise TypeError("frac nie jest ulamkiem")

    return (frac[0] > 0 and frac[1] > 0) \
        or (frac[0] < 0 and frac[1] < 0)


def is_zero(frac):
    """
    Sprawdza czy ułamek jest równy zero.

    >>> is_zero([0, 3])
    True
    >>> is_zero([1, 2])
    False
    """

    if not is_frac(frac):
        raise TypeError("frac nie jest ulamkiem")

    if frac[0] == 0:
        return True
    return False


def cmp_frac(frac1, frac2):
    """
    Porównuje dwa ułamki

    >>> cmp_frac([5,2], [3,2])
    1
    >>> cmp_frac([1,2], [3,2])
    -1
    >>> cmp_frac([3,2], [3,2])
    0
    """

    if not is_frac(frac1, frac2):
        raise TypeError("argumenty musza byc ulamkami")

    sub_of_abs = sub_frac(abs_frac(frac1), abs_frac(frac2))
    if sub_of_abs[0] > 0:
        return 1
    if sub_of_abs[0] == 0:
        return 0
    return -1


def frac2float(frac):
    """
    Konwertuje ułamek do float.

    >>> frac2float([1, 2])
    0.5
    >>> frac2float([-3, 2])
    -1.5
    """

    if not is_frac(frac):
        raise TypeError("frac nie jest ulamkiem")

    return frac[0] / frac[1]


class TestFractions(unittest.TestCase):
    """
    Klasa testująca funkcje modułu fracs.
    """

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([1, 2], [6, 4]), [2, 1])
        self.assertEqual(add_frac([-3, 4], [3, 4]), [0, 1])

        self.assertRaises(TypeError, lambda: add_frac(3, 5))

    def test_sub_frac(self):
        self.assertEqual(sub_frac([3, 4], [1, 4]), [1, 2])
        self.assertEqual(sub_frac([3, 4], [4, 5]), [-1, 20])
        self.assertEqual(sub_frac([1, 3], [-2, 3]), [1, 1])
        self.assertEqual(sub_frac([-2, 4], [-3, 4]), [1, 4])

        self.assertRaises(TypeError, lambda: sub_frac(3, 5))

    def test_mul_frac(self):
        self.assertEqual(mul_frac([3, 4], [1, 2]), [3, 8])
        self.assertEqual(mul_frac([3, 4], [0, 2]), [0, 1])
        self.assertEqual(mul_frac([3, 4], [-1, 2]), [-3, 8])

        self.assertRaises(TypeError, lambda: mul_frac(3, 5))

    def test_div_frac(self):
        self.assertEqual(div_frac([3, 4], [1, 2]), [3, 2])
        self.assertEqual(div_frac([3, 4], [-1, 2]), [-3, 2])

        self.assertRaises(TypeError, lambda: div_frac(3, 5))
        self.assertRaises(ValueError, lambda: div_frac([1, 3], [0, 1]))

    def test_is_positive(self):
        self.assertTrue(is_positive([1, 2]))
        self.assertTrue(is_positive([-1, -2]))

        self.assertFalse(is_positive([-1, 2]))
        self.assertFalse(is_positive([1, -2]))

        self.assertRaises(TypeError, lambda: is_positive('string'))

    def test_is_zero(self):
        self.assertTrue(is_zero([0, 3]))

        self.assertFalse(is_zero([1, 2]))

        self.assertRaises(TypeError, lambda: is_zero('string'))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([5, 2], [3, 2]), 1)
        self.assertEqual(cmp_frac([1, 2], [3, 2]), -1)
        self.assertEqual(cmp_frac([3, 2], [3, 2]), 0)

        self.assertRaises(TypeError, lambda: cmp_frac(3, 2))

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 2]), 0.5)
        self.assertEqual(frac2float([-3, 2]), -1.5)

        self.assertRaises(TypeError, lambda: frac2float(42))

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
