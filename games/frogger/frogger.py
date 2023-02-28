# Frogger
# Simon Ly

# Importing and initializing pygame
import pygame
import random
from pygame import mixer

pygame.init()

# Some variables for game setup
SCREEN_SIZE = (650, 550)  # 16 across and 11 up for 50*50 blocks
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Setting up the display and clock
display = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Frogger")
clock = pygame.time.Clock()

# Initializing background image
background_image = pygame.image.load("games\\frogger\\assets\\road.png").convert()
background_image = pygame.transform.scale(background_image, SCREEN_SIZE)

#############################################################################################################
# Initializing frogger parameters and functions
#############################################################################################################
frog_size = (50, 50)
frog_X = SCREEN_SIZE[0]/2
frog_Y = SCREEN_SIZE[1] - frog_size[0]
frog_Y_start = frog_Y
frog_velocity = 10
frog_jump_ticks = 1
frog_jump_ready = True
frog_image = pygame.image.load("games\\frogger\\assets\\frogger.png").convert_alpha()
frog_image = pygame.transform.scale(frog_image, frog_size)
direction = "START"
frog_direction = "UP"
frog_dying_sound = mixer.Sound("games\\frogger\\assets\\dying_sound.wav")
frog_dying_sound.set_volume(0.05)

# Drawing frog function
def frog(x, y):
    display.blit(frog_image, (x - frog_size[0] / 2, y))


# Function called after each jump to make frog ready to jump again
def jump_reset():
    global frog_jump_ready, frog_jump_ticks, direction
    frog_jump_ready = True
    frog_jump_ticks = 1
    direction = "START"


# Function to determine the direction the frog will be facing
def direction_check(arrow_dir):
    global frog_image, frog_direction
    if frog_direction == "UP":
        if arrow_dir == "LEFT":
            frog_image = pygame.transform.rotate(frog_image, 90)
            frog_direction = "LEFT"
        elif arrow_dir == "DOWN":
            frog_image = pygame.transform.rotate(frog_image, 180)
            frog_direction = "DOWN"
        elif arrow_dir == "RIGHT":
            frog_image = pygame.transform.rotate(frog_image, 270)
            frog_direction = "RIGHT"
    elif frog_direction == "LEFT":
        if arrow_dir == "DOWN":
            frog_image = pygame.transform.rotate(frog_image, 90)
            frog_direction = "DOWN"
        elif arrow_dir == "RIGHT":
            frog_image = pygame.transform.rotate(frog_image, 180)
            frog_direction = "RIGHT"
        elif arrow_dir == "UP":
            frog_image = pygame.transform.rotate(frog_image, 270)
            frog_direction = "UP"
    elif frog_direction == "DOWN":
        if arrow_dir == "RIGHT":
            frog_image = pygame.transform.rotate(frog_image, 90)
            frog_direction = "RIGHT"
        elif arrow_dir == "UP":
            frog_image = pygame.transform.rotate(frog_image, 180)
            frog_direction = "UP"
        elif arrow_dir == "LEFT":
            frog_image = pygame.transform.rotate(frog_image, 270)
            frog_direction = "LEFT"
    elif frog_direction == "RIGHT":
        if arrow_dir == "UP":
            frog_image = pygame.transform.rotate(frog_image, 90)
            frog_direction = "UP"
        elif arrow_dir == "LEFT":
            frog_image = pygame.transform.rotate(frog_image, 180)
            frog_direction = "LEFT"
        elif arrow_dir == "DOWN":
            frog_image = pygame.transform.rotate(frog_image, 270)
            frog_direction = "DOWN"

    print(arrow_dir)
#############################################################################################################
# END OF FROGGER STUFF
#############################################################################################################

#############################################################################################################
# Start of fleet parameters and functions
#############################################################################################################
fleet_count = 4
car_size = (50, 50)
truck_size = (100, 50)
car1_image = pygame.image.load("games\\frogger\\assets\\car1.png").convert_alpha()
car1_image = pygame.transform.scale(car1_image, car_size)
car2_image = pygame.image.load("games\\frogger\\assets\\car2.png").convert_alpha()
car2_image = pygame.transform.scale(car2_image, car_size)


# Vehicles class
class Fleet:
    def __init__(self, image,  size, position, velocity):
        self.image = image
        self.size = size
        self.position = position
        self.velocity = velocity

top_vehicles = []
bottom_vehicles = []
for num in range(fleet_count):
    top_vehicle_random_generator = random.randint(1,2)
    bottom_vehicle_random_generator = random.randint(1,2)
    top_position = [random.randint(0,15)*50, num*50 + 50]
    bottom_position = [random.randint(0,15)*50, num*50 + 300]
    top_velocity = random.randint(-2, 2) * 5
    bottom_velocity = random.randint(-2, 2) * 5
    while top_velocity == 0:
        top_velocity = random.randint(-2, 2) * 5
    while bottom_velocity == 0:
        bottom_velocity = random.randint(-2, 2) * 5

    if top_vehicle_random_generator == 1:
        top_vehicles.append(Fleet(car1_image, car_size, top_position, top_velocity))
        if top_velocity < 0:
            top_vehicles[num].image = pygame.transform.rotate(top_vehicles[num].image, 180)
    elif top_vehicle_random_generator == 2:
        top_vehicles.append(Fleet(car2_image, car_size, top_position, top_velocity))

    if bottom_vehicle_random_generator == 1:
        bottom_vehicles.append(Fleet(car1_image, car_size, bottom_position, bottom_velocity))
    elif bottom_vehicle_random_generator == 2:
        bottom_vehicles.append(Fleet(car2_image, car_size, bottom_position, bottom_velocity))

    if top_velocity < 0:
        top_vehicles[num].image = pygame.transform.rotate(top_vehicles[num].image, 180)
    if bottom_velocity < 0:
        bottom_vehicles[num].image = pygame.transform.rotate(top_vehicles[num].image, 180)


