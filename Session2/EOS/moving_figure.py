# !/usr/bin/env python3
# @file moving_figure.py
# SCRP: EOS - Moving Figure
# Daryl Dang

import pygame
import math
# GLOBALS
WHITE   =   (255, 255, 255)
BLACK   =   (0, 0, 0)
YELLOW  =   (255, 255, 0)
PINK    =   (255, 192, 203)
FPS = 60

# Initialize pygame and display window
pygame.init()
display = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Moving Figure")
clock = pygame.time.Clock() # Clock for the game that will help us control the tick (frame) speed

# GAME VARIABLES
# Face
face_pos = [250, 250]
face_rad = 100

# Mouth
mouth_pos = [250, 300]
mouth_rad = 30

# Left eye
left_eye_rect = [200, 200, 30, 50]
left_eye_pupil_rect = [205, 225, 20, 25]
left_eyebrow_rect = [200, 185, 30, 25]

# Right eye
right_eye_rect = [270, 200, 30, 50]
right_eye_pupil_rect = [275, 225, 20, 25]
right_eyebrow_rect = [270, 185, 30, 25]

# Game loop
running = True
while running:
    clock.tick(FPS) # Limit the frame rate so we have a controllable circle
    for event in pygame.event.get():
        # Quit when the user presses the X at the top right
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen before drawing a new circle
    display.fill(WHITE)

    # Draw main face
    pygame.draw.circle(display, YELLOW, face_pos, face_rad, 0)
    pygame.draw.circle(display, BLACK, face_pos, face_rad, 1) # Face border

    # Draw mouth
    pygame.draw.circle(display, PINK, mouth_pos, mouth_rad, 0)
    pygame.draw.circle(display, BLACK, mouth_pos, mouth_rad, 1) # Mouth border

    # Draw left eye (not moving)
    pygame.draw.ellipse(display, WHITE, left_eye_rect, 0)
    pygame.draw.ellipse(display, BLACK, left_eye_rect, 1)

    pygame.draw.ellipse(display, BLACK, left_eye_pupil_rect, 0)

    pygame.draw.arc(display, BLACK, left_eyebrow_rect, 0, math.pi)

    # Draw right eye (moving)
    pygame.draw.ellipse(display, WHITE, right_eye_rect, 0)
    pygame.draw.ellipse(display, BLACK, right_eye_rect, 1)

    pygame.draw.ellipse(display, BLACK, right_eye_pupil_rect, 0)

    pygame.draw.arc(display, BLACK, right_eyebrow_rect, 0, math.pi)

    # Update the pygame window
    pygame.display.update()

# Close and clean up
pygame.quit()
