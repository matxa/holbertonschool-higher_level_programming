#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Initializing the Rectangle class"""
    def __init__(self, width=0, height=0):
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__height = height
        self.__width = width

    """Getting the private __height variable"""
    @property
    def height(self):
        return self.__height

    """Setting the private __height variable"""
    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """Getting the private __width variable"""
    @property
    def width(self):
        return self.__width

    """Setting the private __width variable"""
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
