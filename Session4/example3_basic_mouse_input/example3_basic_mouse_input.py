# !/usr/bin/env python3
# @file example3_basic_mouse_input.py
# SCRP: Example 3 - Basic Mouse Input
# Daryl Dang

"""
Example 3 - Basic Mouse Input
----------------------------------------------------
This example demonstrates the basics of reading mouse input events.
"""
####################################################################################################
# IMPORTS
####################################################################################################
import pygame

####################################################################################################
# GLOBALS
####################################################################################################
# Screen
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
FPS = 60

####################################################################################################
# SETUP (initialize and load images)
####################################################################################################
# Initialize pygame and display window
pygame.init()
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Doesn't matter too much here
pygame.display.set_caption("Basic Mouse Input")
clock = pygame.time.Clock()

####################################################################################################
# GAME LOOP
####################################################################################################
running = True
while running:
    for event in pygame.event.get():
        # Quit when the user presses the X at the top right
        if event.type == pygame.QUIT:
            running = False

        # Mouse button inputs
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("A mouse button was pressed!")

            mouse_pressed = pygame.mouse.get_pressed()
            # Left mouse button check
            if mouse_pressed[0]:
                print("Left mouse button was pressed!")
            # Middle mouse button check
            if mouse_pressed[1]:
                print("Middle mouse button was pressed!")
            # Right mouse button check
            if mouse_pressed[2]:
                print("Right mouse button was pressed!")

            print("---------------------------")
    # Update the pygame window and set clock tick
    pygame.display.update()
    clock.tick(FPS)

# Close and clean up
pygame.quit()
