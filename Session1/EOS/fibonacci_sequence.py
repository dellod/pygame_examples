# !/usr/bin/env python3
# @file fibonacci_sequence.py
# SCRP: EOS - Fibonacci Sequence 
# Daryl Dang

####################################################################################################
# This file will serve as a template for starting out projects and setting up the PyGame window.
# Note: examples will LOOSELY follow PEP 8 guidelines.
# See https://peps.python.org/pep-0008/ for more detailed guidelines.
####################################################################################################

# 1. Ask user for input for the level of Fibonacci sequence and store in variable.
#   NOTE: need to type cast the input as it will first be read as a string
iterations = int(input("Enter number of iterations for Fibonacci Sequence (larger than 2): "))

# 2. If user enters in a number less than or equal to 2, tell them the program cannot run and exit.
if (iterations <= 2):
    print("the program requires a number larger than 2, exiting program...")
    exit(0)
else:
    print("Correct input, working on creating Fibonacci Sequence...")

# 3. Define starting numbers.
n1 = 0
n2 = 1

# 4. Create key variables for loop.
prev_number = n1        # First number to add
curr_number = n2        # Second number to add
i = 2                   # Loop counter (starts at 2 since we skip the first two numbers)

# 5. Print first two numbers (n1 and n2), as these will always be present for every sequence.
print("Number 1: " + str(n1))
print("Number 2: " + str(n2))

# 6. Loop through and print each iteration of Fibonacci sequence.
while i < iterations:
    # Calculate new number and print it
    temp = prev_number + curr_number
    print("Number " + str(i + 1) + ": " + str(temp))

    # Replace old numbers
    prev_number = curr_number
    curr_number = temp

    # Update loop
    i += 1
