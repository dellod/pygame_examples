# !/usr/bin/env python3
# @file paint.py
# SCRP: Example 4 - Paint
# Daryl Dang

"""
Example 4 - Paint
----------------------------------------------------
This example combines the use of mouse positioning and mouse button detection all together to create
a small paint program.
"""
####################################################################################################
# IMPORTS
####################################################################################################
import pygame
import random

####################################################################################################
# GLOBALS
####################################################################################################
# Screen
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
FPS = 144
WHITE = (255, 255, 255)

# CIRCLE BRUSH
RADIUS = 25
COLOUR = [0, 0, 0] # Start off as black

####################################################################################################
# SETUP (initialize and load images)
####################################################################################################
# Initialize pygame and display window
pygame.init()
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Paint")
clock = pygame.time.Clock()
display.fill(WHITE)
pygame.display.flip()

# GAME LOOP
running = True
while running:
    for event in pygame.event.get():
        # Quit when the user presses the X at the top right
        if event.type == pygame.QUIT:
            running = False

        # Mouse button inputs
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pressed = pygame.mouse.get_pressed()

            # Check middle button
            if mouse_pressed[1]:
                # Clear canvas by redrawing background on top
                display.fill(WHITE)
                pygame.display.flip()

            # Check right button
            if mouse_pressed[2]:
                # Randomize next colour selection when right mouse button is pressed
                COLOUR = [random.uniform(0, 255), random.uniform(0, 255), random.uniform(0, 255)]

    # Track mouse position and store in variable
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed() # This is different from inside the event loop as we
                                               # we are checking this for every frame of the game.

    # Check when left mouse button is pressed and draw a circle
    if mouse_pressed[0]:
        pygame.draw.circle(display, COLOUR, mouse_pos, RADIUS, 0)

    # Update the pygame window and set clock tick
    pygame.display.update()
    clock.tick(FPS)

# Close and clean up
pygame.quit()
