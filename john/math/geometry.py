"""
Various math routines

circle_area()
rectangle_area()

blah blah
blah blah
blah blah
"""
from math import pi


def circle_area(diameter):
    """
    Calculate area of circle

    :param diameter: diameter of circle
    :return: area of circle
    """
    radius = diameter / 2
    return pi * radius ** 2


def rectangle_area(length, width):
    return length * width

# module search order:
# 1. current folder
# 2. folders in PYTHONPATH
# 3. builtin folders (sys.prefix/lib)

# if run as script, NOT imported as module
if __name__ == '__main__':
    print("Hi Mom!")
    print(circle_area(22))
