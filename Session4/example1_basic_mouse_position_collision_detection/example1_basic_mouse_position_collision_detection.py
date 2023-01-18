# !/usr/bin/env python3
# @file example1_basic_collision_detection.py
# SCRP: Example 1 - Basic Mouse Position Collision Detection
# Daryl Dang

"""
Example 1 - Basic Mouse Position Collision Detection
----------------------------------------------------
This example demonstrates basic collision detection with your mouse and drawn object on the screen
using collidepoint().
"""

import pygame

# GLOBALS
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
COLOUR = [255, 255, 255]
CENTER = (250, 250)
RADIUS = 100

# Initialize pygame and display window (this isn't that crucial for this basic program)
pygame.init()
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Basic Mouse Position Collision Detection")

# Draw circle first and store it in a variable so we can use it later in the loop
circ = pygame.draw.circle(display, COLOUR, CENTER, RADIUS, 0)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        # Quit when the user presses the X at the top right
        if event.type == pygame.QUIT:
            running = False

    point = pygame.mouse.get_pos()
    collide = circ.collidepoint(point)
    if collide:
        COLOUR = [255, 0, 0]
    else:
        COLOUR = [255, 255, 255]

    # Draw circle again and update with new colour
    display.fill(0)
    pygame.draw.circle(display, COLOUR, CENTER, RADIUS, 0)

    # Update the pygame window
    pygame.display.update()

# Close and clean up
pygame.quit()
