#!/usr/bin/python3
""" defines a class square """


class Square:
    """ A square that has a private instance attribute called 'size'. """

    def __init__(self, size=0):
        """
        initializes square
        Args:
            size: size of sides of new square
        """

        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """
        finds area of square
        Returns:
            The measurement of the square's surface.
        """

        return self.__size ** 2
