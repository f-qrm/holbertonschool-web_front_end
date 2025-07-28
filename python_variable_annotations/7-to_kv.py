#!/usr/bin/env python3
"""
This module provides a function to create a tuple from a string and a numeric
value.
It demonstrates the use of complex type annotations with Union and Tuple,
and includes proper documentation for the module and the function.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple where the first element is the given string
    and the second
    element is the square of the numeric value as a float.

    Args:
        k (str): The string key.
        v (Union[int, float]): The numeric value, either int or float.

    Returns:
        Tuple[str, float]: A tuple containing the string and the squared value
        as float.
    """
    return (k, float(v ** 2))
