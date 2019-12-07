#!/usr/bin/env python3
"""Moduł testujący klasę CyclicList."""

import unittest
import cycliclist


class TestCyclicList(unittest.TestCase):

    def test_is_empty(self):
        self.assertTrue(cycliclist.CyclicList().is_empty())
        alist = cycliclist.CyclicList()
        alist.insert_head(cycliclist.Node(10))
        self.assertFalse(alist.is_empty())

    def test_insert_head(self):
        alist = cycliclist.CyclicList()
        alist.insert_head(cycliclist.Node('not head'))
        self.assertTrue(alist.head is alist.head.next)
        alist.insert_head(cycliclist.Node('head'))
        self.assertEqual(alist.head.data, 'head')
        self.assertTrue(alist.head is not alist.head.next)

    def test_insert_tail(self):
        alist = cycliclist.CyclicList()
        alist.insert_tail(cycliclist.Node('not tail'))
        self.assertTrue(alist.tail is alist.head)
        alist.insert_tail(cycliclist.Node('tail'))
        self.assertEqual(alist.tail.data, 'tail')
        self.assertTrue(alist.tail is not alist.head)

    def test_search_existing(self):
        alist = cycliclist.CyclicList()
        node = cycliclist.Node(5)
        alist.insert_tail(cycliclist.Node(1))
        alist.insert_tail(cycliclist.Node(2))
        alist.insert_tail(cycliclist.Node(3))
        alist.insert_tail(node)
        alist.insert_tail(cycliclist.Node(9))
        alist.insert_tail(cycliclist.Node(6))
        self.assertEqual(alist.search(5), node)

    def test_search_non_existing(self):
        alist = cycliclist.CyclicList()
        alist.insert_tail(cycliclist.Node(1))
        alist.insert_tail(cycliclist.Node(2))
        alist.insert_tail(cycliclist.Node(3))
        alist.insert_tail(cycliclist.Node(9))
        alist.insert_tail(cycliclist.Node(6))
        self.assertIsNone(alist.search(5))

    def test_remove_in_the_middle(self):
        alist = cycliclist.CyclicList()
        node = cycliclist.Node('to remove')
        alist.insert_tail(cycliclist.Node(1))
        alist.insert_tail(cycliclist.Node(2))
        alist.insert_tail(node)
        alist.insert_tail(cycliclist.Node(4))
        alist.insert_tail(cycliclist.Node(5))
        node_to_remove = alist.head.next.next
        self.assertEqual(alist.count(), 5)
        alist.remove(node_to_remove)
        self.assertNotEqual(alist.head.next.next, node_to_remove)
        self.assertEqual(alist.count(), 4)

    def test_remove_the_first(self):
        alist = cycliclist.CyclicList()
        node = cycliclist.Node('to remove')
        alist.insert_tail(node)
        alist.insert_tail(cycliclist.Node(2))
        alist.insert_tail(cycliclist.Node(3))
        alist.insert_tail(cycliclist.Node(4))
        alist.insert_tail(cycliclist.Node(5))
        node_to_remove = alist.head
        self.assertEqual(alist.count(), 5)
        alist.remove(node_to_remove)
        self.assertNotEqual(alist.head, node_to_remove)
        self.assertEqual(alist.count(), 4)

    def test_remove_the_last(self):
        alist = cycliclist.CyclicList()
        node = cycliclist.Node('to remove')
        alist.insert_tail(cycliclist.Node(1))
        alist.insert_tail(cycliclist.Node(2))
        alist.insert_tail(cycliclist.Node(3))
        alist.insert_tail(cycliclist.Node(4))
        alist.insert_tail(node)
        node_to_remove = alist.head.next.next.next.next
        self.assertEqual(alist.count(), 5)
        alist.remove(node_to_remove)
        self.assertNotEqual(alist.head.next.next.next.next, node_to_remove)
        self.assertEqual(alist.count(), 4)

    def test_remove_non_existing(self):
        alist = cycliclist.CyclicList()
        alist.insert_tail(cycliclist.Node('exists'))
        node = cycliclist.Node('does not exist')
        self.assertEqual(alist.count(), 1)
        alist.remove(node)
        self.assertEqual(alist.count(), 1)

    def test_remove_from_empty_list(self):
        alist = cycliclist.CyclicList()
        node = cycliclist.Node(30)
        with self.assertRaises(ValueError):
            alist.remove(node)

    def test_merge(self):
        self_list = cycliclist.CyclicList()
        other_list = cycliclist.CyclicList()
        for x in range(1, 4):
            self_list.insert_tail(cycliclist.Node(x))
        for y in range(4, 7):
            other_list.insert_tail(cycliclist.Node(y))

        self_list.merge(other_list)
        self.assertEqual(self_list.count(), 6)
        self.assertEqual(self_list.tail.data, 6)

    def test_merge_other_is_empty(self):
        self_list = cycliclist.CyclicList()
        other_list = cycliclist.CyclicList()
        self_list.insert_tail(cycliclist.Node(1))
        self_list.insert_tail(cycliclist.Node(2))
        self_list.insert_tail(cycliclist.Node(3))
        tail = self_list.tail
        self_list.merge(other_list)
        self.assertEqual(self_list.tail, tail)

    def test_merge_self_is_empty(self):
        self_list = cycliclist.CyclicList()
        other_list = cycliclist.CyclicList()
        other_list.insert_tail(cycliclist.Node(1))
        other_list.insert_tail(cycliclist.Node(2))
        other_list.insert_tail(cycliclist.Node(3))
        tail = other_list.tail
        self_list.merge(other_list)
        self.assertEqual(self_list.tail, tail)

    def test_clear(self):
        alist = cycliclist.CyclicList()
        alist.insert_tail(cycliclist.Node(1))
        alist.insert_tail(cycliclist.Node(2))
        alist.insert_tail(cycliclist.Node(3))
        self.assertEqual(alist.count(), 3)
        alist.clear()
        self.assertEqual(alist.count(), 0)
        self.assertEqual(alist.head, alist.tail)

    def test_clear_empty_list(self):
        alist = cycliclist.CyclicList()
        alist.clear()
        self.assertEqual(alist.count(), 0)

if __name__ == '__main__':
    unittest.main()
