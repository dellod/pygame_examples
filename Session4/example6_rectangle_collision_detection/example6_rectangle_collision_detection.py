# !/usr/bin/env python3
# @file example6_rectangle_collision_detection.py
# SCRP: Example 6 - Rectangle Collision Detection
# Daryl Dang

"""
Example 6 - Rectangle Collision Detection
----------------------------------------------------
This example demonstrates basic collision detection between rectangles.
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
SCREEN_HEIGHT = 500
FPS = 60

# Colours
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)

# Rectangles
RECT_WIDTH = 100
RECT_HEIGHT = 100
RECT1_X = 0
RECT1_Y = SCREEN_HEIGHT/2 - RECT_HEIGHT/2
RECT1_COLOUR = GREEN
RECT2_X = SCREEN_WIDTH - RECT_WIDTH
RECT2_Y = SCREEN_HEIGHT/2 - RECT_HEIGHT/2
RECT2_COLOUR = RED

####################################################################################################
# SETUP (initialize and load images)
####################################################################################################
# Initialize pygame and display window
pygame.init()
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rectangle Collision Detection")
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

    # Draw rectangles
    rect1 = pygame.draw.rect(display, RECT1_COLOUR, pygame.Rect(RECT1_X, RECT1_Y, RECT_WIDTH, RECT_HEIGHT))
    rect2 = pygame.draw.rect(display, RECT2_COLOUR, pygame.Rect(RECT2_X, RECT2_Y, RECT_WIDTH, RECT_HEIGHT))

    # Call the function colliderect() to check if two drawn rectangles are touching on screen. Pass
    # in two Rect objects. This function will return a boolean value.
    collide = pygame.Rect.colliderect(rect1, rect2)

    # If not colliding, continue adding movement to our first rectangle. Otherwise, stop it and turn
    # it red.
    if not(collide):
        RECT1_X += 5
    else:
        RECT1_COLOUR = RED

    # Update the pygame window and set clock tick
    pygame.display.update()
    clock.tick(FPS)

# Close and clean up
pygame.quit()
