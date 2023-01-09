#!/usr/bin/python3


class MyInt(int):
    """MyInt class"""

    def __eq__(self, other):
        """invert equality"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """invert non equality"""
        return not super().__ne__(other)
