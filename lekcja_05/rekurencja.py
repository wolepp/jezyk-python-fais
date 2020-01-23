#!/usr/bin/env python3

"""
Zawiera rekurencyjne funkcje do obliczania silnii oraz wyrazów
ciągu Fibonacciego.
"""


def is_natural_number(arg):
    """
    Sprawdza czy argument arg jest liczba naturalna.

    >>> is_natural_number(5)
    True
    >>> is_natural_number(-5)
    False
    >>> is_natural_number('string')
    False
    """

    try:
        arg = int(arg)
    except (ValueError, TypeError):
        return False

    if arg < 0:
        return False
    return True


def factorial(n):
    """
    Rekurencyjna funkcja do obliczania silnii z n

    >>> factorial(5)
    120
    >>> factorial(7)
    5040
    """

    if not is_natural_number(n):
        raise ValueError('n musi byc liczba naturalna')

    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """
    Iteracyjna wersja funkcji fibbonaci(n)

    >>> fibonacci(5)
    5
    >>> [fibonacci(x) for x in range(10)]
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """

    if not is_natural_number(n):
        raise ValueError('n musi byc liczba naturalna')

    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
