#!/usr/bin/env python3

"""
Moduł z funkcjami do działań na ułamkach.
Ułamek reprezentowany przez listę dwóch liczb całkowitych [licznik, mianownik].

Wojciech Lepich
"""

import doctest
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
        if not isinstance(arg, list) or not len(arg) == 2:
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
        raise TypeError("argumenty musza byc ulamkiem")

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
        raise TypeError("argumenty musza byc ulamkiem")

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
    # temporary scratch solution
    if frac[0] == 0:
        return True
    return False


def cmp_frac(frac1, frac2): pass


def frac2float(frac): pass


if __name__ == "__main__":
    doctest.testmod()
