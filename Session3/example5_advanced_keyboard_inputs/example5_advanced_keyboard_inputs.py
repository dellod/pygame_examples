# !/usr/bin/env python3
# @file example5_advanced_keyboard_inputs.py
# SCRP: Example 5 - Advanced Keyboard Inputs
# Daryl Dang

"""
Example 5 - Advanced Keyboard Inputs
---------------------------------
This example goes over using keyboard inputs to move a figure on the screen
"""

import pygame

# GLOBALS
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
FPS = 60
GUY_X = 50
GUY_Y = 375

# Initialize pygame and display window
pygame.init()
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Advanced Keyboard Inputs")
clock = pygame.time.Clock()

# Load background in
not_mario_background_img = pygame.image.load("Session3\\example5_advanced_keyboard_inputs\\not-mario-bg.png").convert()
not_mario_background_img = pygame.transform.scale(not_mario_background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load character in
not_mario_img = pygame.image.load("Session3\\example5_advanced_keyboard_inputs\\not-mario.png").convert_alpha() # Use this to keep the background transparent
not_mario_img = pygame.transform.scale(not_mario_img, (100, 100))

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
                GUY_Y -= 10 # Move by 10 pixels up
            # DOWN key check
            if event.key == pygame.K_DOWN:
                GUY_Y += 10 # Move by 10 pixels up
            # LEFT key check
            if event.key == pygame.K_LEFT:
                GUY_X -= 10 # Move by 10 pixels left
            # RIGHT key check
            if event.key == pygame.K_RIGHT:
                GUY_X += 10 # Move by 10 pixels right

    # Draw background (we need this in the game loop as without it you will see traces of your character)
    display.blit(not_mario_background_img, (0,0)) # Want background to take up whole screen

    # Draw mario in
    display.blit(not_mario_img, (GUY_X, GUY_Y))

    # Update the pygame window and set clock tick
    pygame.display.update()
    clock.tick(FPS)

# Close and clean up
pygame.quit()
