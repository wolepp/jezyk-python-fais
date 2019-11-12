#!/usr/bin/env python3

"""
Moduł z funkcjami do działań na ułamkach.
Ułamek reprezentowany przez listę dwóch liczb całkowitych [licznik, mianownik].

Wojciech Lepich
"""

import doctest
from math import gcd    # fractions.gcd is deprecated


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

    if not isinstance(frac, list) or not len(frac) == 2:
        raise TypeError("frac nie jest ulamkiem")

    licznik, mianownik = frac[0], frac[1]
    dzielnik = gcd(licznik, mianownik)

    if mianownik > 0:
        return [licznik // dzielnik, mianownik // dzielnik]
    return [-licznik // dzielnik, -mianownik // dzielnik]


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

    if not isinstance(frac1, list) or not len(frac1) == 2:
        raise TypeError("frac1 nie jest ulamkiem")
    if not isinstance(frac2, list) or not len(frac2) == 2:
        raise TypeError("frac2 nie jest ulamkiem")

    mianownik = lcm(frac1[1], frac2[1])
    licznik = frac1[0] * mianownik // frac1[1] + \
        frac2[0] * mianownik // frac2[1]
    return simplify_frac([licznik, mianownik])


def sub_frac(frac1, frac2): pass


def mul_frac(frac1, frac2): pass


def div_frac(frac1, frac2): pass


def is_positive(frac): pass


def is_zer(frac): pass


def cmp_frac(frac1, frac2): pass


def frac2float(frac): pass


if __name__ == "__main__":
    doctest.testmod()
