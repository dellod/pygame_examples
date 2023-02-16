# !/usr/bin/env python3
# @file example3_load_multiple_images.py
# SCRP: Example 3 - Load Multiple Images
# Daryl Dang

"""
Example 3 - Load Multiple Images
--------------------------------
This example goes over how to load multiple images to the screen.
One being the background and the other being a character of some sort in the background.
"""

import pygame

# GLOBALS
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
FPS = 60

# Initialize pygame and display window
pygame.init()
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Load Multiple Images")
clock = pygame.time.Clock()

# Load background in
not_mario_background_img = pygame.image.load("Session3\\example3_load_multiple_images\\not-mario-bg.png").convert()
not_mario_background_img = pygame.transform.scale(not_mario_background_img, (SCREEN_WIDTH, SCREEN_HEIGHT)) # Make the same as width and height of display window

# Load character in
not_mario_img = pygame.image.load("Session3\\example3_load_multiple_images\\not-mario.png").convert_alpha() # Use this to keep the background transparent
not_mario_img = pygame.transform.scale(not_mario_img, (100, 100)) # Make appropriate sized width and height

# Game loop
running = True
while running:
    for event in pygame.event.get():
        # Quit when the user presses the X at the top right
        if event.type == pygame.QUIT:
            running = False

    # Place images in using blit
    display.blit(not_mario_background_img, (0,0)) # Want background to take up whole screen
    display.blit(not_mario_img, (50, 375)) # Specific position for mario to be on the ground

    # Update the pygame window and set clock tick
    pygame.display.update()
    clock.tick(FPS)

# Close and clean up
pygame.quit()
