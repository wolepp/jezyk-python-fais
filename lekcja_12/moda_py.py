"""
Zadanie 12.5 - moda.

Metoda znajdowania mody (dominanty) w zbiorze nieuporządkowanym
z wykorzystaniem słownika Pythona.
"""
import unittest
import timeit
from operator import itemgetter


def moda_py(L, left, right):
    counter = {}
    while left <= right:
        counter[L[left]] = counter.get(L[left], 0) + 1
        left += 1
    return max(counter, key=counter.get)


class TestModaPy(unittest.TestCase):

    def test_moda_py_1(self):
        L = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9]
        moda = moda_py(L, 0, len(L)-1)
        self.assertEqual(moda, 1)

    def test_moda_py_2(self):
        L = [3, 2, 1, 3, 2, 1]
        moda = moda_py(L, 0, len(L)-1)
        self.assertEqual(moda, 3)


if __name__ == "__main__":
    unittest.main()
