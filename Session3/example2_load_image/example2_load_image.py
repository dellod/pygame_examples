# !/usr/bin/env python3
# @file example2_load_image.py
# SCRP: Example 2 - Load Image
# Daryl Dang

"""
Example 2 - Load Image
----------------------
This example goes over how to load an image.
"""

import pygame

# Initialize pygame and display window
pygame.init()
display = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Load Image")

# Load image
not_mario_img = pygame.image.load("Session3\\example2_load_image\\not_mario.png").convert()

# Use blit
display.blit(not_mario_img, (0,0))

# Update display one time (draws to screen). This is OPTIONAL as blit will draw one time anyways.
pygame.display.flip()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        # Quit when the user presses the X at the top right
        if event.type == pygame.QUIT:
            running = False

    ### QUESTION: What is the difference between having display.blit inside the game loop instead?
    #display.blit(not_mario_img, (0,0))

    # Update the pygame window
    pygame.display.update()

# Close and clean up
pygame.quit()
