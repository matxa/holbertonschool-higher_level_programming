#!/usr/bin/python3
"""class that defines Rectangle and inherites from Base"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializing Rectangle
        class
        """
        super().__init__(id)
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    """Getting the private __height variable"""
    @property
    def height(self):
        """getting the height
        """
        return self.__height

    """Setting the private __height variable"""
    @height.setter
    def height(self, value):
        """Setting the height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    """Getting the private __width variable"""
    @property
    def width(self):
        """getting the width
        """
        return self.__width

    """Setting the private __width variable"""
    @width.setter
    def width(self, value):
        """Setting the width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    """Getting the private __x variable"""
    @property
    def x(self):
        """getting x
        """
        return self.__x

    """Setting the private __x variable"""
    @x.setter
    def x(self, value):
        """Setting x
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    """Getting the private __y variable"""
    @property
    def y(self):
        """getting y
        """
        return self.__y

    """Setting the private __y variable"""
    @y.setter
    def y(self, value):
        """Setting y
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    """Calculate the area of the rectangle"""
    def area(self):
        """calc Area
        """
        return self.__height * self.__width

    """Dispay Representation of rectangle class"""
    def display(self):
        """display
        """
        print("{}".format('\n' * self.__y), end="")
        for i in range(self.__height):
            print('{}{}'.format(' ' * self.__x, '#' * self.__width))

    """String Representation of rectangle class"""
    def __str__(self):
        """string representation
        """
        tprint = (self.id, self.__x, self.__y, self.__width, self.__height)
        return "[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}".format(*tprint)

    """Update the Rectangle"""
    def update(self, *args, **kwargs):
        """Update
        """
        if args and len(args) != 0:
            self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
        else:
            for k, v in kwargs.items():
                if k == "height":
                    self.__height = v
                elif k == "width":
                    self.__width = v
                elif k == "x":
                    self.__x = v
                elif k == "y":
                    self.__y = v
                elif k == "id":
                    self.id = v

    """return a to_dictionary Representation"""
    def to_dictionary(self):
        """return dict
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
