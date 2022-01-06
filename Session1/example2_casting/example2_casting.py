# !/usr/bin/env python3
# @file example2_casting.py
# SCRP: Session 1 - Example 2: Casting
# Daryl Dang

"""
This program demonstrates how to use casting for integers, floats, and strings.
"""

# Integer Casting
a = int(1)          # a now becomes 1 (doesn't change)
b = int(3.14)       # b now becomes 3 (always cuts off the decimal point and rounds down)
c = int("4")        # c now becomes 4

# Float Casting
d = float(5.5)      # d now becomes 5.5 (doesn't change)
e = float(6)        # e now becomes 6.0
f = float("7")      # f now becomes 7.0
g = float("8.6")    # g now becomes 8.6

# String Casting
h = str("hi")       # h now becomes "hi" (doesn't change)
i = str(2)          # i now becomes "2"
j = str(3.5)        # j now becomes "3.5"
