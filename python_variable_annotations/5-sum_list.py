#!/usr/bin/env python3
"""
This module provides a function to sum a list of floating point numbers.

It demonstrates the use of type annotations and includes proper documentation
for both the module and the function according to project requirements.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate and return the sum of a list of floats.

    Args:
        input_list (List[float]): A list of floating point numbers to sum.

    Returns:
        float: The sum of all elements in the input list.
    """
    return sum(input_list)
