#!/usr/bin/python3
"""Class MyList"""


class MyList(list):
    """My list inherits from List object"""
    def print_sorted(self):
        """Print sorted list
        """
        print("{}".format(sorted(self)))
