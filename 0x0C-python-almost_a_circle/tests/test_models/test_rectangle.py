#!/usr/bin/python3
"""
This specifies unit tests for the models/rectangle.py file.
"""

import unittest
import json
from models import rectangle
from models.base import Base
Rectangle = rectangle.Rectangle


class TestRectangle(unittest.TestCase):
    """
    Unit tests for verifying the instantiation
    of the Rectangle class."""
    @classmethod
    def setUpClass(cls):
        """setting up class"""
        Base._Base__nb_objects = 0
        cls.d1 = Rectangle(10, 10)
        cls.d2 = Rectangle(2, 3, 4)


    def test_width(self):
        """Checking for the operational width."""
        self.assertEqual(self.d1.width, 10)
        self.assertEqual(self.d2.width, 2)


    def test_x(self):
        """Check the functionality of x"""
        self.assertEqual(self.d1.x, 0)
        self.assertEqual(self.d2.x, 4)

    def test_id(self):
        """Checking for a valid or operational ID."""
        self.assertEqual(self.d1.id, 1)
        self.assertEqual(self.d2.id, 2)

    def test_y(self):
        """Test for the proper functioning of y"""
        self.assertEqual(self.d1.y, 0)
        self.assertEqual(self.d2.y, 0)

    def test_width(self):
        """ width"""
        with self.assertRaises(TypeError):
            d = Rectangle()

    def test_height(self):
        """Testing for functioning height"""
        self.assertEqual(self.d1.height, 10)
        self.assertEqual(self.d2.height, 3)

    def test_height(self):
        """height"""
        with self.assertRaises(TypeError):
            d = Rectangle(1)

    def width_typeerror(self):
        """Test not int for width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            d = Rectangle("hello", 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            d = Rectangle(True, 1)

    def height_typeerror(self):
        """not int for height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            d = Rectangle(1, "hello")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            d = Rectangle(1, True)

    def x_typeerror(self):
        """not int for x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            d = Rectangle(1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            d = Rectangle(1, 1, True)

    def y_typeerror(self):
        """not int for y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            d = Rectangle(1, 1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            d = Rectangle(1, 1, 1, True)

    def width_valueerror(self):
        """ ints <= 0 for width"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            d = Rectangle(-1, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            d = Rectangle(0, 1)

    def height_valueerror(self):
        """ints <= 0 for height"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            d = Rectangle(1, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            d = Rectangle(1, 0)

    def x_valueerror(self):
        """ints < 0 for x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            d = Rectangle(1, 1, -1)

    def y_valueerror(self):
        """Test ints <= 0 for y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            d = Rectangle(1, 1, 1, -1)

    def test_area(self):
        """test area"""
        self.assertEqual(self.d1.area(), 100)
        self.assertEqual(self.d2.area(), 6)

    def area_args(self):
        """too many args for area()"""
        with self.assertRaises(TypeError):
            d = self.d1.area(1)

    def display_too_many_args(self):
        """display with too many args"""
        with self.assertRaises(TypeError):
            self.d1.display(1)

    def test_str(self):
        """Test the __str__ method"""
        self.assertEqual(str(self.d1), "[Rectangle] (1) 0/0 - 10/10")
        self.assertEqual(str(self.d2), "[Rectangle] (2) 4/0 - 2/3")

    def test_update_args(self):
        """
        Testing the udpate method
        with *args"""
        d = Rectangle(1, 1, 0, 0, 1)
        self.assertEqual(str(d), "[Rectangle] (1) 0/0 - 1/1")
        d.update(89)
        self.assertEqual(str(d), "[Rectangle] (89) 0/0 - 1/1")
        d.update(89, 2)
        self.assertEqual(str(d), "[Rectangle] (89) 0/0 - 2/1")
        d.update(89, 2, 3)
        self.assertEqual(str(d), "[Rectangle] (89) 0/0 - 2/3")
        d.update(89, 2, 3, 4)
        self.assertEqual(str(d), "[Rectangle] (89) 4/0 - 2/3")
        d.update(89, 2, 3, 4, 5)
        self.assertEqual(str(d), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_args_setter(self):
        """
        tests that the update method
        uses setter with *args"""
        d = Rectangle(1, 1, 0, 0, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            d.update(1, "hello")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            d.update(1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            d.update(1, 1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            d.update(1, 1, 1, 1, "hello")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            d.update(1, 0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            d.update(1, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            d.update(1, 1, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            d.update(1, 1, -1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            d.update(1, 1, 1, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            d.update(1, 1, 1, 1, -1)

    def update_too_many_args(self):
        """too many args for update"""
        recta = Rectangle(1, 1, 0, 0, 1)
        recta.update(1, 1, 1, 1, 1, 2)
        self.assertEqual(str(recta), "[Rectangle] (1) 1/1 - 1/1")

    def update_no_args(self):
        """no args for update"""
        recta = Rectangle(1, 1, 0, 0, 1)
        recta.update()
        self.assertEqual(str(recta), "[Rectangle] (1) 0/0 - 1/1")

    def mix_args_kwargs(self):
        """output for mixed args and kwargs"""
        recta = Rectangle(1, 1, 0, 0, 1)
        recta.update(2, 2, 2, 2, 2, width=3, height=3, x=3, y=3, id=3)
        self.assertEqual(str(recta), "[Rectangle] (2) 2/2 - 2/2")

