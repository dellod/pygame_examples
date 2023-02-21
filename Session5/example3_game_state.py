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

#text for game over screen
game_over_font = pygame.font.Font('freesansbold.ttf',64)

#call this function when the game is deemed over
def game_over():
    game_over_text = game_over_font.render("GAME OVER",True,WHITE)
    screen.blit(game_over_text,(190,250))

#player variables
player_image = pygame.image.load('images\spaceship.png').convert_alpha()
player_image = pygame.transform.scale(player_image,(75,50))
player_X = 400
player_Y = 523
player_X_movement = 1.7


def player(x,y):
    screen.blit(player_image,(x -16, y+10))

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

    invader_X.append(random.randint(64,737))
    invader_Y.append(random.randint(30,180))

    invader_X_movement.append(20)
    invader_Y_movement.append(50)


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

    keys_pressed = pygame.key.get_pressed()
    # Control player movement with arrow keys
    if keys_pressed[pygame.K_LEFT]:
        player_X -= player_X_movement
    if keys_pressed[pygame.K_RIGHT]:
        player_X += player_X_movement

    #for loop to move invaders on the x axis
    for i in range(number_of_invaders):
        invader_X[i] += invader_X_movement[i]


    #movement of invader
    for i in range(number_of_invaders):
        #if invader is at the bottom fo the screen
        if invader_Y[i] >= 450:
            #if statement to check collision with player
            if abs(player_X - invader_X[i]) < 80:
                #every invader goes off screen as the game is now over!
                for j in range(number_of_invaders):
                    invader_Y[j] = 2000
                #call game_over function to turn into game_over state
                game_over()
                break
        # if invader is at one of the boundaries of the screen
        if invader_X[i] >= 735 or invader_X[i] <= 0:
            #reverse movement of invader
            invader_X_movement[i] *= -1
            invader_Y[i] += invader_Y_movement[i]



        invader(invader_X[i],invader_Y[i],i)

    # stop player from going out of bounds
    if player_X <= 16:
        player_X = 16
    elif player_X >= 750:
        player_X = 750

    player(player_X,player_Y)

    pygame.display.update()

pygame.quit()
