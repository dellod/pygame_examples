# !/usr/bin/env python3
# @file example3_class_methods.py
# SCRP: Example 3 - Class Methods
# Daryl Dang

"""
Example 3 - Class Methods
-----------------------
This example goes over how to create a basic class that uses its own methods.
"""

# Class Definition
class Animal:
    def __init__(self, animal_name):
        self.name = animal_name

    def make_sound(self, noise):
        print(self.name + " says " + noise + "!")

# Make object
big_red_dog = Animal("Clifford")

# Use the method of the object
big_red_dog.make_sound("bark")

# If you uncomment the code below, you will see that we can't call the function SINCE only objects
# of class animal can use it.
# make_sound("hello")