# !/usr/bin/env python3
# @file memory_game.py
# SCRP: Memory Game
# Daryl Dang

"""
Memory Game
-----------

"""
####################################################################################################
# IMPORTS
####################################################################################################
import pygame
import random

####################################################################################################
# GLOBALS/CONSTANTS
####################################################################################################
# Screen
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
FPS = 60

# Colours
WHITE = (255, 255, 255)
FOREST_GREEN = (34, 139, 34)

# Icons
OPTION_ICON_SIZE = (100, 100)
ICON1_POS = (50,  150)
ICON2_POS = (250, 150)
ICON3_POS = (450, 150)

# Player
DEF_SIZE = (250, 300)
YOU_LABEL_POS = (100, 400)
CPU_LABEL_POS = (600, 400)
YOU_CHOICE_POS = (100, 450)
CPU_CHOICE_POS = (600, 450)

# Message
MESSAGE_POS = (50, 50)
OUTCOME_POS = (50, 300)

####################################################################################################
# SETUP
####################################################################################################
# Initialize pygame and display window
pygame.init()
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Memory Game")
clock = pygame.time.Clock()

# Load images
rock_icon_img = pygame.image.load("games\\rps\\assets\\rock.png").convert_alpha()
rock_icon_img = pygame.transform.scale(rock_icon_img, OPTION_ICON_SIZE)
paper_icon_img = pygame.image.load("games\\rps\\assets\\paper.png").convert_alpha()
paper_icon_img = pygame.transform.scale(paper_icon_img, OPTION_ICON_SIZE)
scissors_icon_img = pygame.image.load("games\\rps\\assets\\scissors.png").convert_alpha()
scissors_icon_img = pygame.transform.scale(scissors_icon_img, OPTION_ICON_SIZE)

rock_img = pygame.image.load("games\\rps\\assets\\rock.png").convert_alpha()
rock_img = pygame.transform.scale(rock_icon_img, DEF_SIZE)
paper_img = pygame.image.load("games\\rps\\assets\\paper.png").convert_alpha()
paper_img = pygame.transform.scale(paper_icon_img, DEF_SIZE)
scissors_img = pygame.image.load("games\\rps\\assets\\scissors.png").convert_alpha()
scissors_img = pygame.transform.scale(scissors_icon_img, DEF_SIZE)
q_mark_img = pygame.image.load("games\\rps\\assets\\questionmark.jpg").convert_alpha()
q_mark_img = pygame.transform.scale(q_mark_img, DEF_SIZE)

# Load font
font = pygame.font.Font('freesansbold.ttf', 32)

# Game variables
you_choice = 0
cpu_choice = 0

# Load options to start (fixes bug)
rock_icon = display.blit(rock_icon_img, ICON1_POS)
paper_icon = display.blit(paper_icon_img, ICON2_POS)
scissor_icon = display.blit(scissors_icon_img, ICON3_POS)

####################################################################################################
# FUNCTIONS
####################################################################################################
def write_main_message(message, colour):
    # Render font
    text = font.render(message, True, colour)

    # Add text using blit
    display.blit(text, MESSAGE_POS)

def write_player_labels():
    # You
    you_label = font.render("You", True, WHITE)
    display.blit(you_label, YOU_LABEL_POS)

    # CPU
    cpu_label = font.render("CPU", True, WHITE)
    display.blit(cpu_label, CPU_LABEL_POS)

def draw_player_choices(choice, player_pos):
    if choice == 1:
        display.blit(rock_img, player_pos)
    elif choice == 2:
        display.blit(paper_img, player_pos)
    elif choice == 3:
        display.blit(scissors_img, player_pos)
    else:
        display.blit(q_mark_img, player_pos)

def generate_cpu_choice():
    return round(random.uniform(0.5, 3.49)) # this creates an equal distribution of choices

def decide_outcome_message(you, cpu):
    if you == 0 and cpu == 0:
        return ""
    elif you == cpu:
        # Tied
        return "You tied!"
    elif you == 1 and cpu == 2:
        # Rock and paper
        return "You lose!"
    elif you == 1 and cpu == 3:
        # Rock and scissors
        return "You win!"
    elif you == 2 and cpu == 1:
        # Paper and rock
        return "You win!"
    elif you == 2 and cpu == 3:
        # Paper and scissors
        return "You lose!"
    elif you == 3 and cpu == 1:
        # Scissors and rock
        return "You lose!"
    elif you == 3 and cpu == 2:
        # Scissors and paper
        return "You win!"

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

        # Check RPS you choice
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if rock_icon.collidepoint(mouse_pos):
                you_choice = 1
                # Generate cpu choice
                cpu_choice = generate_cpu_choice()
            elif paper_icon.collidepoint(mouse_pos):
                you_choice = 2
                # Generate cpu choice
                cpu_choice = generate_cpu_choice()
            elif scissor_icon.collidepoint(mouse_pos):
                you_choice = 3
                # Generate cpu choice
                cpu_choice = generate_cpu_choice()

    # Display background
    display.fill(FOREST_GREEN)

    # Write message at the top
    write_main_message("Choose your option!", WHITE)

    # Load option icons
    rock_icon = display.blit(rock_icon_img, ICON1_POS)
    paper_icon = display.blit(paper_icon_img, ICON2_POS)
    scissor_icon = display.blit(scissors_icon_img, ICON3_POS)

    # Draw player choices
    write_player_labels()
    draw_player_choices(you_choice, YOU_CHOICE_POS)
    draw_player_choices(cpu_choice, CPU_CHOICE_POS)

    # Get mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Write outcome message
    outcome_message = font.render(decide_outcome_message(you_choice, cpu_choice), True, WHITE)
    display.blit(outcome_message, OUTCOME_POS)

    # Update the pygame window and set clock tick
    pygame.display.update()
    clock.tick(FPS)

# Close and clean up
pygame.quit()
