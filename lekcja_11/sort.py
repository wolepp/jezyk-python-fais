"""
W module porównywane są czasy sortowań: insertsort, selectsort
shellsort, timsort.
"""
import timeit
from matplotlib import pyplot as plt
import sort_test_data as data


def swap(L, left, right):
    """Zamiana miejscami dwóch elementów."""
    # L[left], L[right] = L[right], L[left]
    item = L[left]
    L[left] = L[right]
    L[right] = item


def insertsort(L, left, right):
    for i in range(left+1, right+1):   # L[left] jest posortowany
        item = L[i]
        j = i
        while j > left and L[j-1] > item:
            L[j] = L[j-1]   # robimy miejsce na item
            j = j-1
        L[j] = item


def selectsort(L, left, right):
    for i in range(left, right):
        k = i
        for j in range(i+1, right+1):
            if L[j] < L[k]:
                k = j
        item = L[k]
        while k > i:
            L[k] = L[k-1]
            k = k-1
        L[i] = item


def shellsort(L, left, right):
    # Wersja wg Kernighana i Ritchiego.
    # Oryginalna sekwencja przyrostów Shella: 1, 2, 4, 8, 16, 32, ...
    # Metoda degeneruje się do czasu kwadratowego dla złośliwych danych.
    h = (right - left) // 2
    while h > 0:
        for i in range(left + h, right + 1):
            for j in range(i, left + h - 1, -h):
                if L[j - h] > L[j]:
                    swap(L, j - h, j)
        h = h // 2


if __name__ == "__main__":

    listy = [
        data.random_integer_list,
        data.nearly_sorted_integer_list,
        data.nearly_sorted_integer_list_reversed,
        data.random_gauss_float_list,
        data.random_repeatable_integer_list
    ]

    N = [
        10**2,
        10**3,
        # 10**4,
        # 10**5,
        # 10**6
    ]

    for n in N:
        for lista in listy:
            shellsort_time = timeit.timeit(lambda: shellsort(
                lista(n), 0, n-1), number=3)
            insertsort_time = timeit.timeit(lambda: insertsort(
                lista(n), 0, n-1), number=3)
            selectsort_time = timeit.timeit(lambda: selectsort(
                lista(n), 0, n-1), number=3)
            timsort_time = timeit.timeit(lambda: lista(n).sort(), number=3)

            print('{}, N={}, średni czas: {:.4f}'.format(
                lista.s, n, shellsort_time/3))
            print('{}, N={}, średni czas: {:.4f}'.format(
                lista.s, n, insertsort_time/3))
            print('{}, N={}, średni czas: {:.4f}'.format(lista.s, n, selectsort_time/3))
            print('{}, N={}, średni czas: {:.4f}'.format(
                lista.s, n, timsort_time/3))
