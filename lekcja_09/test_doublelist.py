#!/usr/bin/env python3
"""Moduł testujący klasę DoubleList."""

import unittest
import doublelist


class TestDoubleList(unittest.TestCase):
    def test_is_empty(self):
        self.assertTrue(doublelist.DoubleList().is_empty())
        alist = doublelist.DoubleList()
        alist.insert_head(doublelist.Node(10))
        self.assertFalse(alist.is_empty())

    def test_count(self):
        alist = doublelist.DoubleList()
        self.assertEqual(alist.count(), 0)
        alist.insert_head(doublelist.Node(1))
        alist.insert_head(doublelist.Node(2))
        alist.insert_head(doublelist.Node(3))
        self.assertEqual(alist.count(), 3)

    def test_insert_head(self):
        alist = doublelist.DoubleList()
        head_node = doublelist.Node('head')
        alist.insert_head(doublelist.Node('not head'))
        alist.insert_head(head_node)
        self.assertEqual(alist.nil.next, head_node)
        self.assertNotEqual(alist.nil.prev, head_node)
        self.assertEqual(alist.length, 2)

    def test_insert_tail(self):
        alist = doublelist.DoubleList()
        tail_node = doublelist.Node('head')
        alist.insert_tail(doublelist.Node('not tail'))
        alist.insert_tail(tail_node)
        self.assertEqual(alist.nil.prev, tail_node)
        self.assertNotEqual(alist.nil.next, tail_node)
        self.assertEqual(alist.length, 2)

    def test_remove_head(self):
        alist = doublelist.DoubleList()
        node_to_remove = doublelist.Node('head to remove')
        alist.insert_head(doublelist.Node('final head'))
        alist.insert_head(node_to_remove)
        length = alist.count()
        removed_node = alist.remove_head()
        self.assertEqual(alist.nil.next.data,
                         doublelist.Node('final head').data)
        self.assertEqual(removed_node, node_to_remove)
        self.assertEqual(alist.count(), length - 1)

    def test_remove_head_empty_list(self):
        alist = doublelist.DoubleList()
        with self.assertRaises(ValueError):
            alist.remove_head()

    def test_remove_head_one_element_list(self):
        alist = doublelist.DoubleList()
        alist.insert_head(doublelist.Node('the only one'))
        self.assertTrue(alist.nil.next is alist.nil.prev
                        and alist.nil.next is not alist.nil)
        alist.remove_head()
        self.assertTrue(alist.nil.next is alist.nil)
        self.assertTrue(alist.nil.prev is alist.nil)

    def test_remove_tail(self):
        alist = doublelist.DoubleList()
        node_to_remove = doublelist.Node('tail to remove')
        alist.insert_tail(doublelist.Node('final tail'))
        alist.insert_tail(node_to_remove)
        length = alist.count()
        removed_node = alist.remove_tail()
        self.assertEqual(alist.nil.prev.data, 'final tail')
        self.assertEqual(removed_node, node_to_remove)
        self.assertEqual(alist.count(), length - 1)

    def test_remove_tail_empty_list(self):
        alist = doublelist.DoubleList()
        with self.assertRaises(ValueError):
            alist.remove_tail()

    def test_remove_tail_one_element_list(self):
        alist = doublelist.DoubleList()
        alist.insert_tail(doublelist.Node('the only one'))
        self.assertTrue(alist.nil.next is alist.nil.prev
                        and alist.nil.next is not alist.nil)
        alist.remove_tail()
        self.assertTrue(alist.nil.next is alist.nil)
        self.assertTrue(alist.nil.prev is alist.nil)

    def test_find_min(self):
        alist = doublelist.DoubleList()
        node = doublelist.Node(1)
        alist.insert_tail(node)
        alist.insert_tail(doublelist.Node(2))
        alist.insert_tail(doublelist.Node(3))
        alist.insert_tail(doublelist.Node(9))
        alist.insert_tail(doublelist.Node(6))
        self.assertEqual(alist.find_min(), node)

    def test_find_min_empty_list(self):
        aslit = doublelist.DoubleList()
        self.assertIsNone(aslit.find_min())

    def test_find_max(self):
        alist = doublelist.DoubleList()
        node = doublelist.Node(9)
        alist.insert_tail(doublelist.Node(1))
        alist.insert_tail(doublelist.Node(2))
        alist.insert_tail(doublelist.Node(3))
        alist.insert_tail(node)
        alist.insert_tail(doublelist.Node(6))
        self.assertEqual(alist.find_max(), node)

    def test_find_max_empty_list(self):
        alist = doublelist.DoubleList()
        self.assertIsNone(alist.find_max())

    def test_remove_in_the_middle(self):
        alist = doublelist.DoubleList()
        node = doublelist.Node('to remove')
        alist.insert_tail(doublelist.Node(1))
        alist.insert_tail(doublelist.Node(2))
        alist.insert_tail(node)
        alist.insert_tail(doublelist.Node(4))
        alist.insert_tail(doublelist.Node(5))
        node_to_remove = alist.nil.next.next.next
        self.assertEqual(alist.count(), 5)
        alist.remove(node_to_remove)
        self.assertNotEqual(alist.nil.next.next.next, node_to_remove)
        self.assertEqual(alist.count(), 4)

    def test_remove_the_first(self):
        alist = doublelist.DoubleList()
        node = doublelist.Node('to remove')
        alist.insert_tail(node)
        alist.insert_tail(doublelist.Node(2))
        alist.insert_tail(doublelist.Node(3))
        alist.insert_tail(doublelist.Node(4))
        alist.insert_tail(doublelist.Node(5))
        node_to_remove = alist.nil.next
        self.assertEqual(alist.count(), 5)
        alist.remove(node_to_remove)
        self.assertNotEqual(alist.nil.next, node_to_remove)
        self.assertEqual(alist.count(), 4)

    def test_remove_the_last(self):
        alist = doublelist.DoubleList()
        node = doublelist.Node('to remove')
        alist.insert_tail(doublelist.Node(1))
        alist.insert_tail(doublelist.Node(2))
        alist.insert_tail(doublelist.Node(3))
        alist.insert_tail(doublelist.Node(4))
        alist.insert_tail(node)
        node_to_remove = alist.nil.next.next.next.next.next
        self.assertEqual(alist.count(), 5)
        alist.remove(node_to_remove)
        self.assertNotEqual(alist.nil.next.next.next.next.next, node_to_remove)
        self.assertEqual(alist.count(), 4)

    def test_remove_non_existing(self):
        alist = doublelist.DoubleList()
        alist.insert_tail(doublelist.Node('exists'))
        node = doublelist.Node('does not exist')
        self.assertEqual(alist.count(), 1)
        alist.remove(node)
        self.assertEqual(alist.count(), 1)

    def test_remove_from_empty_list(self):
        alist = doublelist.DoubleList()
        node = doublelist.Node(30)
        with self.assertRaises(ValueError):
            alist.remove(node)

    def test_clear(self):
        alist = doublelist.DoubleList()
        alist.insert_tail(doublelist.Node(1))
        alist.insert_tail(doublelist.Node(2))
        alist.insert_tail(doublelist.Node(3))
        self.assertEqual(alist.count(), 3)
        alist.clear()
        self.assertEqual(alist.count(), 0)

    def test_clear_empty_list(self):
        alist = doublelist.DoubleList()
        alist.clear()
        self.assertEqual(alist.count(), 0)



if __name__ == '__main__':
    unittest.main()
