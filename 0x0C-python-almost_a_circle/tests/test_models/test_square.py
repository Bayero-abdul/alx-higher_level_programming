#!/usr/bin/python3
"""this module contains testcases for Square class."""


import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test case for Square class."""

    def test_size(self):
        """test for size."""

        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(s1.size, 10)

        with self.assertRaises(ValueError):
            s1.size = -10

        with self.assertRaises(TypeError):
            s1.size = "10"

    def test_update(self):
        """test for update()."""

        s1 = Square(5)

        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), '[Square] (1) 3/4 - 2')

        s1.update(size=7, id=89, x=7, y=1)
        self.assertEqual(str(s1), '[Square] (89) 7/1 - 7')

        s1.update(None)
        self.assertEqual(str(s1), str(s1))


if __name__ == "__main__":
    unittest.main()
