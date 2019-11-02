#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# TODO: sprawdzic kodowanie!

def zad4_2_miarka(length):
    """
    Zwraca miarke zadanej dlugosci.

    >>> zad4_2_miarka(5)
    '|....|....|....|....|....|\\n0    1    2    3    4    5'
    >>> zad4_2_miarka(0)
    '|\\n0'
    >>> zad4_2_miarka(-3)
    Traceback (most recent call last):
        ...
    ValueError: dlugosc musi byc wieksza niz 0
    >>> zad4_2_miarka('string')
    Traceback (most recent call last):
        ...
    TypeError: dlugosc musi byc liczba
    """
    
    try:
        length = int(length)
    except ValueError:
        raise TypeError('dlugosc musi byc liczba')
    if length < 0:
        raise ValueError('dlugosc musi byc wieksza niz 0')

    miarka = ('|....' * length) + '|'
    miarka += '\n0'
    for i in range(1, length+1):
        miarka += ("%5d" % i)
    return miarka

def zad4_2_prostokat():
    x = int(input('dlugosc prostokota: '))
    y = int(input('wysokosc prostokota: '))
    prostokat = ''
    for i in range(y):
        prostokat += ('+---' * x) + '+\n'
        prostokat += ('|   ' * x) + '|\n'
    prostokat += ('+---' * x) + '+'
    return prostokat

def zad4_3(n):
    """Iteracyjna wersja funkcji factorial(n)."""

    if n < 0:
        raise ValueError('n musi byc naturalne')
    silnia = 1
    for i in range(1, n+1):
        silnia *= i
    return silnia

def zad4_4(n):
    """Iteracyjna wersja funkcji fibbonaci(n)"""

    if n < 0:
        raise ValueError('n musi byc naturalne')
    if n == 0 or n == 1:
        return n
    fib0, fib1 = 0, 1
    for i in range(2, n+1):
        fib0, fib1 = fib1, fib0 + fib1
    return fib1

def odwracanie(L, left, right):
    """odwraca kolejnosc elementow na liscie od left do right wlacznie."""

    if not isinstance(L, list):
        raise TypeError('L musi byc lista')


def zad4_6():
    pass

def zad4_7():
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()


