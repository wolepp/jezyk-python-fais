#!/usr/bin/env python3
"""
Zadanie 6.1

Wojciech Lepich
"""

import unittest


class Time:
    """Klasa reprezentująca odcinek czasu."""

    def __init__(self, s=0):
        """Zwraca instancję klasy Time."""
        self.s = int(s)

    def __str__(self):
        """Zwraca string 'hh:mm:ss'."""
        h = self.s // 3600
        sec = self.s - h * 3600
        m = sec // 60
        sec = sec - m * 60
        return "{0:02d}:{1:02d}:{2:02d}".format(h, m, sec)
        # 4834 : 01:20:34

    def __repr__(self):
        """Zwraca string 'Time(s)'."""
        return "Time({0})".format(self.s)

    def __add__(self, other):
        """Dodawanie odcinków czasu."""
        return Time(self.s + other.s)

#   def __cmp__(self, other):           # porównywanie, -1|0|+1
#       """Porównywanie odcinków czasu."""
#       return cmp(self.s, other.s)

    def __lt__(self, other):    	# <
        return self.s < other.s

    def __gt__(self, other):    	# >
        return self.s > other.s

    def __le__(self, other):    	# <=
        return self.s <= other.s

    def __ge__(self, other):    	# >=
        return self.s >= other.s

    def __eq__(self, other):    	# ==
        return self.s == other.s

    def __ne__(self, other):            # !=
        return self.s != other.s

    def __int__(self):                  # int(time1)
        """Konwersja odcinka czasu do int."""
        return self.s

# Kod testujący moduł.


class TestTime(unittest.TestCase):

    def setUp(self):
        pass

    def test_print(self):               # test str() i repr()
        self.assertEqual(str(Time(4834)), '01:20:34')
        self.assertEqual(str(Time(1)), '00:00:01')
        self.assertEqual(str(Time(65)), '00:01:05')
        self.assertEqual(str(Time(86399)), '23:59:59')
        self.assertEqual(str(Time(86400)), '24:00:00')

    def test_add(self):
        self.assertEqual(Time(1) + Time(2), Time(3))
        self.assertEqual(Time(50) + Time(0), Time(50))

    def test_lt(self):
        self.assertTrue(Time(2) < Time(3))
        self.assertTrue(Time(5) < Time(8))
        self.assertFalse(Time(10) < Time(1))

    def test_gt(self):
        self.assertTrue(Time(3) > Time(2))
        self.assertTrue(Time(7) > Time(3))
        self.assertFalse(Time(3) > Time(9))

    def test_le(self):
        self.assertTrue(Time(3) <= Time(3))
        self.assertTrue(Time(3) <= Time(30))
        self.assertFalse(Time(30) <= Time(9))

    def test_ge(self):
        self.assertTrue(Time(3) >= Time(3))
        self.assertTrue(Time(6) >= Time(3))
        self.assertFalse(Time(4) >= Time(8))

    def test_eq(self):
        self.assertTrue(Time(1) == Time(1))
        self.assertTrue(Time(100) == Time(100))
        self.assertFalse(Time(1) == Time(900))

    def test_ne(self):
        self.assertTrue(Time(1) != Time(2))
        self.assertTrue(Time(4) != Time(2))
        self.assertFalse(Time(5) != Time(5))

    def test_int(self):
        self.assertEqual(int(Time(10)), 10)
        self.assertEqual(int(Time(6500)), 6500)
        self.assertNotEqual(int(Time(50)), 49)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()     # wszystkie testy
