# !/usr/bin/env python3
# @file example10_user_input.py
# SCRP: Example 10 - User Input
# Daryl Dang

# Basic string example
message_from_user = input("Type your message here: ")
print("This is what the user said: " + message_from_user)

# Integer example
number_from_user = input("Enter in a number from 1 to 5: ")
integer_from_user = int(number_from_user) # need to type case here because input is default a string
new_number = integer_from_user + 10

print("Here is the result of the user number + 10: " + str(new_number)) # have to type cast back
