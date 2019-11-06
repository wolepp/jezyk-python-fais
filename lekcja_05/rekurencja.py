"""
Zawiera rekurencyjne funkcje do obliczania silnii oraz wyrazow
ciagu Fibonacciego.
"""
import functools


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
    return True


def factorial(n):
    """
    Iteracyjna wersja funkcji factorial(n).

    >>> factorial(5)
    120
    >>> factorial(7)
    5040
    """

    if not is_natural_number(n):
        raise ValueError('n musi byc liczba naturalna')

    return functools.reduce(lambda a, b: a * b, range(1, n+1))


def fibonacci(n):
    """
    Iteracyjna wersja funkcji fibbonaci(n)

    >>> zad4_4(5)
    5
    >>> [zad4_4(x) for x in range(10)]
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """

    if not is_natural_number(n):
        raise ValueError('n musi byc liczba naturalna')

    if n in (0, 1):
        return n

    fib0, fib1 = 0, 1
    for i in range(2, n+1):
        fib0, fib1 = fib1, fib0 + fib1
    return fib1
