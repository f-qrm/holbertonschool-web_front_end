#!/usr/bin/env python3
"""
This module provides a function to compute the floor of a floating point
number.

It demonstrates the use of type annotations and includes proper documentation
for both the module and the function according to project requirements.
"""
import math


def floor(n: float) -> int:
    """
    Return the floor of a floating point number as an integer.

    Args:
        n (float): The floating point number to compute the floor of.

    Returns:
        int: The largest integer less than or equal to n.
    """
    return math.floor(n)
