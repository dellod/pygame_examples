# !/usr/bin/env python3
# @file example7_distance_between_points.py
# SCRP: Example 7 - Distance Between Points
# Daryl Dang

"""
Example 7 - Distance Between Points
----------------------------------------------------
This example demonstrates how to calculate the distance between two points on the display window.
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

# Circle
CENTER = (250, 250)
RADIUS = 25

####################################################################################################
# SETUP (initialize and load images)
####################################################################################################
# Initialize pygame and display window
pygame.init()
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Distance Between Points")
clock = pygame.time.Clock()

####################################################################################################
# FUNCTIONS
####################################################################################################
def get_dist(x1, y1, x2, y2):
    """
    Get distance between two points on the display window given their x and y positions. Point 1
    should correspond to x1 and y1 while Point 2 should correspond to x2 and y2.
    """
    distance = math.sqrt((math.pow(x1 - x2, 2)) + (math.pow(y1 - y2, 2)))
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

    # Draw center circle
    pygame.draw.circle(display, BLACK, CENTER, RADIUS, 0)

    # Get mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Calculate distance between center of circle and mouse
    distance_between_points = round(get_dist(CENTER[0], CENTER[1], mouse_pos[0], mouse_pos[1]))

    # OPTIONAL: draw line between circle and mouse position
    pygame.draw.line(display, RED, CENTER, mouse_pos)

    # OPTIONAL: display text of distance on display
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(f'Distance: {distance_between_points}', True, BLACK)
    display.blit(text, (10, 10))

    # Update the pygame window and set clock tick
    pygame.display.update()
    clock.tick(FPS)

# Close and clean up
pygame.quit()
