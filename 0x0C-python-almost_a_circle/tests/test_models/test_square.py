#!/usr/bin/python3
"""this module contains testcases for Square class."""


import unittest
import os
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test case for Square class."""

    @classmethod
    def tearDownClass(self):

        if os.path.exists('Square.json'):
            os.remove('Square.json')

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

        with self.assertRaises(ValueError):
            Square(0)

        with self.assertRaises(ValueError):
            Square(-1)

        with self.assertRaises(TypeError):
            Square("6")

    def test_x_attr(self):
        """test for x."""

        s1 = Square(1, 3)
        self.assertTrue(s1.x == 3)

        with self.assertRaises(TypeError):
            Square(1, "2")

        with self.assertRaises(ValueError):
            Square(1, -1)

    def test_y_attr(self):
        """test for y."""

        s2 = Square(1, 3, 4)
        self.assertTrue(s2.y == 4)

        with self.assertRaises(TypeError):
            Square(1, 3, "6")

        with self.assertRaises(ValueError):
            Square(1, 3, -3)

    def test_id_attr(self):
        """test for id."""

        s1 = Square(2, 5, 7, 5)
        self.assertTrue(s1.id == 5)

    def test_update(self):
        """test for update()."""

        s1 = Square(5)

        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), '[Square] (1) 3/4 - 2')

        s1.update(size=7, id=89, x=7, y=1)
        self.assertEqual(str(s1), '[Square] (89) 7/1 - 7')

        s1.update(None)
        self.assertEqual(str(s1), str(s1))

    def test_save_to_file(self):
        """test save_to_file()."""

        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertTrue('[]', f.read())

        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertTrue('[]', f.read())


if __name__ == "__main__":
    unittest.main()
