# !/usr/bin/env python3
# @file step2_duck_class.py
# SCRP: Step 2 - Duck Class
# Daryl Dang

"""
Step 2 - Duck Class
------------------------------------
This step will go over how to make a duck class and give it basic methods to be drawn to the screen.
"""
####################################################################################################
# IMPORTS
####################################################################################################
import pygame
import time
####################################################################################################
# GLOBALS/CONSTANTS
####################################################################################################
# Screen
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
FPS = 60

# Dog
DOG_POS = (360, 400) # this is a tuple because it is not moving
DOG_SIZE = (250, 200) # this is a tuple because the dog is not changing size

# Duck
DUCK_SIZE = (100, 100) # this is a tuple because the duck is not changing size

####################################################################################################
# CLASS DEFINITIONS
####################################################################################################
class Duck:
    """
    Duck class.

    Attributes
    ----------
    display (pygame.Surface): The display that the duck will be drawn to
    duck_img (pygame.Surface): Image of duck loaded from file
    duck_pos (list): Position of the duck
    """
    def __init__(self, display: pygame.Surface, duck_img_file_path: str):
        """
        Init method

        Parameters
        ----------
            display (pygame.Surface): The display that the duck will be drawn to
            duck_img_file_path (str): The file location of the duck image
        """
        # Store the display that we are drawing the duck to
        self.display = display

        # Load duck
        self.duck_img = pygame.image.load(duck_img_file_path).convert_alpha()
        self.duck_img = pygame.transform.scale(self.duck_img, DUCK_SIZE)

        # Load a default position for the duck to start (bottom of the screen)
        self.duck_pos = [500, 700]

        # Initialize speed of duck for x and y
        self.duck_x_speed = 5 # this will change when it hits a wall
        self.duck_y_speed = -2

    def draw(self):
        """
        This will draw the duck to the display window using it's current set position (duck_pos).
        """
        self.display.blit(self.duck_img, self.duck_pos)

    def update_position(self):
        """
        Move the duck upwards and side to side. This will check if the duck hits the side of the
        wall and flip the direction of the x speed so it goes the other way.
        """
        # Update x and y position
        self.duck_pos[0] += self.duck_x_speed
        self.duck_pos[1] += self.duck_y_speed

        # Check if hitting the wall
        # The current method is simplified but can be condensed into one if statement... How do we
        # do this?
        if self.duck_pos[0] <= 0:
            self.duck_x_speed = 5 # go to the right instead
            self.duck_img = pygame.transform.flip(self.duck_img, True, False) # Flip vertically
        elif self.duck_pos[0] + DUCK_SIZE[1] >= SCREEN_WIDTH:
            self.duck_x_speed = -5 # go to the left instead
            self.duck_img = pygame.transform.flip(self.duck_img, True, False) # Flip vertically

####################################################################################################
# SETUP
####################################################################################################
# Initialize pygame and display window
pygame.init()
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Duck Hunter")
clock = pygame.time.Clock()

# Load background
duck_hunter_background_img = pygame.image.load("Session8\\assets\\background.png").convert()
duck_hunter_background_img = pygame.transform.scale(duck_hunter_background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load dog
dog_img = pygame.image.load("Session8\\assets\\dog.png").convert_alpha()
dog_img = pygame.transform.scale(dog_img, DOG_SIZE)

# Create our duck object
duck = Duck(display, "Session8\\assets\\duck.png")

####################################################################################################
# MAIN GAME LOOP
####################################################################################################
running = True
time.sleep(5)

while running:
    # Event loop
    for event in pygame.event.get():
        # Quit when the user presses the X at the top right
        if event.type == pygame.QUIT:
            running = False

    # Draw background
    display.blit(duck_hunter_background_img, (0,0)) # Put starting position in top left corner

    # Draw dog
    display.blit(dog_img, DOG_POS)

    # Draw duck using draw method from class
    duck.draw()

    # Update the position of our duck
    duck.update_position()

    # Update the pygame window and set clock tick
    pygame.display.update()
    clock.tick(FPS)

# Close and clean up
pygame.quit()