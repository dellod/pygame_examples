# !/usr/bin/env python3
# @file example8_circle_collision.py
# SCRP: Example 8 - Circle Collision
# Daryl Dang

"""
Example 8 - Circle Collision
----------------------------------------------------
This example demonstrates calculating distance between points so that cna be used to calculate the
distance between circles.
"""
####################################################################################################
# IMPORTS
####################################################################################################
import pygame
import math # Need this for square root and exponent function

####################################################################################################
# GLOBALS
####################################################################################################
# Screen
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
FPS = 60

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Circle 1
CENTER_CIRC_1 = (250, 250)
RADIUS_CIRC_1 = 100

# Circle 2
RADIUS_CIRC_2 = 50

####################################################################################################
# SETUP (initialize and load images)
####################################################################################################
# Initialize pygame and display window
pygame.init()
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rectangle Collision Detection")
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 32)

####################################################################################################
# FUNCTIONS
####################################################################################################
def get_dist(x1, y1, x2, y2):
    """
    Get distance between two points on the display window given their x and y positions. Point 1
    should correspond to x1 and y1 while Point 2 should correspond to x2 and y2. This formula is
    based on Pythagorean Theorem.

    Parameters
    ----------
    x1 (float) - x-coordinate of point 1
    y1 (float) - y-coordinate of point 1
    x2 (float) - x-coordinate of point 2
    y2 (float) - y-coordinate of point 2

    Returns
    -------
    distance (float) - distance between the two points specified
    """
    distance = math.sqrt((math.pow(x1 - x2, 2)) + (math.pow(y1 - y2, 2))) # Pythagorean theorem
    return distance

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

    # Draw circle 1 in the center of the display window
    pygame.draw.circle(display, BLACK, CENTER_CIRC_1, RADIUS_CIRC_1, 2)

    # Get mouse position and update circle 2 position
    mouse_pos = pygame.mouse.get_pos()

    # Calculate distance between center of circle and mouse
    distance_between_points = round(get_dist(CENTER_CIRC_1[0], CENTER_CIRC_1[1], mouse_pos[0], mouse_pos[1]))

    # Check if circles have touched based on distance between their centres with their radius' added
    # If TRUE: colour the mouse circle RED
    # Otherwise: colour the mouse circle GREEN
    if distance_between_points < (RADIUS_CIRC_1 + RADIUS_CIRC_2):
        pygame.draw.circle(display, RED, mouse_pos, RADIUS_CIRC_2)
        text = font.render("Collision", True, RED)
    else:
        pygame.draw.circle(display, GREEN, mouse_pos, RADIUS_CIRC_2)
        text = font.render("No Collision", True, GREEN)

    # OPTIONAL: display text of distance on display
    display.blit(text, (10, 10))

    # Update the pygame window and set clock tick
    pygame.display.update()
    clock.tick(FPS)

# Close and clean up
pygame.quit()
