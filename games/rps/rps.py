# !/usr/bin/env python3
# @file memory_game.py
# SCRP: Memory Game
# Daryl Dang

"""
Memory Game
-----------

"""
####################################################################################################
# IMPORTS
####################################################################################################
import pygame

####################################################################################################
# GLOBALS/CONSTANTS
####################################################################################################
# Screen
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
FPS = 60

# Colours
FOREST_GREEN = (34, 139, 34)

####################################################################################################
# CLASS DEFINITIONS
####################################################################################################

####################################################################################################
# SETUP (init pygame, load images, create objects, create events, load fonts, load music, etc.)
####################################################################################################
# Initialize pygame and display window
pygame.init()
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Memory Game")
clock = pygame.time.Clock()

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

    # Display background
    display.fill(FOREST_GREEN)

    # Update the pygame window and set clock tick
    pygame.display.update()
    clock.tick(FPS)

# Close and clean up
pygame.quit()
