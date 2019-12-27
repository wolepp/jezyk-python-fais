"""
Zawiera funkcje do generowania list z liczbami do testowania sortowań.
"""

import random
from math import sqrt
from matplotlib import pyplot


def random_integer_list(N):
    """
    Zwraca nieposortowaną listę liczb całkowitych od 0 do N-1.
    """
    random_integer_list.s = 'Liczby losowe'

    L = list(range(N))
    random.shuffle(L)
    return L


def nearly_sorted_integer_list(N):
    """
    Zwraca prawie posortowaną listę liczb całkowitych od 0 do N-1.
    """
    nearly_sorted_integer_list.s = 'Liczby prawie posortowane'

    if N >= 100:
        x = N // 30
    elif N >= 10:
        x = 9
    else:
        x = 4

    L = []
    for i in range(N):
        if i % x == 0:
            L.append(random.randrange(N))
        else:
            L.append(i)
    return L


def nearly_sorted_integer_list_reversed(N):
    """
    Zwraca prawie posortowaną odwrotną listę liczb całkowitych od 0 do N-1.
    """
    nearly_sorted_integer_list_reversed.s = 'Liczby prawie posortowane odwrotnie'

    L = nearly_sorted_integer_list(N)
    L.reverse()
    return L


def random_gauss_float_list(N):
    """
    Zwraca listę N liczb float w losowej kolejności o rozkładzie gaussowskim.
    """
    random_gauss_float_list.s = 'Losowe liczby float, rozkład gaussowski'

    L = []
    for i in range(N):
        L.append(random.gauss(0, 1))
    return L


def random_repeatable_integer_list(N):
    """
    Zwraca listę N liczb całkowitych należących do zbioru k-elementowego, 
    k < N w losowej kolejności.
    """
    random_repeatable_integer_list.s = 'Losowe powtarzające się liczby.'

    k = int(sqrt(N))
    L = []
    for i in range(N):
        L.append(random.randrange(k))
    return L


if __name__ == "__main__":
    random_integer_list.s = 'Random Integer List'
    nearly_sorted_integer_list.s = 'Nearly sorted integer list'
    nearly_sorted_integer_list_reversed.s = 'Nearly sorted integer list reversed'
    random_gauss_float_list.s = 'Random gauss float list'
    random_repeatable_integer_list.s = 'Random repeatable integer list'

    ROZMIARY = [
        9,
        58,
        250
    ]
    FUNKCJE = [
        random_integer_list,
        nearly_sorted_integer_list,
        nearly_sorted_integer_list_reversed,
        random_gauss_float_list,
        random_repeatable_integer_list
    ]

    # Uwaga, pokazywanych jest 15 wykresów, jeden po drugim.
    for funkcja in FUNKCJE:
        for rozmiar in ROZMIARY:
            pyplot.title('{}, N={}'.format(funkcja.s, str(rozmiar)))

            # pyplot.plot - kropki, pyplot.bar - kreski
            # pyplot.plot(range(rozmiar), funkcja(rozmiar), '.')
            pyplot.bar(range(rozmiar), funkcja(rozmiar))

            pyplot.show()
