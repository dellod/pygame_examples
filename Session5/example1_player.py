#import important libraries

import pygame

#Initializing setup variables for later
WHITE = (255, 255, 255)
BLACK = (0,0,0)
FPS = 60

#initialize pygame
pygame.init()
clock = pygame.time.Clock() # Clock for the game that will help us control the tick (frame) speed


#create screen
width = 800
height = 600
screen = pygame.display.set_mode((width,height))

#create caption
pygame.display.set_caption("Space Invader")

#player variables
player_image = pygame.image.load('images\spaceship.png').convert_alpha()
player_image = pygame.transform.scale(player_image,(75,50))
player_X = 400
player_Y = 523
player_X_movement = 1.7

#blit player
def player(x,y):
    #important to offset the x and y position slightly so the center of the ship is displayed correctly
    screen.blit(player_image,(x-16, y+10))

#Game loop
running = True

while running:
    clock.tick(FPS)  # Limit the frame rate so we have a controllable circle
    screen.fill((BLACK))  # fill screen at the top of the loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys_pressed = pygame.key.get_pressed()
    # Control player movement with arrow keys
    if keys_pressed[pygame.K_LEFT]:
        player_X -= player_X_movement
    if keys_pressed[pygame.K_RIGHT]:
        player_X += player_X_movement

    # stop player from going out of bounds
    if player_X <= 16:
        player_X = 16
    elif player_X >= 750:
        player_X = 750

    player(player_X, player_Y)
    pygame.display.update()

pygame.quit()
