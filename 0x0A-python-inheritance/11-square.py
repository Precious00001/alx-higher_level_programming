#!/usr/bin/python3
"""
    a Rectangle subclass Square.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        Represent a square.
    """
    def __init__(self, size):
        """
            Initialize a square
        """
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Specify the calculation of the area for the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
            __str__
        """
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))
