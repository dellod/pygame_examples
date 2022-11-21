# !/usr/bin/env python3
# @file example2_drawing_circle.py
# SCRP: Example 3 - Moving Circle
# Daryl Dang

import pygame

# GLOBALS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# Initialize pygame and display window
pygame.init()
display = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Moving Circle")
clock = pygame.time.Clock() # Clock for the game that will help us control the tick (frame) speed

# Game variables
x = 100
y = 100
radius = 100
filled_width = 0
border_width = 1

# Game loop
running = True
while running:
    clock.tick(FPS) # Limit the frame rate so we have a controllable circle
    for event in pygame.event.get():
        # Quit when the user presses the X at the top right
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen before drawing a new circle
    display.fill(BLACK)

    # Draw circle
    pygame.draw.circle(display, WHITE, [x, y], radius, filled_width) # filled circle
    pygame.draw.circle(display, BLACK, [x, y], radius, border_width) # border of circle

    # Update position of the circle of the next loop
    x += 1
    y += 1

    # Update the pygame window
    pygame.display.update()

# 5. Close and clean up
pygame.quit()
