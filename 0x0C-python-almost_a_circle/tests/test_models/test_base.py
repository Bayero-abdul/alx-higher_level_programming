#!/usr/bin/python3
"""this module contains testcases for Base class."""


import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test case for Base class."""

    @classmethod
    def setUpClass(self):
        """set up code."""

        self.r1 = Rectangle(10, 7, 2, 8)
        self.lst = []

    @classmethod
    def tearDownClass(self):
        """tear down code."""

        if os.path.exists('Rectangle.json'):
            os.remove('Rectangle.json')

        if os.path.exists('Square.json'):
            os.remove('Square.json')

    def test_init(self):
        """test for initialization."""

        b1 = Base()
        self.assertTrue(b1.id == 6)

        b2 = Base(12)
        self.assertTrue(b2.id == 12)

        b2.id = 7
        self.assertTrue(b2.id == 7)

    def test_to_json_string(self):
        """test to_json_string()."""

        dictionary = self.r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertTrue(dictionary == {'x': 2,
                                       'width': 10,
                                       'id': 1,
                                       'height': 7,
                                       'y': 8})

        self.assertIs(type(dictionary), dict)
        self.lst.append(dictionary)
        self.assertTrue(eval(json_dictionary) == self.lst)
        self.assertTrue(Base.to_json_string([]) == "[]")

    def test_save_to_file(self):
        """test save_to_file()."""

        Rectangle.save_to_file([self.r1])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(str(self.lst), f.read())

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertTrue('[]', f.read())

    def test_from_json_string(self):
        """test from_json_string()."""

        output = Rectangle.from_json_string(None)
        self.assertTrue(output == [])

        output1 = Rectangle.from_json_string('')
        self.assertTrue(output == [])

        json_list = Rectangle.to_json_string(self.lst)
        list_output = Rectangle.from_json_string(json_list)
        self.assertTrue(list_output == self.lst)

    def test_create(self):
        """test create()."""

        r4 = Rectangle(3, 5, 1)
        r4_dictionary = r4.to_dictionary()
        r5 = Rectangle.create(**r4_dictionary)
        self.assertEqual(str(r4), str(r5))
        self.assertFalse(r4 == r5)

        s1 = Square(3)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))
        self.assertFalse(s1 == s2)

    def test_load_from_file(self):
        """test for load_from_file()."""

        list_rectangles_input = [self.r1]

        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        for rect in list_rectangles_input:
            self.assertIs(type(rect), Rectangle)

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]

        Square.save_to_file(list_squares_input)
        ist_squares_output = Square.load_from_file()

        for square in list_squares_input:
            self.assertIs(type(square), Square)

        os.remove('Rectangle.json')
        os.remove('Square.json')

        self.assertTrue([] == Rectangle.load_from_file())
        self.assertTrue([] == Square.load_from_file())


if __name__ == "__main__":
    unittest.main()
