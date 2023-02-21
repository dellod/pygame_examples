#import important libraries

import pygame
import random
import math


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


#blit player
def player(x,y):
    screen.blit(player_image,(x -16, y+10))

#Invaders stored in a list
invader_image = []
invader_X = []
invader_Y = []
invader_X_movement = []
invader_Y_movement = []
number_of_invaders = 8 #change variable to add more invaders

#blit invader
def invader(x,y,i):
    screen.blit(invader_image[i],(x,y))

#for loop to initialize invaders
for num in range(number_of_invaders):
    invader_image.append(pygame.image.load('images\enemy.png').convert_alpha())
    invader_image[num] = pygame.transform.scale(invader_image[num],(50,50))

    invader_X.append(random.randint(64,737))
    invader_Y.append(random.randint(30,180))

    invader_X_movement.append(1.2)
    invader_Y_movement.append(50)

#lasers

laser_image = pygame.image.load('images\laser.png').convert_alpha()
laser_image = pygame.transform.scale(laser_image,(30,58))
laser_X = 0
laser_Y = 500
laser_Y_movement = 5
laser_ready = True

#blit laser
def laser(x,y):
    global laser_ready
    screen.blit(laser_image,(x,y))
    laser_ready= False

#function to detect collision

def isCollision(x1,x2,y1,y2):
    #calculate distance
    distance = math.sqrt((math.pow(x1 - x2, 2)) + (math.pow(y1 - y2, 2)))
    #if distance variable is at least 30 pixels away then we detect collision
    if distance <= 30:
        return True
    else:
        return False

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
        player_X += -1.7
    if keys_pressed[pygame.K_RIGHT]:
        player_X += 1.7
    if keys_pressed[pygame.K_SPACE]:
        # if no laser has been shot then call laser function and place laser X coord where player X coord is
        if laser_ready:
            #shoot from where the player is on the x axis
            laser_X = player_X
            laser(laser_X, laser_Y)

    

    # for loop to move invaders on the x axis
    for i in range(number_of_invaders):
        invader_X[i] += invader_X_movement[i]

    # if laser has gone to the top of the screen, reset laser state to rest
    if laser_Y <= 0:
        laser_Y = 550
        laser_ready= True

    if not laser_ready:
        laser(laser_X, laser_Y)
        laser_Y -= laser_Y_movement


     # movement of invader
    for i in range(number_of_invaders):
        # if invader is at one of the boundaries of the screen
        if invader_X[i] >= 735 or invader_X[i] <= 0:
            # reverse movement of invader
            invader_X_movement[i] *= -1
            invader_Y[i] += invader_Y_movement[i]
        # collision detection for invader with laser
        collision = isCollision(laser_X, invader_X[i], laser_Y, invader_Y[i])
        #if it's true that the laser collided with an invader
        if collision:
            #reset laser's Y position
            laser_Y = 550
            #set laser back to rest to allow player to shoot again
            laser_ready= True
            #reset the invader that was shot to a new location near the top
            invader_X[i] = random.randint(64, 736)
            invader_Y[i] = random.randint(30, 200)
            invader_X_movement[i] *= -1

        invader(invader_X[i], invader_Y[i], i)

    # stop player from going out of bounds
    if player_X <= 16:
        player_X = 16
    elif player_X >= 750:
        player_X = 750

    player(player_X, player_Y)
    pygame.display.update()

pygame.quit()
