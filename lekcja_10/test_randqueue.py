#!/usr/bin/env python3
"""Moduł testujący implementację kolejki losowej."""

import randqueue
import unittest


class TestRandomQueue(unittest.TestCase):

    def test_insert(self):
        rq = randqueue.RandomQueue()
        rq.insert(3)
        rq.insert(1)
        rq.insert(-48)
        rq.insert(42)
        self.assertEqual(str(rq), '[3, 1, -48, 42]')

    def test_remove(self):
        rq = randqueue.RandomQueue()
        with self.assertRaises(Exception):
            rq.remove()

        items = [3, 1, -48, 42, (3, 2, 6), [12, -523], 'string']
        for item in items:
            rq.insert(item)

        while items:
            removed = rq.remove()
            print(rq) # żeby pokazać, że losowo
            self.assertIn(removed, items)
            items.remove(removed)

        self.assertEqual(items, [])

    def test_is_empty(self):
        rq = randqueue.RandomQueue()
        self.assertTrue(rq.is_empty())
        rq.insert(3)
        rq.insert([3, 5])
        self.assertFalse(rq.is_empty())

    def test_clear(self):
        rq = randqueue.RandomQueue()
        rq.insert(3)
        rq.insert(6)
        rq.clear()
        self.assertTrue(rq.is_empty())


if __name__ == "__main__":
    unittest.main()
