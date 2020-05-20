#!/usr/bin/python3
"""Square class"""


class Square:
    """Init class"""
    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if type(position) != tuple or (position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
    """Method for calc the area of square"""
    def area(self):
        return self.__size * self.__size
    """property to get size"""
    @property
    def size(self):
        return self.__size
    """property to set size"""
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    """property to get position"""
    @property
    def position(self):
        return self.__position
    """property to set position"""
    @position.setter
    def position(self, value):
        if type(value) != tuple or (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    """print squares"""
    def my_print(self):
        if self.__position[1] > 0:
            print()
        if self.__size != 0:
            for line in range(self.__size):
                print(" " * self.__position[0], end="")
                for square in range(self.__size):
                    print("#", end="")
                print()
