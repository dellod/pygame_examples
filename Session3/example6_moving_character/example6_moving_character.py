# !/usr/bin/env python3
# @file example6_moving_character.py
# SCRP: Example 6 - Moving Character
# Daryl Dang

"""
Example 6 - Moving Character
---------------------------------
This example goes over how to improve movement from example 4 and used frame-based techniques
instead.
"""

import pygame

# GLOBALS
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
FPS = 60
GUY_X = 50
GUY_Y = 375
GUY_MOVEMENT = 5

# Initialize pygame and display window
pygame.init()
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Basic Keyboard Inputs")
clock = pygame.time.Clock()

# Load mario background in
not_mario_background_img = pygame.image.load("Session3\\example6_moving_character\\not-mario-bg.png").convert()
not_mario_background_img = pygame.transform.scale(not_mario_background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load mario in
not_mario_img = pygame.image.load("Session3\\example6_moving_character\\not-mario.png").convert_alpha() # Use this to keep the background transparent
not_mario_img = pygame.transform.scale(not_mario_img, (100, 100))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        # Quit when the user presses the X at the top right
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            pass
            # OLD METHOD
            # ----------
            # # UP key check
            # if event.key == pygame.K_UP:
            #     MARIO_Y -= 10 # Move by 10 pixels up
            # # DOWN key check
            # if event.key == pygame.K_DOWN:
            #     MARIO_Y += 10 # Move by 10 pixels up
            # # LEFT key check
            # if event.key == pygame.K_LEFT:
            #     MARIO_X -= 10 # Move by 10 pixels left
            # # RIGHT key check
            # if event.key == pygame.K_RIGHT:
            #     MARIO_X += 10 # Move by 10 pixels right

    # NEW METHOD
    # ----------
    # Movement checking - for the future, try to put this in its own function!

    # pygame.key.get_pressed() returns something called "ScancodeWrapper" that is almost like a
    # massive dictionary. This list contains all the keys that have been pressed on your keyboard
    # for a particular frame. That's why, if we index a pygame key, it will return True or False
    # based on if it was pressed.
    keys_pressed = pygame.key.get_pressed()

    # Here we index the keys and see if the dictionary returns true for each given key.
    if keys_pressed[pygame.K_LEFT]:
        GUY_X -= GUY_MOVEMENT
    if keys_pressed[pygame.K_RIGHT]:
        GUY_X += GUY_MOVEMENT
    if keys_pressed[pygame.K_UP]:
        GUY_Y -= GUY_MOVEMENT
    if keys_pressed[pygame.K_DOWN]:
        GUY_Y += GUY_MOVEMENT

    # Draw background (we need this in the game loop as without it you will see traces of your character)
    display.blit(not_mario_background_img, (0,0)) # Want background to take up whole screen

    # Draw character in with the global positioning
    display.blit(not_mario_img, (GUY_X, GUY_Y))

    # Update the pygame window and set clock tick
    pygame.display.update()
    clock.tick(FPS)

# Close and clean up
pygame.quit()
