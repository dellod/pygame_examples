# !/usr/bin/env python3
# @file moving_figure.py
# SCRP: EOS - Moving Figure
# Daryl Dang

import pygame
import math
import random

# GLOBALS
WIDTH   =   500
HEIGHT  =   500
WHITE   =   (255, 255, 255)
BLACK   =   (0, 0, 0)
YELLOW  =   (255, 255, 0)
PINK    =   (255, 192, 203)
FPS     =   60

# Initialize pygame and display window
pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Figure")
clock = pygame.time.Clock() # Clock for the game that will help us control the tick (frame) speed
start_ticks = pygame.time.get_ticks()

# GAME VARIABLES
# Center
x = 250
x_mov = random.uniform(-10, 10) # x movement random from -10 to 10
y = 250
y_mov = random.uniform(-10, 10) # y movement random from -10 to 10

# Face
face_pos = [x, y]
face_rad = 100

# Mouth
mouth_pos = [x, y + 50]
mouth_rad = 30

# Left eye
left_eye_rect = [x - 50, y - 50, 30, 50]
left_eye_pupil_rect = [x - 45, y - 25, 20, 25]
left_eyebrow_rect = [x- 50, y - 65, 30, 25]

# Right eye
right_eye_rect = [x + 20, y - 50, 30, 50]
right_eye_pupil_rect = [x + 25, y - 25, 20, 25]
right_eyebrow_rect = [x + 20, y - 65, 30, 25]

right_eye_closed_start = [right_eye_rect[0], right_eye_rect[3] / 2 + right_eye_rect[1]]
right_eye_closed_end = [right_eye_rect[0] + right_eye_rect[2], right_eye_rect[3] / 2 + right_eye_rect[1]]

BLINK_EVENT = pygame.USEREVENT + 1
blink_timer = 1000
is_blinking = False

# TIMERS
pygame.time.set_timer(BLINK_EVENT, blink_timer)

# Game loop
running = True
while running:
    clock.tick(FPS) # Limit the frame rate so we have a controllable circle
    for event in pygame.event.get():
        # Blink event
        if event.type == BLINK_EVENT:
            is_blinking= not(is_blinking)
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
    pygame.draw.arc(display, BLACK, right_eyebrow_rect, 0, math.pi)
    if is_blinking:
        # Eye is blinking
        pygame.draw.line(display, BLACK, right_eye_closed_start, right_eye_closed_end, 10)
    else:
        # Eye is open
        pygame.draw.ellipse(display, WHITE, right_eye_rect, 0)
        pygame.draw.ellipse(display, BLACK, right_eye_rect, 1)
        pygame.draw.ellipse(display, BLACK, right_eye_pupil_rect, 0)

    if x + face_rad >= WIDTH or x - face_rad <= 0:
        x_mov *= -1

    if y + face_rad >= HEIGHT or y - face_rad <= 0:
        y_mov *= -1

    # Update position
    x += x_mov
    y += y_mov

    # Update all positions
    # Face
    face_pos = [x, y]
    face_rad = 100

    # Mouth
    mouth_pos = [x, y + 50]
    mouth_rad = 30

    # Left eye
    left_eye_rect = [x - 50, y - 50, 30, 50]
    left_eye_pupil_rect = [x - 45, y - 25, 20, 25]
    left_eyebrow_rect = [x- 50, y - 65, 30, 25]

    # Right eye
    right_eye_rect = [x + 20, y - 50, 30, 50]
    right_eye_pupil_rect = [x + 25, y - 25, 20, 25]
    right_eyebrow_rect = [x + 20, y - 65, 30, 25]

    right_eye_closed_start = [right_eye_rect[0], right_eye_rect[3] / 2 + right_eye_rect[1]]
    right_eye_closed_end = [right_eye_rect[0] + right_eye_rect[2], right_eye_rect[3] / 2 + right_eye_rect[1]]

    # Update the pygame window
    pygame.display.update()

# Close and clean up
pygame.quit()
