#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        try:
            if size >= 0:
                self.__size = int(size)
        except ValueError:
            print("size must be >= 0")
        except TypeError:
            print("size must be an integer")
