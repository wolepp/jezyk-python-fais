"""
Zadanie 12.2 - wyszukiwanie binarne.

Rekurencyjna wersja wyszukiwania binarnego.
"""

import unittest


def binarne_rek(L, left, right, y):
    """Wyszukiwanie binarne w wersji rekurencyjnej."""
    if left <= right:
        k = (left + right) // 2
        if y == L[k]:
            return k
        if y > L[k]:
            return binarne_rek(L, k+1, right, y)
        else:
            return binarne_rek(L, left, k-1, y)
    return None


class TestBinarneRek(unittest.TestCase):

    def test_binarne_rek_1(self):
        L = list(range(10))
        idx = binarne_rek(L, 0, 9, 5)
        self.assertEqual(idx, 5)

    def test_binarne_rek_2(self):
        L = [1, 3, 4, 5, 6, 100, 122, 123, 900]
        idx = binarne_rek(L, 0, len(L)-1, 3)
        self.assertEqual(idx, 1)

    def test_binarne_rek_3(self):
        L = [-5, -4, 0, 10, 44400, 44430, 44456]
        idx = binarne_rek(L, 0, len(L)-1, 44456)
        self.assertEqual(idx, 6)

    def test_binarne_rek_non_existing(self):
        L = [-5, -4, 0, 10, 44400, 44430, 44456]
        idx = binarne_rek(L, 0, len(L)-1, 99999)
        self.assertIsNone(idx)
        idx = binarne_rek(L, 0, len(L)-1, -1000)
        self.assertIsNone(idx)
        idx = binarne_rek(L, 0, len(L)-1, 1)
        self.assertIsNone(idx)


if __name__ == "__main__":
    unittest.main()
