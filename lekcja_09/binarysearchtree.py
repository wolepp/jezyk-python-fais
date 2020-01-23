"""
Zadanie 9.6 - BinaryTree

Rozwiązanie bez klasy BinaryTree
"""

import unittest


class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


def count_leafs(top):
    """Liczy liście drzewa binarnego."""

    leafs = 0
    if top is not None:
        if top.left:
            leafs += count_leafs(top.left)
        if top.right:
            leafs += count_leafs(top.right)
        if top.left is None and top.right is None:
            leafs += 1
    return leafs


def calc_total(top):
    """Liczy sumę liczb przechowywanych w drzewie binarnym."""

    calc = 0
    if top is not None:
        calc += top.data
        if top.left:
            calc += calc_total(top.left)
        if top.right:
            calc += calc_total(top.right)
    return calc


class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        self.root = Node(1)
        self.root.left = Node(2)
        self.root.right = Node(3)
        self.root.left.left = Node(4)
        self.root.left.right = Node(5)
        self.root.right.left = Node(6)
        self.root.right.right = Node(7)
        self.root.right.right.left = Node(8)
        #         1
        #       /   \
        #     2       3
        #    / \     / \
        #   4   5   6   7
        #              /
        #             8

    def test_count_leafs(self):
        self.assertEqual(count_leafs(self.root), 4)

    def test_calc_total(self):
        self.assertEqual(calc_total(self.root), 36)


if __name__ == '__main__':
    unittest.main()
