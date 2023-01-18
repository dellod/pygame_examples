# !/usr/bin/env python3
# @file example2_following_mouse_position.py
# SCRP: Example 1 - Following Mouse Position
# Daryl Dang

"""
Example 2 - Following Mouse Position
----------------------------------------------------
This example demonstrates the basics of reading and using mouse inputs.
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

# Colour
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Circle
RADIUS = 50

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

    # Make background white
    display.fill(WHITE)

    # Get the mouse position and store it in a variable (this variable is a tuple!)
    mouse_pos = pygame.mouse.get_pos()

    # Draw circle with the mouse position as our center
    pygame.draw.circle(display, BLUE, mouse_pos, RADIUS, 0)

    # Update the pygame window and set clock tick
    pygame.display.update()
    clock.tick(60)

# Close and clean up
pygame.quit()
