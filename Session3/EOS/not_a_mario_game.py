# !/usr/bin/env python3
# @file not_a_mario_game.py
# SCRP: EOS - Not a Mario Game
# Daryl Dang

"""
EOS - Not a Mario Game
-----------------
Combining everything in session 3 and making it more complex by adding elements such as:
- boundaries
- gravity
"""
####################################################################################################
# IMPORTS
####################################################################################################
import pygame

####################################################################################################
# GLOBALS
####################################################################################################
# Screen
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
FPS = 60

# Character (guy)
GUY_WIDTH = 100
GUY_HEIGHT = 100
GUY_X = 50
GUY_Y = 375
GUY_HORIZONTAL_MOVEMENT = 5
JUMP_HEIGHT = 20
GUY_Y_VELOCITY = JUMP_HEIGHT
GRAVITY = 1
is_jumping = False
jump_count = 10

# Block
BLOCK_X = 600
BLOCK_Y = -50
BLOCK_MOVEMENT = 7
is_block_falling = False # This variable will be used as a flag to make the block fall

####################################################################################################
# EVENTS
####################################################################################################
BLOCK_FALLING = pygame.USEREVENT + 1

####################################################################################################
# FUNCTIONS
####################################################################################################
def check_guy_keyboard_movement():
    # Define global variables
    global GUY_X, GUY_Y, GUY_HORIZONTAL_MOVEMENT, is_jumping, jump_count

    # Check what key was last pressed
    keys_pressed = pygame.key.get_pressed()

    # Check horizontal movement keys and make sure they are within the boundaries
    if keys_pressed[pygame.K_LEFT] and GUY_X >= 0:
        GUY_X -= GUY_HORIZONTAL_MOVEMENT
    if keys_pressed[pygame.K_RIGHT] and (GUY_X + GUY_WIDTH) <= SCREEN_WIDTH:
        GUY_X += GUY_HORIZONTAL_MOVEMENT

    # Check if mario is not in the state of jumping and if not, turn into jump state
    if not(is_jumping):
        if keys_pressed[pygame.K_UP]:
            is_jumping = True

def make_guy_jump():
    # Define global variables
    global is_jumping, GUY_Y, GUY_Y_VELOCITY, JUMP_HEIGHT

    # Check if in jumping state
    if is_jumping:
        GUY_Y -= GUY_Y_VELOCITY # Subtract the velocity from GUY's y position
        GUY_Y_VELOCITY -= GRAVITY # Add to our velocity with our gravity value

        # If our velocity has reached the negative jump height then reset
        if GUY_Y_VELOCITY < -JUMP_HEIGHT:
            is_jumping = False # Change state back to false
            GUY_Y_VELOCITY = JUMP_HEIGHT # Reset velocity to original jump height

####################################################################################################
# SETUP (Initialize and load images)
####################################################################################################
# Initialize pygame and display window
pygame.init()
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Not a Mario Game")
clock = pygame.time.Clock()

# Load background in
not_mario_background_img = pygame.image.load("Session3\\EOS\\not-mario-bg.png").convert()
not_mario_background_img = pygame.transform.scale(not_mario_background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load character in
not_mario_img = pygame.image.load("Session3\\EOS\\not-mario.png").convert_alpha()
not_mario_img = pygame.transform.scale(not_mario_img, (GUY_WIDTH, GUY_HEIGHT))

# Load block in
block_img = pygame.image.load("Session3\\EOS\\block.png").convert_alpha()
block_img = pygame.transform.scale(block_img, (100, 100))
pygame.time.set_timer(BLOCK_FALLING, 2000) # Every 2 seconds (2000 milliseconds)

####################################################################################################
# GAME LOOP
####################################################################################################
running = True
while running:
    # Event loop
    for event in pygame.event.get():
        # Quit when the user presses the X at the top right
        if event.type == pygame.QUIT:
            running = False
        # Block will fall based on timer event
        if event.type == BLOCK_FALLING:
            is_block_falling = True

    # Check character keyboard movement using function below
    check_guy_keyboard_movement()

    # Make character jump
    make_guy_jump()

    # Draw Background
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

    # Update the pygame window and set clock tick
    pygame.display.update()
    clock.tick(FPS)

# Close and clean up
pygame.quit()
