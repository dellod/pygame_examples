# !/usr/bin/env python3
# @file example8_advanced_timer_event.py
# SCRP: Example 8 - Advanced Timer Events
# Daryl Dang

"""
Example 8 - Advanced Timer Events
---------------------------------
An extension of previous examples from this session that adds a timer event.
"""

import pygame

# GLOBALS
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
FPS = 60
GUY_X = 50
GUY_Y = 375
GUY_MOVEMENT = 5
BLOCK_X = 600
BLOCK_Y = -50
BLOCK_MOVEMENT = 10

# EVENTS
BLOCK_FALLING = pygame.USEREVENT + 1

# Initialize pygame and display window (this isn't that crucial for this basic program)
pygame.init()
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Advanced Timer Events")
clock = pygame.time.Clock()

# Load background in
not_mario_background_img = pygame.image.load("Session3\\example8_advanced_timer_event\\not-mario-bg.png").convert()
not_mario_background_img = pygame.transform.scale(not_mario_background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load character in
not_mario_img = pygame.image.load("Session3\\example8_advanced_timer_event\\not-mario.png").convert_alpha()
not_mario_img = pygame.transform.scale(not_mario_img, (100, 100))

# Load enemy block in
block_img = pygame.image.load("Session3\\example8_advanced_timer_event\\block.png").convert_alpha()
block_img = pygame.transform.scale(block_img, (100, 100))
pygame.time.set_timer(BLOCK_FALLING, 2000) # Every 2 seconds (2000 milliseconds)

# Game loop
running = True
is_block_falling = False # This variable will be used as a flag to make the block fall
while running:
    for event in pygame.event.get():
        # Quit when the user presses the X at the top right
        if event.type == pygame.QUIT:
            running = False
        if event.type == BLOCK_FALLING:
            is_block_falling = True

    # Keyboard Movement
    keys_pressed = pygame.key.get_pressed()
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

    # Draw block falling down if indicated by event
    if is_block_falling:
        display.blit(block_img, (BLOCK_X, BLOCK_Y))
        BLOCK_Y += BLOCK_MOVEMENT

    # Stop block from falling once it reaches the bottom and reset position
    if BLOCK_Y >= SCREEN_HEIGHT:
        is_block_falling = False
        BLOCK_Y = -50

    # Update the pygame window
    pygame.display.update()
    clock.tick(60)

# Close and clean up
pygame.quit()
