# !/usr/bin/env python3
# @file example7_moving_character.py
# SCRP: Example 7 - Advanced Timer Events
# Daryl Dang

"""
Example 7 - Advanced Timer Events
---------------------------------
An extension of previous examples from this session that adds a timer event.
"""

import pygame

# GLOBALS
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
FPS = 60
MARIO_X = 50
MARIO_Y = 375
MARIO_MOVEMENT = 5
THWOMP_X = 600
THWOMP_Y = -50
THWOMP_MOVEMENT = 10

# EVENTS
THWOMP_FALLING = pygame.USEREVENT + 1

# Initialize pygame and display window (this isn't that crucial for this basic program)
pygame.init()
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Advanced Timer Events")
clock = pygame.time.Clock()

# Load mario background in
mario_background_img = pygame.image.load("Session3\\example7_advanced_timer_event\\mario-bg.png").convert()
mario_background_img = pygame.transform.scale(mario_background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load mario in
mario_img = pygame.image.load("Session3\\example7_advanced_timer_event\\mario.png").convert_alpha()
mario_img = pygame.transform.scale(mario_img, (100, 100))

# Load thwomp in
thwomp_img = pygame.image.load("Session3\\example7_advanced_timer_event\\thwomp.png").convert_alpha()
thwomp_img = pygame.transform.scale(thwomp_img, (100, 100))
pygame.time.set_timer(THWOMP_FALLING, 2000) # Every 2 seconds (2000 milliseconds)

# Game loop
running = True
is_thwomp_falling = False # This variable will be used as a flag to make the thwomp fall
while running:
    for event in pygame.event.get():
        # Quit when the user presses the X at the top right
        if event.type == pygame.QUIT:
            running = False
        if event.type == THWOMP_FALLING:
            is_thwomp_falling = True

    # Keyboard Movement
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT]:
        MARIO_X -= MARIO_MOVEMENT
    if keys_pressed[pygame.K_RIGHT]:
        MARIO_X += MARIO_MOVEMENT
    if keys_pressed[pygame.K_UP]:
        MARIO_Y -= MARIO_MOVEMENT
    if keys_pressed[pygame.K_DOWN]:
        MARIO_Y += MARIO_MOVEMENT

    # Draw background (we need this in the game loop as without it you will see traces of mario)
    display.blit(mario_background_img, (0,0)) # Want background to take up whole screen

    # Draw mario in with the global positioning
    display.blit(mario_img, (MARIO_X, MARIO_Y))

    # Draw thwomp falling down if indicated by event
    if is_thwomp_falling:
        display.blit(thwomp_img, (THWOMP_X, THWOMP_Y))
        THWOMP_Y += THWOMP_MOVEMENT

    # Stop thwomp from falling once it reaches the bottom and reset position
    if THWOMP_Y >= SCREEN_HEIGHT:
        is_thwomp_falling = False
        THWOMP_Y = -50

    # Update the pygame window
    pygame.display.update()
    clock.tick(60)

# Close and clean up
pygame.quit()
