"""
Zadanie 12.1 - wyszukiwanie liniowe.

Program na listę L wstawia n liczb wylosowanych z zakresu od 0 do k-1.
Program losuje liczbę y z tego samego zakresu i znajduje wszystkie jej
wystąpienia przy pomocy wyszukiwania liniowego.
"""

import random


if __name__ == "__main__":
    n, k = 100, 10
    L = [random.randrange(0, k) for i in range(n)]

    y = random.randrange(0, k)
    wystapienia = []
    for (indeks, liczba) in enumerate(L):
        if liczba == y:
            wystapienia.append(indeks)

    print('{} jest na pozycjach: {}'.format(y, wystapienia))
    print(L)
