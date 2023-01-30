#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests class for testing Maximum integer in a list."""

    def test_list_ints(self):
        self.assertEqual(max_integer([3, -1, 9]), 9)
        self.assertEqual(max_integer([-1, -5, -4]), -1)
        self.assertEqual(max_integer([9]), 9)
        self.assertEqual(max_integer([4, 7, 3]), 7)

    def test_empty_list(self):
        self.assertEqual(max_integer(), None)

    def test_typeerorrs(self):
        with self.assertRaises(TypeError):
            max_integer(4)

        with self.assertRaises(TypeError):
            max_integer([4, "43", 6])


if __name__ == '__main__':
    unittest.main(verbosity=2)
