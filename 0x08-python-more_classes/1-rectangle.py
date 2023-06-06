#!/usr/bin/python3
"""
    Rectangle module

    """


class Rectangle:
    """
        Represent a rectangle
        """
    def __init__(self, width=0, height=0):
        """
            Init a new Rectangle Class

        Args:
            width (int): width of new rectangle
            height (int): height of new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
            getter for the private instance attribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Width setter
        Args:
            Value (int) : a value to set
        Raises:
            TypeError: If the value is not an integer
            ValueError: If the value is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            Get/set the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
