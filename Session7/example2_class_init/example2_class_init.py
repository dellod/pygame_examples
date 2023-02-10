# !/usr/bin/env python3
# @file example2_class_init.py
# SCRP: Example 2 - Class init
# Daryl Dang

"""
Example 2 - Class Init
-----------------------
This example goes over how to create a basic class and using a constructor (__init__) method.
"""

# Class Definition
class Animal:
    def __init__(self, animal_name):
        # self refers to the instance of the class
        # for example, self.name means that the name belongs to the object when it is created.
        self.name = animal_name

# Let's make two separate objects and build them using constructors
big_red_dog = Animal("Clifford")
detective_dog = Animal("Scooby")

# Print out their unique names
print(big_red_dog.name)
print(detective_dog.name)