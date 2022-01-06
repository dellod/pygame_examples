# !/usr/bin/env python3
# @file broken_code.py
# SCRP: PyCharm Basics - Hello World
# Daryl Dang

"""
This file will demonstrate a practical use of the debugger tool in PyCharm.
"""


def addition_function(number_1, number_2):
    result = number_1 * number_2
    return result


if __name__ == "__main__":
    addition_result = addition_function(5, 5)
    print("The result of the addition function is... {}".format(addition_result))
