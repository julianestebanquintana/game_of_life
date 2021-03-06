import time
import sys
import pygame
import numpy as np

pygame.init()

# Title
pygame.display.set_caption("Game of Life - By Julian Quintana")

# Creating a dark screen
height, width = 1000, 1000
screen = pygame.display.set_mode((height, width))
background = (25, 25, 25)
screen.fill(background)

# Dividing the screen on cells
cells_x, cells_y = 25, 25
dim_x = width/cells_x
dim_y = height/cells_y

# Matrix for keeping the state of the game. Alive=1, death=0.
game_state = np.zeros((cells_x, cells_y))

# Game execution control
pause_exec = False

# Execution loop
while True:
    # Reinitializing screen and game state in every iteration
    new_game_state = np.copy(game_state)
    screen.fill(background)
    time.sleep(0.1)

    # Registering keyboard and mouse events
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            pause_exec = not pause_exec
        mouse_click = pygame.mouse.get_pressed()
        if sum(mouse_click) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX/dim_x)), int(np.floor(posY/dim_y))
            new_game_state[celX, celY] = not mouse_click[2]

    # Calculating game state
    for y in range(0, cells_x):
        for x in range(0, cells_y):
            if not pause_exec:

                # Calculating close neighbors
                n_neigh = (
                        game_state[(x - 1) % cells_x, (y - 1) % cells_y]
                        + game_state[x % cells_x, (y - 1) % cells_y]
                        + game_state[(x + 1) % cells_x, (y - 1) % cells_y]
                        + game_state[(x - 1) % cells_x, y % cells_y]
                        + game_state[(x + 1) % cells_x, y % cells_y]
                        + game_state[(x - 1) % cells_x, (y + 1) % cells_y]
                        + game_state[x % cells_x, (y + 1) % cells_y]
                        + game_state[(x + 1) % cells_x, (y + 1) % cells_y]
                    )

                # Original Horton's Rules:
                # Rule #1: One death cell with 3 alive neighbors
                # gets back to life
                if game_state[x, y] == 0 and n_neigh == 3:
                    new_game_state[x, y] = 1

                # Rule #2: One cell alive, dies if it has less than 2 alive
                # neighbors (loneliness) or if it has more than 3 alive
                # neighbors (overpopulation)
                elif game_state[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    new_game_state[x, y] = 0

            # Creates the polygon of every drawing cell
            poly = [(x*dim_x, y*dim_y),
                    ((x+1)*dim_x, y*dim_y),
                    ((x+1)*dim_x, (y+1)*dim_y),
                    (x*dim_x, (y+1)*dim_y)]

            # Draws every pair of x and y
            if new_game_state[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)

    # Updating the state of the game
    game_state = np.copy(new_game_state)

    pygame.display.flip()
