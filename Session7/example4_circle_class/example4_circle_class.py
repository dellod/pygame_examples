# !/usr/bin/env python3
# @file example4_circle_class.py
# SCRP: Example 4 - Circle Class
# Daryl Dang

"""
Example 4 - Circle Class
-----------------------
A circle class that stores key parameters such as the:
- Radius
- Colour
- Position

It will also have methods such as:
- Drawing the circle
- Change colour when mouse touches
"""
####################################################################################################
# IMPORTS
####################################################################################################
import pygame

####################################################################################################
# CONSTANTS
####################################################################################################
# Screen
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
FPS = 60

# Colours
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

####################################################################################################
# CIRCLE CLASS
####################################################################################################
class Circle:
    """
    Circle class.

    Attributes
    ----------
    radius (float): Radius of the circle
    colour (tuple): Colour levels of the circle
    position (list): Position of the circle [x, y]
    my_circle (pygame.Rect): Stores the circle object when drawn (used for mouse detection)
    """
    def __init__(self, radius, colour, position):
        """
        Init function

        Parameters
        ----------
            radius (float): Radius of the circle
            colour (tuple): Colour levels of the circle
            position (list): Position of the circle [x, y]
        """
        self.radius = radius
        self.colour = colour
        self.position = position

    def draw(self, display):
        """
        Draws the circle to the display.

        Parameters
        ----------
            display (pygame.Surface): Display window of your game
        """
        self.my_circle = pygame.draw.circle(display, self.colour, self.position, self.radius, 0)

    def change_colour_when_hovered(self, mouse_pos):
        """
        Changes the colour of the circle when the mouse has hovered over it.

        Parameters
        ----------
            mouse_pos (list): Position of the mouse [x, y]
        """
        # Check the collision and store in variable (bool)
        collide = self.my_circle.collidepoint(mouse_pos)

         # If we have collided with our circle, change the colour to black permanently.
        if collide:
            self.colour = BLACK

####################################################################################################
# SETUP
####################################################################################################
# Initialize pygame and display window
pygame.init()
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Circle Class")
clock = pygame.time.Clock()

# Create circle classes
my_circle_1 = Circle(50, RED, [150, 100])
my_circle_2 = Circle(50, GREEN, [400, 125])
my_circle_3 = Circle(75, BLUE, [350, 400])
my_circle_4 = Circle(50, GREEN, [150, 375])
my_circle_5 = Circle(100, BLUE, [250, 250])

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

    # Draw white background
    display.fill(WHITE)

    # Draw all circles
    my_circle_1.draw(display)
    my_circle_2.draw(display)
    my_circle_3.draw(display)
    my_circle_4.draw(display)
    my_circle_5.draw(display)

    # Check if the mouse has hovered over all circles
    mouse_pos = pygame.mouse.get_pos()
    my_circle_1.change_colour_when_hovered(mouse_pos)
    my_circle_2.change_colour_when_hovered(mouse_pos)
    my_circle_3.change_colour_when_hovered(mouse_pos)
    my_circle_4.change_colour_when_hovered(mouse_pos)
    my_circle_5.change_colour_when_hovered(mouse_pos)

    # Update the pygame window and set clock tick
    pygame.display.update()
    clock.tick(FPS)

# Close and clean up
pygame.quit()