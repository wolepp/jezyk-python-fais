#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce


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


def zad4_2_prostokat(x, y):
    """
    Zwraca prostokat o zadanych wymiarach.

    >>> zad4_2_prostokat(3,2)
    '+---+---+---+\\n|   |   |   |\\n+---+---+---+\\n|   |   |   |\\n+---+---+---+'
    >>> zad4_2_prostokat(0,1)
    '+\\n|\\n+'
    >>> zad4_2_prostokat(0,0)
    '+'
    >>> zad4_2_prostokat(-2,3)
    Traceback (most recent call last):
        ...
    ValueError: wymiar musi byc co najmniej rowny 0
    >>> zad4_2_prostokat(2,-3)
    Traceback (most recent call last):
        ...
    ValueError: wymiar musi byc co najmniej rowny 0
    >>> zad4_2_prostokat(2,'string')
    Traceback (most recent call last):
        ...
    TypeError: wymiar musi byc liczba
    """

    try:
        x = int(x)
        y = int(y)
    except ValueError:
        raise TypeError('wymiar musi byc liczba')
    if x < 0 or y < 0:
        raise ValueError('wymiar musi byc co najmniej rowny 0')

    prostokat = ''
    for i in range(y):
        prostokat += ('+---' * x) + '+\n'
        prostokat += ('|   ' * x) + '|\n'
    prostokat += ('+---' * x) + '+'
    return prostokat


def zad4_3(n):
    """
    Iteracyjna funkcja oblizająca silnię z n

    >>> zad4_3(5)
    120
    >>> zad4_3(-1)
    Traceback (most recent call last):
        ...
    ValueError: n musi byc naturalne
    >>> zad4_3('string')
    Traceback (most recent call last):
        ...
    TypeError: n musi byc liczba naturalna
    """

    try:
        n = int(n)
    except ValueError:
        raise TypeError('n musi byc liczba naturalna')
    if n < 0:
        raise ValueError('n musi byc naturalne')

    return reduce(lambda a, b: a * b, range(1, n+1))


def zad4_4(n):
    """
    Iteracyjna funkcja obliczająca n-ty wyraz ciągu Fibonacciego

    >>> zad4_4(5)
    5
    >>> [zad4_4(x) for x in range(10)]
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    >>> zad4_4(-1)
    Traceback (most recent call last):
        ...
    ValueError: n musi byc naturalne
    >>> zad4_4('string')
    Traceback (most recent call last):
        ...
    TypeError: n musi byc liczba naturalna
    """

    try:
        n = int(n)
    except ValueError:
        raise TypeError('n musi byc liczba naturalna')
    if n < 0:
        raise ValueError('n musi byc naturalne')

    if n == 0 or n == 1:
        return n

    fib0, fib1 = 0, 1
    for i in range(2, n+1):
        fib0, fib1 = fib1, fib0 + fib1
    return fib1


def odwracanie(L, left, right):
    """
    Odwraca kolejność elementów na liście od left do right włącznie.

    Obsluguje ujemne indeksy.
    >>> odwracanie(list(range(10)), 0, 9)
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    >>> odwracanie(list(range(10)), 2, 4)
    [0, 1, 4, 3, 2, 5, 6, 7, 8, 9]
    >>> odwracanie(list(range(10)), 3, -2)
    [0, 1, 2, 8, 7, 6, 5, 4, 3, 9]
    >>> odwracanie(list(range(10)), 8, 5)
    [0, 1, 2, 3, 4, 8, 7, 6, 5, 9]
    >>> odwracanie(list(range(10)), -7, -4)
    [0, 1, 2, 6, 5, 4, 3, 7, 8, 9]
    >>> odwracanie(3, 2, 5)
    Traceback (most recent call last):
        ...
    TypeError: L musi byc lista
    >>> odwracanie([0, 1], 3, 1)
    Traceback (most recent call last):
        ...
    IndexError: argument left poza lista
    >>> odwracanie([0, 1], 1, 4)
    Traceback (most recent call last):
        ...
    IndexError: argument right poza lista
    """

    if not isinstance(L, list):
        raise TypeError('L musi byc lista')
    try:
        left = int(left)
        right = int(right)
    except ValueError:
        raise TypeError('wartosci left i right musza byc liczbami calkowitymi')

    # obsluga ujemnych indeksow
    if left < 0:
        left = len(L) + left
    if right < 0:
        right = len(L) + right

    # sprawdz czy nie jest poza
    if left >= len(L):
        raise IndexError('argument left poza lista')
    if right >= len(L):
        raise IndexError('argument right poza lista')

    # nie rób nic, jeżeli left > right
    # if left > right:
    #     right, left = left, right

    while left < right:
        L[left], L[right] = L[right], L[left]
        left, right = left + 1, right - 1
    return L


def sum_seq(sequence):
    """
    Oblicza sumę liczb w sequence, która może mieć zagnieżdżone sekwencje.

    >>> sum_seq([1, 2, 3])
    6
    >>> sum_seq((1, 2, 3))
    6
    >>> sum_seq([[[], [3, 5], (2, 6)], 7, 8])
    31
    >>> sum_seq(4)
    Traceback (most recent call last):
        ...
    TypeError: sequence nie jest sekwencja
    >>> sum_seq('string')
    Traceback (most recent call last):
        ...
    TypeError: sequence nie jest sekwencja
    """

    if not isinstance(sequence, (list, tuple)):
        raise TypeError('sequence nie jest sekwencja')

    asum = 0
    for element in sequence:
        if isinstance(element, (list, tuple)):
            asum += sum_seq(element)
        else:
            asum += element
    return asum


def flatten(sequence):
    """
    Spłaszcza strukturę sequence, która może mieć zagnieżdżone sekwencje.

    >>> flatten([])
    []
    >>> flatten([1, 2, 3])
    [1, 2, 3]
    >>> flatten([1,(2,3),[],[4,(5,6,7)],8,[9]])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> flatten(3)
    Traceback (most recent call last):
        ...
    TypeError: sequence nie jest sekwencja
    >>> flatten('string')
    Traceback (most recent call last):
        ...
    TypeError: sequence nie jest sekwencja
    """

    if not isinstance(sequence, (list, tuple)):
        raise TypeError('sequence nie jest sekwencja')

    alist = []
    for element in sequence:
        if isinstance(element, (list, tuple)):
            alist.extend(flatten(element))
        else:
            alist.append(element)
    return alist


if __name__ == '__main__':
    import doctest
    doctest.testmod()
