# !/usr/bin/env python3
# @file example1_mouse_position.py
# SCRP: Example 1 - Mouse Position
# Daryl Dang

"""
Example 1 - Mouse Position
----------------------------------------------------
This example demonstrates the basics of using mouse inputs.
"""
####################################################################################################
# IMPORTS
####################################################################################################
import pygame

####################################################################################################
# GLOBALS
####################################################################################################
# Screen
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
FPS = 60
WHITE = (255, 255, 255)

####################################################################################################
# SETUP (initialize and load images)
####################################################################################################
# Initialize pygame and display window
pygame.init()
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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

    # Get the mouse position and store it in a variable
    mouse_pos = pygame.mouse.get_pos()

    # Print the mouse position to the console (use format printing technique)
    print(f'(MOUSE X: {mouse_pos[0]}, MOUSE Y: {mouse_pos[1]})')

    # Make background white
    display.fill(WHITE)

    # Update the pygame window and set clock tick
    pygame.display.update()
    clock.tick(60)

# Close and clean up
pygame.quit()
