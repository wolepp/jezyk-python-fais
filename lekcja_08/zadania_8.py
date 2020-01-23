#!/usr/bin/env python3
"""
Rozwiązania zadań z zestawu 8.

Wojciech Lepich
"""

import random
import math


def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""

    if a == 0 and b == 0:
        print('a i b nie mogą być równocześnie równe 0')
    elif b == 0:
        print("b = 0 => ax + by + c = ax + c = 0")
        print("prosta równoległa do osi OY, przecina oś OX w punkcie")
        print("x = -c/a =", -c/a)
    elif a == 0:
        print("a = 0 => ax + by + c = by + c = 0")
        print("prosta równoległa do osi OX, przecina oś OY w punkcie")
        print("y = -c/b =", -c/b)
    else:  # a != 0 and b != 0
        print("równanie kierunkowej prostej")
        print("ax + by + c => y = -(a/b)*x - c/b")
        print("prosta przecina oś OX w punkcie x = ", -c/a)
        print("prosta przecina oś OY w punkcie y = ", -c/b)

    if c == 0 and not (a == 0 and b == 0):
        print("prosta przechodzi przez początek układu współrzędnych")


def calc_pi(n=100):
    """Obliczanie liczby pi metodą Monte Carlo.

    n oznacza liczbę losowanych punktów.
    """

    w_kole = 0
    for i in range(0, n):
        x = random.random()
        y = random.random()
        if x*x + y*y < 1.0:
            w_kole += 1
    return 4 * w_kole / n


def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta.

    Wykorzystuje wzór Herona. Długości boków trójkąta wynoszą a, b, c.
    """

    p = (a + b + c) / 2
    if not (a < b+c and b < a+c and c < a+b
            and 2*a < 2*p and 2*b < 2*p and 2*c < 2*p
            and p-a > 0 and p-b > 0 and p-c > 0):
        raise ValueError('Liczby a, b, c nie są długościami boków trójkąta.')

    return math.sqrt(p*(p-a)*(p-b)*(p-c))


P_VALUES = {0: {0: 0.5}}


def P(i, j):
    """Oblicza wartość funkcji P(i, j):

    P(0, 0) = 0.5,
    P(i, 0) = 0.0 dla i > 0,
    P(0, j) = 1.0 dla j > 0,
    P(i, j) = 0.5 * (P(i-1), j) + P(i, j-1)), dla i, j > 0
    """

    if i < 0 or j < 0:
        raise ValueError('Argumenty muszą być nieujemne.')

    if i == 0 and j == 0:
        return 0.5
    if i == 0:
        return 1.0
    if j == 0:
        return 0.0

    global P_VALUES
    if not i in P_VALUES:
        P_VALUES[i] = {j: 0.5 * (P(i-1, j) + P(i, j-1))}
    elif not j in P_VALUES[i]:
        P_VALUES[i][j] = 0.5 * (P(i-1, j) + P(i, j-1))

    return P_VALUES[i][j]
