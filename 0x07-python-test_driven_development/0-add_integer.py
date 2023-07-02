#!/usr/bin/python3
"""Defines an integer addition function."""

def add_integer(a, b=98):
        """
    Adds two numbers, a and b, and returns the result as an integer.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int: The addition of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.

        """
        if ((not isinstance(a, int) and not isinstance(a, float))):
            raise TypeError("a must be an integer")
        if ((not isinstance(b, int) and not isinstance(b, float))):
            raise TypeError("b must be an integer")
        return (int(a) + int(b))
