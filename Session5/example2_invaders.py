#import important libraries

import pygame
import random



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

#Invaders stored in a list
invader_image = []
invader_X = []
invader_Y = []
invader_X_movement = []
invader_Y_movement = []
number_of_invaders = 8 #change variable to add more invaders

#for loop to initialize invaders
for num in range(number_of_invaders):
    invader_image.append(pygame.image.load('images\enemy.png').convert_alpha())
    invader_image[num] = pygame.transform.scale(invader_image[num],(50,50))
    #generate the places the invaders will spawn
    invader_X.append(random.randint(64,737))
    invader_Y.append(random.randint(30,180))

    invader_X_movement.append(1.2)
    invader_Y_movement.append(50)

#blit invader
def invader(x,y,i):
    screen.blit(invader_image[i],(x,y))

#game loop
running = True

while running:
    clock.tick(FPS)  # Limit the frame rate
    screen.fill((BLACK)) #fill screen at the top of the loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #for loop to move invaders on the x axis
    for i in range(number_of_invaders):
        invader_X[i] += invader_X_movement[i]

    #movement of invader on the Y axis
    for i in range(number_of_invaders):
        if invader_X[i] >= 735 or invader_X[i] <= 0:
            invader_X_movement[i] *= -1
            invader_Y[i] += invader_Y_movement[i]
        invader(invader_X[i], invader_Y[i], i)
    pygame.display.update()

pygame.quit()