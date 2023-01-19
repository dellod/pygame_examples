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
pygame.display.set_caption("Mouse Position")
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

        # Check when mouse button is pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("A mouse button was pressed!")

    # Get the mouse position and store it in a variable (this variable is a tuple!)
    mouse_pos = pygame.mouse.get_pos()

    # Update the pygame window and set clock tick
    pygame.display.update()
    clock.tick(FPS)

# Close and clean up
pygame.quit()
