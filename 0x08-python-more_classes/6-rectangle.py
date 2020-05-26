#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Initializing the Rectangle class
    """

    # Public attribute
    number_of_instances = 0

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
        Rectangle.number_of_instances += 1

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

    """Calculate the area of the rectangle"""
    def area(self):
        return self.__height * self.__width

    """Calculate the perimiter of the rectangle class"""
    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__height) + (self.__width + self.__width)

    """String Representation of rectangle class"""
    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        rect_r = (('#' * self.__width) + '\n') * (self.__height - 1)
        return rect_r + ('#' * self.__width)

    """Representation of rectangle class"""
    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    """Prititing message when instance of class is deleted"""
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