# Function to draw cars
def draw_fleet():
    for i in range(fleet_count):
        display.blit(top_vehicles[i].image, top_vehicles[i].position)
        display.blit(bottom_vehicles[i].image, bottom_vehicles[i].position)

#############################################################################################################
# End of fleet stuff
#############################################################################################################

#############################################################################################################
# Gamestates
#############################################################################################################

game_over_font = pygame.font.Font('freesansbold.ttf', 40)
game_over_check = True #True means game is still running, False means game over


def game_over(score):
    game_over_text = game_over_font.render("Game Over", True, WHITE)
    display.blit(game_over_text, (220,60))
    point_text = point_font.render("Score: " + str(score), True, WHITE)
    display.blit(point_text, (250, 110))

# Checking points
points = 0

point_font = pygame.font.Font('freesansbold.ttf', 40)

def draw_points(score):
    point_text = point_font.render(str(score), True, WHITE)
    display.blit(point_text, (5, 5))

#############################################################################################################
# Drawing loop begins here
#############################################################################################################
running = True

while running:

    clock.tick(FPS)
    display.blit(background_image, (0, 0))

    # Exit loop always required
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check if game is still running before drawing any other shapes
    if game_over_check is True:

        # Logic for frog movement. If frog moves in direction of arrow key, "direction" variable is changed to up left
        # down or right
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT] and frog_jump_ready is True:
            frog_jump_ready = False
            direction = "LEFT"
            direction_check(direction)
        if keys_pressed[pygame.K_RIGHT] and frog_jump_ready is True:
            frog_jump_ready = False
            direction = "RIGHT"
            direction_check(direction)

        if keys_pressed[pygame.K_UP] and frog_jump_ready is True:
            frog_jump_ready = False
            direction = "UP"
            direction_check(direction)

        if keys_pressed[pygame.K_DOWN] and frog_jump_ready is True:
            frog_jump_ready = False
            direction = "DOWN"
            direction_check(direction)

        # Depending on direction variable, frog will move in increments of 50 using velocity of 10 to space out movement.
        if direction == "LEFT" and frog_X > frog_size[0]/2:
            if frog_jump_ticks <= 5:
                frog_X -= frog_velocity
                frog_jump_ticks += 1
            else:
                jump_reset()
        elif direction == "RIGHT" and frog_X < SCREEN_SIZE[0] - frog_size[0]/2:
            if frog_jump_ticks <= 5:
                frog_X += frog_velocity
                frog_jump_ticks += 1
            else:
                jump_reset()
        elif direction == "UP" and frog_Y > 0:
            if frog_jump_ticks <= 5:
                frog_Y -= frog_velocity
                frog_jump_ticks += 1
            else:
                jump_reset()
        elif direction == "DOWN":
            if frog_jump_ticks <= 5 and frog_Y < frog_Y_start:
                frog_Y += frog_velocity
                frog_jump_ticks += 1
            else:
                jump_reset()
        else:
            jump_reset()

        # Check if frog reached the top or bottom
        if frog_Y == 0 and (points % 2 == 0 or points == 0):
            points += 1
        if frog_Y == SCREEN_SIZE[1] - frog_size[0] and points % 2 == 1 and points != 0:
            points += 1
        draw_points(points)

        # Make vehicles move and change directions when hitting walls
        for i in range(fleet_count):
            top_vehicles[i].position[0] += top_vehicles[i].velocity
            if (top_vehicles[i].position[0] <= 0 and top_vehicles[i].velocity < 0) or (top_vehicles[i].position[0] >= SCREEN_SIZE[0]-car_size[0] and top_vehicles[i].velocity > 0):
                top_vehicles[i].velocity *= -1
                top_vehicles[i].image = pygame.transform.rotate(top_vehicles[i].image, 180)
            bottom_vehicles[i].position[0] += bottom_vehicles[i].velocity
            if (bottom_vehicles[i].position[0] <= 0 and bottom_vehicles[i].velocity < 0) or (bottom_vehicles[i].position[0] >= SCREEN_SIZE[0] - car_size[0] and bottom_vehicles[i].velocity > 0):
                bottom_vehicles[i].velocity *= -1
                bottom_vehicles[i].image = pygame.transform.rotate(bottom_vehicles[i].image, 180)

        # Collision checking
        for i in range(fleet_count):
            if abs(frog_Y - bottom_vehicles[i].position[1]) < frog_size[1]:
                if abs(frog_X - bottom_vehicles[i].position[0]) < frog_size[0]:
                    for j in range(fleet_count):
                        bottom_vehicles[j].position[0] = 2000
                        bottom_vehicles[j].velocity = 0
                        top_vehicles[j].position[0] = 2000
                        top_vehicles[j].velocity = 0
                    game_over_check = False
                    frog_dying_sound.play()
                    break
            if abs(frog_Y - top_vehicles[i].position[1]) < frog_size[1]:
                if abs(frog_X - top_vehicles[i].position[0]) < frog_size[0]:
                    for j in range(fleet_count):
                        bottom_vehicles[j].position[0] = 2000
                        bottom_vehicles[j].velocity = 0
                        top_vehicles[j].position[0] = 2000
                        top_vehicles[j].velocity = 0
                    game_over_check = False
                    frog_dying_sound.play()
                    break

        frog(frog_X, frog_Y)
        draw_fleet()

    else:
        game_over(points)
    pygame.display.update()
#############################################################################################################
# End of drawing loop
#############################################################################################################

pygame.quit()
