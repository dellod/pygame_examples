# !/usr/bin/env python3
# @file example1_display_window.py
# SCRP: Example 1 - Display Window
# Daryl Dang

# 1. Need to import the PyGame library
import pygame

# 2. Initialize all the PyGame modules
pygame.init()

# 3. Create the display window
display = pygame.display.set_mode((500, 500))  # 500 pixels by 500 pixels
<<<<<<< HEAD
=======
pygame.display.set_caption("My Game") # Set the name of the window
>>>>>>> 5f909bad9b06152ab1efb5c4f1f0fab9e87953de

# 4. Create a "game" (infinite) loop
running = True
while running:
    for event in pygame.event.get():
        # Quit when the user presses the X at the top right
        if event.type == pygame.QUIT:
            running = False

# 5. Close and clean up
pygame.quit()
