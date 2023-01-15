# !/usr/bin/env python3
# @file example2_drawing_circle.py
# SCRP: Example 2 - Drawing Circle
# Daryl Dang

import pygame

# GLOBALS
WHITE = (255, 255, 255)

# Initialize pygame and display window
pygame.init()
display = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Drawing Circle")
 # Draw circle
surface     = display       # what surface to draw on
colour      = WHITE         # the colour of the circle
center      = [250, 250]    # the center position of the circle
radius      = 100           # radius of the circle
width       = 0             # used for line thickness or to just fill the circle
# Game loop
running = True
while running:
    for event in pygame.event.get():
        # Quit when the user presses the X at the top right
        if event.type == pygame.QUIT:
            running = False

   
    pygame.draw.circle(surface, colour, center, radius, width)

    # Update the pygame window
    pygame.display.update()

# 5. Close and clean up
pygame.quit()
