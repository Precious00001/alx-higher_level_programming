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

    def area(self):
        """
            Calculate and return the area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
            Calculate and return the perimeter of the rectangle.

        Return : (int) rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return(self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
            print the rectangle

        Return:
            Print a rectangle with a width represented by the character '#'.
            """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for w in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if w != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
