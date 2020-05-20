#!/usr/bin/python3
"""Square class"""


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
    """Attribute to get size"""
    @property
    def size(self):
        return self.__size
    """Attribute to set size"""
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    """print squares"""
    def my_print(self):
        if self.__size != 0:
            for line in range(self.__size):
                for square in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
