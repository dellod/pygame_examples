# !/usr/bin/env python3
# @file example5_mouse_position_collision_detection.py
# SCRP: Example 5 - Mouse Position Collision Detection
# Daryl Dang

"""
Example 5 - Mouse Position Collision Detection
----------------------------------------------------
This example demonstrates basic collision detection with your mouse and drawn object on the screen
using collidepoint().
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
WHITE = (255, 255, 255)

# Circle
COLOUR = [0, 0, 0]
CENTER = (250, 250)
RADIUS = 100

####################################################################################################
# SETUP (initialize and load images)
####################################################################################################
# Initialize pygame and display window
pygame.init()
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mouse Position Collision Detection")
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

    # Draw black background
    display.fill(WHITE)

    # Draw circle that will be checking the collision
    circle = pygame.draw.circle(display, COLOUR, CENTER, RADIUS, 0)

    # Get the mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Call the function collidepoint() to check if the drawn circle is colliding with the drawn
    # circle on the screen. Pass in the mouse position variable as our only argument. This function
    # will return a boolean value.
    collide = circle.collidepoint(mouse_pos)

    # If we have collided with our circle, colour it red. Otherwise, colour the circle white.
    if collide:
        COLOUR = [255, 0, 0] # RED
    else:
        COLOUR = [0, 0, 0] # WHITE

    # Update the pygame window and set clock tick
    pygame.display.update()
    clock.tick(FPS)

# Close and clean up
pygame.quit()
