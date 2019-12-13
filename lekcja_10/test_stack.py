import unittest
import stack


class TestStack(unittest.TestCase):

    def setUp(self):
        self.empty_stack = stack.Stack(3)
        self.full_stack = stack.Stack(3)
        self.full_stack.push(0)
        self.full_stack.push(1)
        self.full_stack.push(2)

    def test_init(self):
        with self.assertRaises(ValueError):
            S = stack.Stack(0)
        with self.assertRaises(ValueError):
            S = stack.Stack(-4)
        with self.assertRaises(ValueError):
            S = stack.Stack('ojej')

    def test_str(self):
        self.assertEqual(str(self.empty_stack), '[]')
        self.assertEqual(str(self.full_stack), '[0, 1, 2]')

    def test_is_empty(self):
        self.assertTrue(self.empty_stack.is_empty())

        self.assertFalse(self.full_stack.is_empty())
        self.assertFalse(stack.Stack(2).push(1))

    def test_is_full(self):
        self.assertTrue(self.full_stack.is_full())

        self.assertFalse(self.empty_stack.is_full())
        self.assertFalse(stack.Stack(2).push(1))

    def test_push(self):
        S = stack.Stack(3)

        with self.assertRaises(ValueError):
            S.push(-2)
        with self.assertRaises(ValueError):
            S.push(3)

        S.push(2)
        S.push(0)
        S.push(1)
        S.push(0)
        S.push(1)
        S.push(2)
        self.assertEqual(str(S), '[2, 0, 1]')

    def test_pop(self):
        S = stack.Stack(3)

        with self.assertRaises(Exception):
            S.pop()

        S.push(2)
        S.push(0)
        S.push(1)
        self.assertEqual(S.pop(), 1)
        self.assertEqual(S.pop(), 0)
        self.assertEqual(S.pop(), 2)

        with self.assertRaises(Exception):
            S.pop()


if __name__ == '__main__':
    unittest.main()
