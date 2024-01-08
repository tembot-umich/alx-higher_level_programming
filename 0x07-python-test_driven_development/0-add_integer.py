#!/usr/bin/python3
"""

The sole function present in this module sums a pair of integer values

"""


def add_integer(a, b=98):
    """Calculate the sum of a pair of numbers, whether integers or floats, and return the total as an integer.

    Args:
        a: first argument
        b: second argument

    Returns:
        Sum of the two arguments

    Raises:
        TypeError: If either of the arguments not an integer or a float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
