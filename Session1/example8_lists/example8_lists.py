# !/usr/bin/env python3
# @file example8_lists.py
# SCRP: Session 1 - Example 8: Lists
# Daryl Dang

"""
This program demonstrates the basics of a list and how to use it.
Comment and uncomment examples to test each section.
"""

# --- How to write/define a list? ---
string_list = ["Alice", "Bob", "Carl", "Daryl", "Edward"]
print(string_list)  # We can print a whole list directly by calling its name in a print statement

integer_list = [5, 6, 7, 8]  # A list made up of integers
print(integer_list)

float_list = [1.2, 3.421, 9.2, 6.6]  # A list made up of floats
print(float_list)

everything_list = ["Alice", 1, True, 3.14]  # A list made up of a bunch of data types
print(everything_list)

# --- How to read an element from a list? ---
name_list = ["Alice", "Bob", "Carl", "Daryl", "Edward"]
print(name_list)  # Print the whole list first
print(name_list[2])  # What gets printed to the screen? (3rd element in the list at the 2nd index position)


# --- How to replace an element in a list? ---
print(name_list)  # Print the whole list first, let's use the name_list again
name_list[3] = "JIM"  # Let's replace "Daryl" with "JIM" instead
print(name_list)  # Print the whole list AGAIN to see the changes


# --- List Functions ---
num_list = [2, 3, 1, 4]

# len: Get the length (size) of the list - how many elements are in the list
print(len(num_list))

# append: Add something to the very END of the list
num_list.append(5)
print(num_list)

# remove: Remove a SPECIFIED element from a list
num_list.remove(3)
print(num_list)

# sort: sorts a list to be in order
num_list.sort()
print(num_list)

# clear: clears an entire list
num_list.clear()
print(num_list)
