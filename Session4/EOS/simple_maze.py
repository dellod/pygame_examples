# !/usr/bin/env python3
# @file maze.py
# SCRP: EOS - Simple Maze
# Daryl Dang

"""
EOS - Simple Maze
----------------------------------------------------
A very simple maze game where you have to pick up a character and move them around the circles.
"""
####################################################################################################
# IMPORTS
####################################################################################################
import math
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
RED = (255, 0, 0)

# Hedgehog
HEDGEHOG_X = 25
HEDGEHOG_Y = 250

# Circle 1
RADIUS1 = 175
CIRCLE1_POS = (400, 250)

# Circle 2
RADIUS2 = 150
CIRCLE2_POS = (750, 250)

####################################################################################################
# SETUP (initialize and load images)
####################################################################################################
# Initialize pygame and display window
pygame.init()
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rectangle Collision Detection")
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 32)

# Load in hedgehog
hedgehog_img = pygame.image.load("Session4\\EOS\\hedgehog.png").convert_alpha()
hedgehog_img = pygame.transform.scale(hedgehog_img, (100, 100))

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
    distance = math.sqrt((math.pow(x2 - x1, 2)) + (math.pow(y2 - y1, 2))) # Pythagorean theorem
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

    # Draw white background
    display.fill(WHITE)

    # Draw obstacle circles
    pygame.draw.circle(display, RED, CIRCLE1_POS, RADIUS1, 25)
    pygame.draw.circle(display, RED, CIRCLE2_POS, RADIUS2, 50)

    # Get mouse position for character
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    # Check when left mouse button and when user is hovering over hedgehog
    if mouse_pressed[0] and (get_dist(HEDGEHOG_X, HEDGEHOG_Y, mouse_pos[0], mouse_pos[1]) < 100):
        HEDGEHOG_X = mouse_pos[0] - 50
        HEDGEHOG_Y = mouse_pos[1] - 50

    # Check collisions with circles
    if get_dist(HEDGEHOG_X + 50, HEDGEHOG_Y + 50, CIRCLE1_POS[0], CIRCLE1_POS[1]) < (RADIUS1 + 35):
        HEDGEHOG_X = 100
        HEDGEHOG_Y = 250

    if get_dist(HEDGEHOG_X + 50, HEDGEHOG_Y + 50, CIRCLE2_POS[0], CIRCLE2_POS[1]) < (RADIUS2 + 35):
        HEDGEHOG_X = 100
        HEDGEHOG_Y = 250

    # Draw hedgehog
    display.blit(hedgehog_img, (HEDGEHOG_X, HEDGEHOG_Y))

    # Update the pygame window and set clock tick
    pygame.display.update()
    clock.tick(FPS)

# Close and clean up
pygame.quit()
