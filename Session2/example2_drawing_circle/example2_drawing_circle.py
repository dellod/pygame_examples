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

# Game loop
running = True
while running:
    for event in pygame.event.get():
        # Quit when the user presses the X at the top right
        if event.type == pygame.QUIT:
            running = False

    # Draw circle
    position = [250, 250]
    radius = 100
    width = 0
    pygame.draw.circle(display, 255, [250, 250], 100, 0)

    # Update the pygame window
    pygame.display.update()

# 5. Close and clean up
pygame.quit()
