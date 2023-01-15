# !/usr/bin/env python3
# @file example1_load_image.py
# SCRP: Example 4 - Advanced Keyboard Inputs
# Daryl Dang

"""
Example 4 - Advanced Keyboard Inputs
---------------------------------
This example goes over using keyboard inputs to move a figure on the screen
"""

import pygame

# GLOBALS
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
MARIO_X = 50
MARIO_Y = 375

# Initialize pygame and display window (this isn't that crucial for this basic program)
pygame.init()
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Basic Keyboard Inputs")

# Load mario background in
mario_background_img = pygame.image.load("Session3\\example4_advanced_keyboard_inputs\\mario-bg.png").convert()
mario_background_img = pygame.transform.scale(mario_background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load mario in
mario_img = pygame.image.load("Session3\\example4_advanced_keyboard_inputs\\mario.png").convert_alpha() # Use this to keep the background transparent
mario_img = pygame.transform.scale(mario_img, (100, 100))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        # Quit when the user presses the X at the top right
        if event.type == pygame.QUIT:
            running = False

        # Keyboard inputs for moving mario
        # NOTE: This will be a very clunky way of moving figures in pygame because we are not
        #       moving this amount per frame. We will look how to make this movement better in
        #       later examples!
        if event.type == pygame.KEYDOWN:
            # UP key check
            if event.key == pygame.K_UP:
                MARIO_Y -= 10 # Move by 10 pixels up
            # DOWN key check
            if event.key == pygame.K_DOWN:
                MARIO_Y += 10 # Move by 10 pixels up
            # LEFT key check
            if event.key == pygame.K_LEFT:
                MARIO_X -= 10 # Move by 10 pixels left
            # RIGHT key check
            if event.key == pygame.K_RIGHT:
                MARIO_X += 10 # Move by 10 pixels right

    # Draw background
    display.blit(mario_background_img, (0,0)) # Want background to take up whole screen

    # Draw mario in
    display.blit(mario_img, (MARIO_X, MARIO_Y))

    # Update the pygame window
    pygame.display.update()

# Close and clean up
pygame.quit()
