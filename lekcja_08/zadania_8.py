"""
Rozwiązania zadań z zestawu 8.

Wojciech Lepich
"""

import random
import math


def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""
    pass


def calc_pi(n=100):
    """Obliczanie liczby pi metodą Monte Carlo.
    n oznacza liczbę losowanych punktów."""

    w_kole = 0
    for i in range(0, n):
        x = random.random()
        y = random.random()
        if x*x + y*y < 1.0:
            w_kole += 1
    return 4 * w_kole / n


def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru
    Herona. Długości boków trójkąta wynoszą a, b, c."""

    p = (a + b + c) / 2
    if not (a < b+c and b < a+c and c < a+b
            and 2*a < 2*p and 2*b < 2*p and 2*c < 2*p
            and p-a > 0 and p-b > 0 and p-c > 0):
        raise ValueError('Liczby a, b, c nie są długościami boków trójkąta.')

    return math.sqrt(p*(p-a)*(p-b)*(p-c))


P_VALUES = {0: {0: 0.5}}


def P(i, j):
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
