# !/usr/bin/env python3
# @file example6_elif_statement.py
# SCRP: Session 1 - Example 6: Elif Statement
# Daryl Dang

"""
This program demonstrates the usage of an elif statement.
"""

percentage_grade = 85  # For example, a grade you would get in school

# Which is the difference between the two methods?
# Comment/Uncomment each section to test the output!

# --- Method 1 ---
if percentage_grade >= 95:
    print("You get an A+")
if percentage_grade >= 85:
    print("You get an A")
if percentage_grade >= 80:
    print("You get a B+")
if percentage_grade >= 75:
    print("You get a B")
if percentage_grade < 75:
    print("You get a grade less than B")

# --- Method 2 ---
if percentage_grade >= 95:
    print("You get an A+")
elif percentage_grade >= 85:
    print("You get an A")
elif percentage_grade >= 80:
    print("You get a B+")
elif percentage_grade >= 75:
    print("You get a B")
else:
    print("You get a grade less than B")
