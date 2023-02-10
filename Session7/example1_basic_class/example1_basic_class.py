# !/usr/bin/env python3
# @file example1_basic_class.py
# SCRP: Example 1 - Basic Class
# Daryl Dang

"""
Example 1 - Basic Class
-----------------------
This example goes over how to create a very basic class and how to make an object out of it.
"""

class Animal:
    name = "Clifford"

dog = Animal()
print(dog.name)

# We can make another object with a different variable name
dog2 = Animal()
print(dog2.name) # This isn't very practical if two dogs have the same name...