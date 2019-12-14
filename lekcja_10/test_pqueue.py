#!/usr/bin/env python3
"""Moduł testujący implementację kolejki priorytetowej."""

import unittest
import pqueue


class TestPriorityQueue(unittest.TestCase):

    def setUp(self):
        # funkcje porównujące
        self.cmp_asc_num = lambda a, b: (b > a) - (b < a)
        self.cmp_asc_len = lambda a, b: \
            (len(str(b)) > len(str(a))) - (len(str(b)) < len(str(a)))
        self.cmp_desc_len = lambda a, b: \
            (len(str(a)) > len(str(b))) - (len(str(a)) < len(str(b)))

    def test_is_empty(self):
        pq = pqueue.PriorityQueue()
        self.assertTrue(pq.is_empty())

        pq.insert(3)
        pq.insert(4)
        pq.insert(2)
        self.assertFalse(pq.is_empty())

        pq.remove()
        pq.remove()
        pq.remove()
        self.assertTrue(pq.is_empty())

    def test_insert(self):
        pq = pqueue.PriorityQueue()
        pq.insert(3)
        pq.insert(4)
        pq.insert(2)
        self.assertEqual(str(pq), '[3, 4, 2]')

    def test_remove(self):
        pq = pqueue.PriorityQueue()
        pq.insert(3)
        pq.insert(45)
        pq.insert(-123)
        self.assertEqual(pq.remove(), 45)
        self.assertEqual(pq.remove(), 3)
        self.assertEqual(pq.remove(), -123)

    def test_remove_asc_num(self):
        pq = pqueue.PriorityQueue(self.cmp_asc_num)
        pq.insert(3)
        pq.insert(45)
        pq.insert(-123)
        self.assertEqual(pq.remove(), -123)
        self.assertEqual(pq.remove(), 3)
        self.assertEqual(pq.remove(), 45)

    def test_remove_desc_len(self):
        pq = pqueue.PriorityQueue(self.cmp_desc_len)
        pq.insert('g')
        pq.insert('zzz')
        pq.insert('bb')
        self.assertEqual(pq.remove(), 'zzz')
        self.assertEqual(pq.remove(), 'bb')
        self.assertEqual(pq.remove(), 'g')

    def test_remove_asc_len(self):
        pq = pqueue.PriorityQueue(self.cmp_asc_len)
        pq.insert('g')
        pq.insert('zzz')
        pq.insert('bb')
        self.assertEqual(pq.remove(), 'g')
        self.assertEqual(pq.remove(), 'bb')
        self.assertEqual(pq.remove(), 'zzz')


if __name__ == "__main__":
    unittest.main()
