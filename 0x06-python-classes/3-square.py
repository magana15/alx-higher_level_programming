#!/usr/bin/python3
""" class Square defining a square"""

class Square:
    """ class Square defining a square"""

    def __init__(self, size=0):
        """initialize square
        Args:
            size (int): size of the square
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """return the area.

        Return:
            area.
        """
        return self.__size**2
