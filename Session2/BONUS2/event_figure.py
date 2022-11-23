# !/usr/bin/env python3
# @file event_figure.py
# SCRP: BONUS 2 - Event Figure
# Daryl Dang

import pygame

# CONSTANTS
WIDTH   =   1000
HEIGHT  =   500
FPS     =   60
BLACK   =   (0, 0, 0)

# Initialize pygame and display window
pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Event Figure")
clock = pygame.time.Clock()

# Add background (optional)
# Source: https://www.deviantart.com/andre-tachibana/art/Megaman-7-background-314483701
background_img = pygame.image.load("Session2\\BONUS2\\background.jpg")
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

# GAME VARIABLES
x = WIDTH / 2 - 50
y = 300
RUN_TIMER = 50
megaman_width = 100
megaman_height = 100

# Stand
stand_img = pygame.image.load("Session2\\BONUS2\\standing.png")
stand_img = pygame.transform.scale(stand_img, (megaman_width, megaman_height))
is_standing = True
STAND_EVENT = pygame.USEREVENT + 1
STAND_TIMER = 2000
pygame.time.set_timer(STAND_EVENT, STAND_TIMER)

# Run 1
run1_img = pygame.image.load("Session2\\BONUS2\\run1.png")
run1_img = pygame.transform.scale(run1_img, (megaman_width, megaman_height))
is_run1 = False
RUN1_EVENT = pygame.USEREVENT + 2

# Run 2
run2_img = pygame.image.load("Session2\\BONUS2\\run2.png")
run2_img = pygame.transform.scale(run2_img, (megaman_width, megaman_height))
RUN2_EVENT = pygame.USEREVENT + 3
is_run2 = False

# Run 3
run3_img = pygame.image.load("Session2\\BONUS2\\run3.png")
run3_img = pygame.transform.scale(run3_img, (megaman_width, megaman_height))
is_run3 = False
RUN3_EVENT = pygame.USEREVENT + 4

# Game loop
running = True
while running:
    # Limit clock frame it
    clock.tick(FPS)

    # Draw background image
    display.blit(background_img, (0, 0))

    # Check events
    for event in pygame.event.get():
        # Quit when the user presses the X at the top right
        if event.type == pygame.QUIT:
            running = False

        # Turns off the standing
        if event.type == STAND_EVENT:
            is_standing = False
            pygame.event.post(pygame.event.Event(RUN1_EVENT))
        if event.type == RUN1_EVENT:
            is_run1 = True
            is_run2 = False
            is_run3 = False
            pygame.time.delay(RUN_TIMER)
            pygame.event.post(pygame.event.Event(RUN2_EVENT))
        if event.type == RUN2_EVENT:
            is_run1 = False
            is_run2 = True
            is_run3 = False
            pygame.time.delay(RUN_TIMER)
            pygame.event.post(pygame.event.Event(RUN3_EVENT))
        if event.type == RUN3_EVENT:
            is_run1 = False
            is_run2 = False
            is_run3 = True
            pygame.time.delay(RUN_TIMER)
            pygame.event.post(pygame.event.Event(RUN1_EVENT))

    # Draw images
    if is_standing:
        display.blit(stand_img, (x, y))
    elif is_run1:
        display.blit(run1_img, (x, y))
    elif is_run2:
        display.blit(run2_img, (x, y))
    elif is_run3:
        display.blit(run3_img, (x, y))

    # Update pygame window
    pygame.display.update()

# Close and clean up
pygame.quit()
