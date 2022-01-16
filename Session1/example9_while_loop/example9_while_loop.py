# !/usr/bin/env python3
# @file example9_while_loop.py
# SCRP: Session 1 - Example 9: While Loop
# Daryl Dang

"""
This program demonstrates a basic while loop. It also showcases what a bad while loop looks like.
"""

# Basic while loop
i = 1         # Set up initial counter variable.
while i < 4:  # Basic while loop condition with counter variable.
    print(i)
    i += 1    # Increment counter variable.

# Bad while loop (uncomment to test) - why is this a bad while loop?
# i = 1
# while i < 4:
#     print(i)
#     i -= 1      # i = i - 1 # The same statement but this is shorthand.
