# !/usr/bin/env python3
# @file step1_basic_setup_and_load_images.py
# SCRP: Step 1 - Basic Setup and Load Images
# Daryl Dang

"""
Step 1 - Basic Setup and Load Images
------------------------------------
This step will go over basic setup and loading images.
"""
####################################################################################################
# IMPORTS
####################################################################################################
import pygame

####################################################################################################
# CONSTANTS
####################################################################################################
# Screen
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
FPS = 60

# Dog
DOG_POS = (360, 400) # this is a tuple because it is not moving

####################################################################################################
# SETUP
####################################################################################################
# Initialize pygame and display window
pygame.init()
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Duck Hunter")
clock = pygame.time.Clock()

# Load background
duck_hunter_background_img = pygame.image.load("Session8\\assets\\background.png").convert()
duck_hunter_background_img = pygame.transform.scale(duck_hunter_background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load dog
dog_img = pygame.image.load("Session8\\assets\\dog.png").convert_alpha()
dog_img = pygame.transform.scale(dog_img, (250, 200))

####################################################################################################
# MAIN GAME LOOP
####################################################################################################
running = True
while running:
    # Event loop
    for event in pygame.event.get():
        # Quit when the user presses the X at the top right
        if event.type == pygame.QUIT:
            running = False

    # Draw background
    display.blit(duck_hunter_background_img, (0,0)) # Put starting position in top left corner

    # Draw dog
    display.blit(dog_img, DOG_POS)

    # Update the pygame window and set clock tick
    pygame.display.update()
    clock.tick(FPS)

# Close and clean up
pygame.quit()