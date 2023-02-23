#import important libraries

import pygame
from pygame import mixer

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

#Background Sound
mixer.music.load('sounds\some_playstation_ski-core_instrumental.wav')
#Sets volume to a floating point value between 0.0 and 1.0
mixer.music.set_volume(0.15)
mixer.music.play(-1)

#player variables
player_image = pygame.image.load('images\spaceship.png').convert_alpha()
player_image = pygame.transform.scale(player_image,(75,50))
player_X = 400
player_Y = 523
player_X_movement = 1.7

#blit player
def player(x,y):
    screen.blit(player_image,(x -16, y+10))

#lasers

laser_image = pygame.image.load('images\laser.png').convert_alpha()
laser_image = pygame.transform.scale(laser_image,(30,58))
laser_X = 0
laser_Y = 500
laser_X_movement = 0
laser_Y_movement = 5
laser_ready = True
laser_sound = mixer.Sound("sounds\laser.wav")

#blit laser
def laser(x,y):
    global laser_ready
    screen.blit(laser_image,(x,y))
    laser_ready = False



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
    if keys_pressed[pygame.K_SPACE]:
        # if no laser has been shot then call laser function and place laser X coord where player X coord is
        if laser_ready:
            #shoot from where the player is on the x axis
            laser_X = player_X
            laser(laser_X, laser_Y)

            laser_sound.play()

    # if laser has gone to the top of the screen, reset laser state to rest
    if laser_Y <= 0:
        laser_Y = 550
        laser_ready= True

    if not laser_ready:
        laser(laser_X, laser_Y)
        laser_Y -= laser_Y_movement

    # stop player from going out of bounds
    if player_X <= 16:
        player_X = 16
    elif player_X >= 750:
        player_X = 750

    player(player_X, player_Y)
    pygame.display.update()

pygame.quit()
