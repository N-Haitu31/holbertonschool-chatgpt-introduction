#!/usr/bin/python3
import sys

"""
Fonction description:
    Recursively calculates the factorial of a non-negative integer n.

Parameters:
    n : int

Returns:
    int
"""


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


f = factorial(int(sys.argv[1]))
print(f)
