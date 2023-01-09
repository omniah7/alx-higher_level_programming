#!/usr/bin/python3


class MyList(list):
    """a class that inherits from list"""
    def print_sorted(self):
        """prints the list (ascending sort)"""
        print(sorted(self))
