#!/usr/bin/env python3
from typing import List, Union
"""
This module provides a function to sum a list containing both integers and floats.

It demonstrates the use of complex type annotations and proper documentation
for both the module and the function according to project requirements.
"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list containing integers and floats and return the result as a float.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and floats.

    Returns:
        float: The sum of all elements in the list as a float.
    """
    return float(sum(mxd_lst))
