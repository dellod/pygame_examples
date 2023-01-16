# !/usr/bin/env python3
# @file example6_simple_timer_event.py
# SCRP: Example 6 - Simple Timer Event
# Daryl Dang

"""
Example 6 - Simple Timer Event
---------------------------------
This example goes over a simple timer event to show the basics of events.
"""

import pygame
import random

# GLOBALS
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
COLOUR = [255, 255, 255]
CENTER = [250, 250]
RADIUS =  100

# EVENTS
SIMPLE_PRINT_EVENT = pygame.USEREVENT + 1
COLOUR_CHANGE_EVENT = pygame.USEREVENT + 2

# Initialize pygame and display window (this isn't that crucial for this basic program)
pygame.init()
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Timer Event")

# Trigger Events with a Timer
pygame.time.set_timer(SIMPLE_PRINT_EVENT, 2000) # Every 2 seconds (2000 milliseconds)
pygame.time.set_timer(COLOUR_CHANGE_EVENT, 1000) # Every 1 seconds (1000 milliseconds)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        # Quit when the user presses the X at the top right
        if event.type == pygame.QUIT:
            running = False

        if event.type == SIMPLE_PRINT_EVENT:
            # Print statement every 2 seconds
            print("Simple event that prints to the console every 2 seconds!")
            print("--------------------------------------------------------")

        if event.type == COLOUR_CHANGE_EVENT:
            # Change the colour randomly every 1 seconds
            COLOUR = [random.uniform(0, 255), random.uniform(0, 255), random.uniform(0, 255)]

    pygame.draw.circle(display, COLOUR, CENTER, RADIUS, 0)

    # Update the pygame window
    pygame.display.update()

# Close and clean up
pygame.quit()
