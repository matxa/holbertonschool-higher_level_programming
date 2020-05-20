#!/usr/bin/python3
"""Empty Square class"""


class Square:
    """Init class"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    """Method for calc the area of square"""
    def area(self):
        return self.__size * self.__size
