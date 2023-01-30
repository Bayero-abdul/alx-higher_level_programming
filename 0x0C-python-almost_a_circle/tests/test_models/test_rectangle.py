#!/usr/bin/python3
"""this module contains testcases for Rectangle class."""


import unittest
import os
import sys
import io
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test case for Rectangle class."""

    @classmethod
    def setUpClass(self):
        self.r1 = Rectangle(10, 7, 2, 8)
        self.lst = []

    @classmethod
    def tearDownClass(self):
        if os.path.exists('Rectangle.json'):
            os.remove('Rectangle.json')

    def test_initialization(self):
        """test for initialization."""

        r1 = Rectangle(10, 2)
        self.assertIs(type(r1), Rectangle)
        r2 = Rectangle(10, 5, 6)
        self.assertTrue(type(r2), Rectangle)

    def test_width_attr(self):
        """test for width."""

        self.r1.width = 4
        self.assertEqual(self.r1.width, 4)

        types = ['3', None, '3.12', {'ella': 1}, [3, 5], (4, 5)]
        for t in types:
            with self.assertRaises(TypeError):
                Rectangle(t, 10)

        with self.assertRaises(ValueError):
            Rectangle(-10, 10)

        with self.assertRaises(ValueError):
            Rectangle(0, 10)

    def test_height_attr(self):
        """test for height."""

        r1 = Rectangle(10, 3)
        self.assertTrue(r1.height == 3)

        types = ['3', None, '3.12', {'ella': 1}, [3, 5], (4, 5)]
        for t in types:
            with self.assertRaises(TypeError):
                Rectangle(10, t)

        with self.assertRaises(ValueError):
            Rectangle(10, -10)

        with self.assertRaises(ValueError):
            Rectangle(10, 0)

    def test_x_attr(self):
        """test for x."""

        self.r1.x = 4
        self.assertEqual(self.r1.x, 4)

        types = ['3', None, '3.12', {'ella': 1}, [3, 5], (4, 5)]
        for t in types:
            with self.assertRaises(TypeError):
                Rectangle(10, 10, t)

        with self.assertRaises(ValueError):
            Rectangle(10, 10, -10)

    def test_y_attr(self):
        """test for y."""

        self.r1.y = 4
        self.assertEqual(self.r1.y, 4)

        types = ['3', None, '3.12', {'ella': 1}, [3, 5], (4, 5)]
        for t in types:
            with self.assertRaises(TypeError):
                Rectangle(10, 10, 10, t)

        with self.assertRaises(ValueError):
            Rectangle(10, 10, 10, -10)

    def test_area(self):
        """test for area()."""

        self.assertEqual(self.r1.area(), 70)

    def test_display(self):
        """test for display()."""

        output = "\n\n  ##\n  ##\n  ##\n"
        r1 = Rectangle(2, 3, 2, 2)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        r1.display()
        self.assertEqual(captured_output.getvalue(), output)

        output = "##\n##\n"
        r2 = Rectangle(2, 2)
        c_o = io.StringIO()
        sys.stdout = c_o
        r2.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(c_o.getvalue(), output)

        output = " ###\n ###\n"
        r3 = Rectangle(3, 2, 1)
        c_o = io.StringIO()
        sys.stdout = c_o
        r3.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(c_o.getvalue(), output)

    def test_update(self):
        """test for update()."""

        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), '[Rectangle] (89) 4/5 - 2/3')

        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), '[Rectangle] (89) 1/3 - 4/2')

        r1.update(None)
        self.assertEqual(str(r1), str(r1))


if __name__ == "__main__":
    unittest.main()
