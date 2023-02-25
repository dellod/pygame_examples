# !/usr/bin/env python3
# @file snake.py
# SCRP: Snake Game
# Daryl Dang

####################################################################################################
# Snake
# Classic snake game where the objective is to get as many points as possible. Leaving the screen or
# consuming any part of the snake's tail will result in a loss and the player will have to restart.
####################################################################################################

# IMPORTS
import pygame
import random
import sys

### GLOBALS
# Clock
CLOCK_TICK_SPEED = 10

# Screen size
SCREEN_WIDTH    = 800
SCREEN_HEIGHT   = 800

# Colours
GREEN   = (0, 255, 0)
RED     = (255, 0, 0)
WHITE   = (255, 255, 255)
BLACK   = (0, 0, 0)

# Positions and sizes
SNAKE_SIZE      = (40, 40)
MOVEMENT_SIZE   = 40
NO_MOVEMENT     = 0
X_POS           = SCREEN_WIDTH / 2
Y_POS           = SCREEN_HEIGHT / 2
X_UPDATE        = 0
Y_UPDATE        = 0

### FUNCTIONS
def reset_position() -> None:
    """Resets the position of the snake and makes it so that it doesn't move."""
    global X_POS, Y_POS, X_UPDATE, Y_UPDATE
    X_POS = SCREEN_WIDTH / 2
    Y_POS = SCREEN_HEIGHT / 2
    X_UPDATE = 0
    Y_UPDATE = 0


def create_message(message: str,
                   colour: tuple,
                   x_pos: float,
                   y_pos: float,
                   display: pygame.Surface,
                   font_style: pygame.font.Font) -> None:
    """Writes message to display window given the colour and position."""
    msg = font_style.render(message, True, colour)
    display.blit(msg, [x_pos, y_pos])


def generate_random_food_position() -> tuple:
    """Generates random food position on the screen."""
    food_pos = \
        (round(random.randrange(0, SCREEN_WIDTH - SNAKE_SIZE[0]) / SNAKE_SIZE[0]) * SNAKE_SIZE[0],
         round(random.randrange(0, SCREEN_HEIGHT - SNAKE_SIZE[1]) / SNAKE_SIZE[1]) * SNAKE_SIZE[1])
    return food_pos


def check_grid_collision(snake_pos: tuple, food_pos: tuple):
    """Check if the snake has made collision with the position of a food."""
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        return True
    else:
        return False


def main() -> None:
    """Main entry point for program"""
    # Declare globals that will be used in function
    global X_POS, Y_POS, X_UPDATE, Y_UPDATE

    # Declare clock
    clock = pygame.time.Clock()

    # Initialize pygame window
    pygame.init()
    display = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT))  # set the screen size
    pygame.display.update()
    pygame.display.set_caption("Snake Game")

    # Set up font style
    font_style = pygame.font.SysFont(None, 50)

    # Snake information
    snake_pos_list = []
    snake_length = 1

    # Food variables
    food_pos = generate_random_food_position()

    # Important info variables
    score = 0

    # Important flag variables for checking states
    is_game_over = False
    did_player_lose = False

    # Game loop - loop until the user quits the game
    while not is_game_over:
        # 1. Detect Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Quit when the user presses the X at the top right
                is_game_over = True
            elif event.type == pygame.KEYDOWN:
                # User has pressed the key, now check which key has been pressed
                if event.key == pygame.K_LEFT:
                    # Move snake to the left
                    X_UPDATE = -MOVEMENT_SIZE
                    Y_UPDATE = NO_MOVEMENT
                if event.key == pygame.K_RIGHT:
                    # Move snake to the right
                    X_UPDATE = MOVEMENT_SIZE
                    Y_UPDATE = NO_MOVEMENT
                if event.key == pygame.K_UP:
                    # Move snake to the up
                    X_UPDATE = NO_MOVEMENT
                    Y_UPDATE = -MOVEMENT_SIZE
                if event.key == pygame.K_DOWN:
                    # Move snake to the down
                    X_UPDATE = NO_MOVEMENT
                    Y_UPDATE = MOVEMENT_SIZE
                if did_player_lose and event.key == pygame.K_c:
                    # Reset the game
                    reset_position()
                    snake_pos_list = []
                    snake_length = 1
                    did_player_lose = False
                    score = 0

        # 2. Check conditions
        if X_POS > SCREEN_WIDTH or X_POS < 0 or Y_POS > SCREEN_HEIGHT or Y_POS < 0:
            did_player_lose = True

        # 3. Update Display
        # Draw background
        display.fill(BLACK)

        # Draw scoreboard
        score_message = "Score: " + str(score)
        create_message(score_message, WHITE, 10, 10, display, font_style)

        # Draw snake
        for snake_block in snake_pos_list:
            pygame.draw.rect(display, GREEN, [snake_block[0], snake_block[1], SNAKE_SIZE[0], SNAKE_SIZE[1]])

        # Draw food
        pygame.draw.rect(display, RED, [food_pos[0], food_pos[1], SNAKE_SIZE[0], SNAKE_SIZE[1]])

        # Check if snake is on top of food
        if check_grid_collision((X_POS, Y_POS), food_pos):
            score += 1 # Get a point
            snake_length += 1 # Increase length
            food_pos = generate_random_food_position() # Generate new food position

        # Increase length of snake
        curr_snake_head = [X_POS, Y_POS]
        snake_pos_list.append(curr_snake_head)
        if len(snake_pos_list) > snake_length:
            del snake_pos_list[0]

        # Check if snake has eaten its own body
        for snake_block in snake_pos_list[:-1]:
            if snake_block == curr_snake_head:
                did_player_lose = True

        # Check if player lost
        if did_player_lose:
            create_message("You lost!",
                           RED,
                           SCREEN_WIDTH/2 - 80,
                           SCREEN_HEIGHT/2,
                           display, font_style)
            create_message("Press 'C' if you would like to play again.",
                           RED,
                           SCREEN_WIDTH/8,
                           SCREEN_HEIGHT/2 + 40,
                           display, font_style)
        else:
            X_POS += X_UPDATE
            Y_POS += Y_UPDATE
        pygame.display.update()
        clock.tick(CLOCK_TICK_SPEED)

    # Close and clean up
    pygame.quit()
    quit()


# ENTRY POINT
if __name__ == "__main__":
    sys.exit(main())
