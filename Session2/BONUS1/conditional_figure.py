# !/usr/bin/env python3
# @file conditional_figure.py
# SCRP: BONUS 1 - Conditional Figure
# Daryl Dang

import pygame

# CONSTANTS
WIDTH   =   1000
HEIGHT  =   500
FPS     =   60
BLACK   =   (0, 0, 0)
ORANGE  =   (238, 103, 48)

# Initialize pygame and display window
pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conditional Figure")
clock = pygame.time.Clock()

# Add background (optional)
# Source: https://www.freepik.com/free-vector/empty-basketball-court-scene_26161662.htm#query=cartoon%20basketball&position=6&from_view=keyword
background_img = pygame.image.load("Session2\\BONUS1\\court.jpg") # Load image in the same folder
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT)) # Make image same size

# GAME VARIABLES
# Basketball
x = 100
y = 400
x_mov = 5
y_mov = -4.5
rad = 45

# Basketball Net
NET_CENTER = (500, 10)
has_scored = False
GROUND = (500, 400)

# Game loop
pygame.time.delay(5000)
running = True
while running:
    # Limit clock frame it
    clock.tick(FPS)

    # Draw background image
    display.blit(background_img, (0,0))

    # Check events
    for event in pygame.event.get():
        # Quit when the user presses the X at the top right
        if event.type == pygame.QUIT:
            running = False

    # Draw basketball
    pygame.draw.circle(display, ORANGE, [x, y], rad, 0) # Fill
    pygame.draw.circle(display, BLACK, [x, y], rad, 5) # Border

    # Update position (simple linear movement)
    x += x_mov
    y += y_mov

    # Check when we hit the net (x-position)
    if x == NET_CENTER[0]:
        x_mov = 0
        y_mov = 3
        has_scored = True

    # Check if the ball hits the ground after being shot in the net (y_position)
    if y == GROUND[1] and has_scored:
        y_mov = 0

    # Update pygame window
    pygame.display.update()

# Close and clean up
pygame.quit()
