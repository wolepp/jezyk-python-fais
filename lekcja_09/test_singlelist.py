#!/usr/bin/env python3
"""Moduł testujący klasę SingleList."""

import unittest
import singlelist


class TestSingleList(unittest.TestCase):
    def test_is_empty(self):
        self.assertTrue(singlelist.SingleList().is_empty())
        alist = singlelist.SingleList()
        alist.insert_head(singlelist.Node(10))
        self.assertFalse(alist.is_empty())

    def test_count(self):
        alist = singlelist.SingleList()
        self.assertEqual(alist.count(), 0)
        alist.insert_head(singlelist.Node(1))
        alist.insert_head(singlelist.Node(2))
        alist.insert_head(singlelist.Node(3))
        self.assertEqual(alist.count(), 3)

    def test_insert_head(self):
        alist = singlelist.SingleList()
        alist.insert_head(singlelist.Node('not head'))
        self.assertTrue(alist.head is alist.tail)
        alist.insert_head(singlelist.Node('head'))
        self.assertEqual(alist.head.data, singlelist.Node('head').data)
        self.assertTrue(alist.head is not alist.tail)

    def test_insert_tail(self):
        alist = singlelist.SingleList()
        alist.insert_tail(singlelist.Node('not tail'))
        self.assertTrue(alist.head is alist.tail)
        alist.insert_tail(singlelist.Node('tail'))
        self.assertEqual(alist.tail.data, singlelist.Node('tail').data)
        self.assertTrue(alist.head is not alist.tail)

    def test_remove_head(self):
        alist = singlelist.SingleList()
        node_to_remove = singlelist.Node('head to remove')
        alist.insert_head(singlelist.Node('final head'))
        alist.insert_head(node_to_remove)
        removed_node = alist.remove_head()
        self.assertEqual(alist.head.data, singlelist.Node('final head').data)
        self.assertEqual(removed_node, node_to_remove)

    def test_remove_head_empty_list(self):
        alist = singlelist.SingleList()
        with self.assertRaises(ValueError):
            alist.remove_head()

    def test_remove_head_one_element_list(self):
        alist = singlelist.SingleList()
        alist.insert_head(singlelist.Node('the only one'))
        self.assertTrue(alist.head is alist.tail and alist.head is not None)
        alist.remove_head()
        self.assertTrue(alist.head is None)
        self.assertTrue(alist.tail is None)

    def test_remove_tail(self):
        alist = singlelist.SingleList()
        node_to_remove = singlelist.Node('tail to remove')
        alist.insert_tail(singlelist.Node('final tail'))
        alist.insert_tail(node_to_remove)
        removed_node = alist.remove_tail()
        self.assertEqual(alist.tail.data, 'final tail')
        self.assertEqual(removed_node, node_to_remove)

    def test_remove_tail_empty_list(self):
        alist = singlelist.SingleList()
        with self.assertRaises(ValueError):
            alist.remove_tail()

    def test_remove_tail_one_element_list(self):
        alist = singlelist.SingleList()
        alist.insert_tail(singlelist.Node('the only one'))
        self.assertTrue(alist.head is alist.tail and alist.head is not None)
        alist.remove_tail()
        self.assertTrue(alist.head is None)
        self.assertTrue(alist.tail is None)

    def test_merge(self):
        self_list = singlelist.SingleList()
        other_list = singlelist.SingleList()
        for x in range(1, 4):
            self_list.insert_tail(singlelist.Node(x))
        for y in range(4, 7):
            other_list.insert_tail(singlelist.Node(y))

        self_list.merge(other_list)
        self.assertEqual(self_list.count(), 6)
        self.assertEqual(self_list.tail.data, 6)

    def test_merge_other_is_empty(self):
        self_list = singlelist.SingleList()
        other_list = singlelist.SingleList()
        self_list.insert_tail(singlelist.Node(1))
        self_list.insert_tail(singlelist.Node(2))
        self_list.insert_tail(singlelist.Node(3))
        tail = self_list.tail
        self_list.merge(other_list)
        self.assertEqual(self_list.tail, tail)

    def test_merge_self_is_empty(self):
        self_list = singlelist.SingleList()
        other_list = singlelist.SingleList()
        other_list.insert_tail(singlelist.Node(1))
        other_list.insert_tail(singlelist.Node(2))
        other_list.insert_tail(singlelist.Node(3))
        tail = other_list.tail
        self_list.merge(other_list)
        self.assertEqual(self_list.tail, tail)

    def test_clear(self):
        alist = singlelist.SingleList()
        alist.insert_tail(singlelist.Node(1))
        alist.insert_tail(singlelist.Node(2))
        alist.insert_tail(singlelist.Node(3))
        self.assertEqual(alist.count(), 3)
        alist.clear()
        self.assertEqual(alist.count(), 0)

    def test_clear_empty_list(self):
        alist = singlelist.SingleList()
        alist.clear()
        self.assertEqual(alist.count(), 0)

    def test_search_existing(self):
        alist = singlelist.SingleList()
        node = singlelist.Node(5)
        alist.insert_tail(singlelist.Node(1))
        alist.insert_tail(singlelist.Node(2))
        alist.insert_tail(singlelist.Node(3))
        alist.insert_tail(node)
        alist.insert_tail(singlelist.Node(9))
        alist.insert_tail(singlelist.Node(6))
        self.assertEqual(alist.search(5), node)

    def test_search_non_existing(self):
        alist = singlelist.SingleList()
        alist.insert_tail(singlelist.Node(1))
        alist.insert_tail(singlelist.Node(2))
        alist.insert_tail(singlelist.Node(3))
        alist.insert_tail(singlelist.Node(9))
        alist.insert_tail(singlelist.Node(6))
        self.assertIsNone(alist.search(5))

    def test_find_min(self):
        alist = singlelist.SingleList()
        node = singlelist.Node(1)
        alist.insert_tail(node)
        alist.insert_tail(singlelist.Node(2))
        alist.insert_tail(singlelist.Node(3))
        alist.insert_tail(singlelist.Node(9))
        alist.insert_tail(singlelist.Node(6))
        self.assertEqual(alist.find_min(), node)

    def test_find_min_empty_list(self):
        alist = singlelist.SingleList()
        self.assertIsNone(alist.find_min())

    def test_find_max(self):
        alist = singlelist.SingleList()
        node = singlelist.Node(9)
        alist.insert_tail(singlelist.Node(1))
        alist.insert_tail(singlelist.Node(2))
        alist.insert_tail(singlelist.Node(3))
        alist.insert_tail(node)
        alist.insert_tail(singlelist.Node(6))
        self.assertEqual(alist.find_max(), node)

    def test_find_max_empty_list(self):
        alist = singlelist.SingleList()
        self.assertIsNone(alist.find_max())

    def test_reverse(self):
        alist = singlelist.SingleList()
        alist.insert_tail(singlelist.Node(1))
        alist.insert_tail(singlelist.Node(2))
        alist.insert_tail(singlelist.Node(3))
        alist.insert_tail(singlelist.Node(9))
        alist.insert_tail(singlelist.Node(6))
        head, tail = alist.head, alist.tail
        alist.reverse()
        self.assertEqual(alist.head, tail)
        self.assertEqual(alist.tail, head)

    def test_reverse_empty(self):
        alist = singlelist.SingleList()
        head, tail = alist.head, alist.tail
        alist.reverse()
        self.assertEqual(alist.head, tail)
        self.assertEqual(alist.tail, head)

if __name__ == '__main__':
    unittest.main()
