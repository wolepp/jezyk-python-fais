"""Moduł testujący klasę SingleList."""

import unittest
import singlelist


class TestSingleList(unittest.TestCase):
    def test_is_empty(self):
        self.assertTrue(singlelist.SingleList().is_empty())
        self.assertFalse(singlelist.SingleList()
                         .insert_head(singlelist.Node(10)))

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
        self.assertTrue(alist.head is not alist.tail)
        alist.remove_head()
        self.assertTrue(alist.head is None)
        self.assertTrue(alist.tail is None)


if __name__ == '__main__':
    unittest.main()
