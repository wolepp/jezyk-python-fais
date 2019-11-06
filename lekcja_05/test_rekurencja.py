"""
Testy jednostkowe modulu rekurencja.
"""
import unittest
import rekurencja


class TestRekurencja(unittest.TestCase):

    def setUp(self):
        self.factorial10 = 3628800
        self.fibonacci6 = 8

    def test_rekurencja_factorial(self):
        self.assertEqual(rekurencja.factorial(10), self.factorial10)

    def test_rekurencja_fibonacci(self):
        self.assertEqual(rekurencja.fibonacci(6), self.fibonacci6)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
