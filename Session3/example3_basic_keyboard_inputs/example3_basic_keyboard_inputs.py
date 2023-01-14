# !/usr/bin/env python3
# @file example1_load_image.py
# SCRP: Example 3 - Basic Keyboard Inputs
# Daryl Dang

"""
Example 3 - Basic Keyboard Inputs
---------------------------------
This example goes over basic keyboard inputs and how to use it.
"""

import pygame

# GLOBALS
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# Initialize pygame and display window (this isn't that crucial for this basic program)
pygame.init()
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Basic Keyboard Inputs")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        # Quit when the user presses the X at the top right
        if event.type == pygame.QUIT:
            running = False

        # Keyboard inputs
        if event.type == pygame.KEYDOWN:
            print("Key pressed!")
            # UP key check
            if event.key == pygame.K_UP:
                print("UP key was pressed!")
            # DOWN key check
            if event.key == pygame.K_DOWN:
                print("DOWN key was pressed!")
            # LEFT key check
            if event.key == pygame.K_LEFT:
                print("LEFT key was pressed!")
            # RIGHT key check
            if event.key == pygame.K_RIGHT:
                print("RIGHT key was pressed!")

            # Add this print statement to make it more readable
            print("----------------------")

    # Update the pygame window
    pygame.display.update()

# Close and clean up
pygame.quit()
