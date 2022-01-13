# !/usr/bin/env python3
# @file example3_arithmetic_operators_quiz.py
# SCRP: Session 1 - Example 3: Arithmetic Operators Quiz
# Daryl Dang

"""
This program contains a small quiz for the user to play that tests their knowledge on arithmetic operators!
This will contain the usage of the input function, that we will discuss in detail later on.
"""


# --- FUNCTIONS ---
def test_answer(expected, actual):
    """
    If the actual answer provided by the user matches expected, return True. Otherwise, return False.

    :param expected: expected answer
    :param actual: answer given by user
    :return bool: if expected matches actual
    """
    if expected == actual:
        print("Correct!")
        return True

    print("Incorrect :(")
    return False


# --- MAIN ---
if __name__ == "__main__":
    # Intialize score for quiz
    total_score = 0

    # Intro
    input("Hello! Welcome to the arithmetic operators quiz. Press enter when ready to start...")

    # Question 1
    if test_answer(30, int(input("What is the result of this operation: 25 + 5 = ? "))):
        total_score += 1

    # Question 2
    if test_answer(11, int(input("What is the result of this operation: 121 / 11 = ? "))):
        total_score += 1

    # Question 3
    if test_answer("2.0",
                   input("What is the result of this operation: 3.5 - 1.5 = ? (MAKE SURE TO INCLUDE THE DECIMAL) ")):
        total_score += 1

    # Question 4
    if test_answer(0, int(input("What is the result of this operation: 0 * 1 234 567= ? "))):
        total_score += 1

    # Question 5
    if test_answer('Y', input("Are you allowed to add two strings together? (Y/N)").capitalize()):
        total_score += 1

    # End
    print("Thanks for playing! You got a total score of: " + str(total_score))
