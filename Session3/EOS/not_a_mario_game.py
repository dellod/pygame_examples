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

# Mario
MARIO_WIDTH = 100
MARIO_HEIGHT = 100
MARIO_X = 50
MARIO_Y = 375
MARIO_HORIZONTAL_MOVEMENT = 5
JUMP_HEIGHT = 20
MARIO_Y_VELOCITY = JUMP_HEIGHT
GRAVITY = 1
is_jumping = False
jump_count = 10

# Thwomp
THWOMP_X = 600
THWOMP_Y = -50
THWOMP_MOVEMENT = 7
is_thwomp_falling = False # This variable will be used as a flag to make the thwomp fall

####################################################################################################
# EVENTS
####################################################################################################
THWOMP_FALLING = pygame.USEREVENT + 1

####################################################################################################
# FUNCTIONS
####################################################################################################
def check_mario_keyboard_movement():
    # Define global variables
    global MARIO_X, MARIO_Y, MARIO_HORIZONTAL_MOVEMENT, is_jumping, jump_count

    # Check what key was last pressed
    keys_pressed = pygame.key.get_pressed()

    # Check horizontal movement keys and make sure they are within the boundaries
    if keys_pressed[pygame.K_LEFT] and MARIO_X >= 0:
        MARIO_X -= MARIO_HORIZONTAL_MOVEMENT
    if keys_pressed[pygame.K_RIGHT] and (MARIO_X + MARIO_WIDTH) <= SCREEN_WIDTH:
        MARIO_X += MARIO_HORIZONTAL_MOVEMENT

    # Check if mario is not in the state of jumping and if not, turn into jump state
    if not(is_jumping):
        if keys_pressed[pygame.K_UP]:
            is_jumping = True

def make_mario_jump():
    # Define global variables
    global is_jumping, MARIO_Y, MARIO_Y_VELOCITY, JUMP_HEIGHT

    # Check if in jumping state
    if is_jumping:
        MARIO_Y -= MARIO_Y_VELOCITY # Subtract the velocity from Mario's y position
        MARIO_Y_VELOCITY -= GRAVITY # Add to our velocity with our gravity value

        # If our velocity has reached the negative jump height then reset
        if MARIO_Y_VELOCITY < -JUMP_HEIGHT:
            is_jumping = False # Change state back to false
            MARIO_Y_VELOCITY = JUMP_HEIGHT # Reset velocity to original jump height

####################################################################################################
# SETUP (Initialize and load images)
####################################################################################################
# Initialize pygame and display window
pygame.init()
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Not a Mario Game")
clock = pygame.time.Clock()

# Load mario background in
mario_background_img = pygame.image.load("Session3\\EOS\\mario-bg.png").convert()
mario_background_img = pygame.transform.scale(mario_background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load mario in
mario_img = pygame.image.load("Session3\\EOS\\mario.png").convert_alpha()
mario_img = pygame.transform.scale(mario_img, (MARIO_WIDTH, MARIO_HEIGHT))

# Load thwomp in
thwomp_img = pygame.image.load("Session3\\EOS\\thwomp.png").convert_alpha()
thwomp_img = pygame.transform.scale(thwomp_img, (100, 100))
pygame.time.set_timer(THWOMP_FALLING, 2000) # Every 2 seconds (2000 milliseconds)

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
        # Thwomp will fall based on timer event
        if event.type == THWOMP_FALLING:
            is_thwomp_falling = True

    # Check mario keyboard movement using function below
    check_mario_keyboard_movement()

    # Make Mario jump
    make_mario_jump()

    # Draw Background
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

    # Update the pygame window and set clock tick
    pygame.display.update()
    clock.tick(FPS)

# Close and clean up
pygame.quit()
