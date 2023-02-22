# !/usr/bin/env python3
# @file step4_hitting_duck.py
# SCRP: Step 4 - Hitting Duck
# Daryl Dang

"""
Step 4 - Hitting Duck
---------------------
This step will go over how to move the previously created duck object.
"""
####################################################################################################
# IMPORTS
####################################################################################################
import pygame
import math

####################################################################################################
# GLOBALS/CONSTANTS
####################################################################################################
# Screen
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
FPS = 60

# Crosshair
CROSSHAIR_SIZE = (50, 50)

# Dog
DOG_POS = (360, 400) # this is a tuple because it is not moving
DOG_SIZE = (250, 200) # this is a tuple because the dog is not changing size

# Duck
DEFAULT_DUCK_POS = (500, 700)
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
        self.duck_pos = list(DEFAULT_DUCK_POS)

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

    def get_dist(self, x1, y1, x2, y2):
        """
        Get distance between two points on the display window given their x and y positions. Point 1
        should correspond to x1 and y1 while Point 2 should correspond to x2 and y2. This formula is
        based on Pythagorean Theorem.

        Parameters
        ----------
        x1 (float) - x-coordinate of point 1
        y1 (float) - y-coordinate of point 1
        x2 (float) - x-coordinate of point 2
        y2 (float) - y-coordinate of point 2

        Returns
        -------
        distance (float) - distance between the two points specified
        """
        distance = math.sqrt((math.pow(x2 - x1, 2)) + (math.pow(y2 - y1, 2))) # Pythagorean theorem
        return distance

    def check_if_duck_is_hit(self, mouse_pos: list, mouse_pressed: list):
        """
        This will check collision of the duck with current mouse position and return if it is hit.

        Parameters
        ----------
            mouse_pos (list): X and Y position of the mouse in a list.

        Returns
        -------
            (bool): True if touching and clicked button, False otherwise.
        """
        # We have to add the size of our duck to our duck pos because we want to make it the center
        distance = self.get_dist(mouse_pos[0], mouse_pos[1],
                                 (self.duck_pos[0] + DUCK_SIZE[0]/2), (self.duck_pos[1] +  DUCK_SIZE[1]/2))

        if distance <= 50 and  mouse_pressed[0]:
            return True # That means we are touching and have clicked our button
        else:
            return False # That means we are not touching

    def reset_position(self):
        """
        Resets the position of Duck to the Default position.
        """
        self.duck_pos = list(DEFAULT_DUCK_POS)

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

# Load crosshair (will follow our mouse)
crosshair_img = pygame.image.load("Session8\\assets\\crosshair.png").convert_alpha()
crosshair_img = pygame.transform.scale(crosshair_img, CROSSHAIR_SIZE)

# Create our duck object
duck = Duck(display, "Session8\\assets\\duck.png")

####################################################################################################
# MAIN GAME LOOP
####################################################################################################
running = True
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

    # Draw the crosshair that will follow the mouse around
    mouse_pos = pygame.mouse.get_pos()
    # We need to move the crosshair image so it's at the center where our mouse is
    crosshair_pos = [mouse_pos[0] - CROSSHAIR_SIZE[0]/2, mouse_pos[1] - CROSSHAIR_SIZE[1]/2]
    display.blit(crosshair_img, crosshair_pos)

    # Check if we are touching the duck and get the mouse pressed values
    mouse_pressed = pygame.mouse.get_pressed()
    if duck.check_if_duck_is_hit(mouse_pos, mouse_pressed):
        duck.reset_position()

    # Update the pygame window and set clock tick
    pygame.display.update()
    clock.tick(FPS)

# Close and clean up
pygame.quit()