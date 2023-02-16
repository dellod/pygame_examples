# !/usr/bin/env python3
# @file example1_adding_text.py
# SCRP: Example 1 - Adding Text
# Daryl Dang

"""
Example 1 - Adding Text
----------------------
This example goes over how to add text.
"""

import pygame

# Initialize pygame and display window
pygame.init()
display = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Adding Text")

# Colours
WHITE = (255, 255, 255)

# Create our font and text to be used
font = pygame.font.Font('freesansbold.ttf', 32)
text_to_be_written = "Hello World :)"
text = font.render(text_to_be_written, True, WHITE)

# Game loop
running = True
while running:
    # Event Loop
    for event in pygame.event.get():
        # Quit when the user presses the X at the top right
        if event.type == pygame.QUIT:
            running = False

    # Add text using blit
    display.blit(text, (150, 250))

    # Update the pygame window
    pygame.display.update()

# Close and clean up
pygame.quit()
