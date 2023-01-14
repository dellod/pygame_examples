# !/usr/bin/env python3
# @file example1_load_image.py
# SCRP: Example 1 - Load Image
# Daryl Dang

"""
Example 1 - Load Image
--------------------------
This example goes over how to load an image.
"""

import pygame

# Initialize pygame and display window
pygame.init()
display = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Load Image")

# Load image
mario_img = pygame.image.load("Session3\\example1_load_image\\mario.png").convert()

# Use blit
display.blit(mario_img, (0,0))

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
    #display.blit(mario_img, (0,0))

    # Update the pygame window
    pygame.display.update()

# Close and clean up
pygame.quit()
