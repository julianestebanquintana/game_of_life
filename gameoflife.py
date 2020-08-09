import time
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

# Execution loop
while True:

    new_game_state = np.copy(game_state)

    for y in range(0, cells_x):
        for x in range(0, cells_y):

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

            # Rule #1: One death cell with 3 alive neighbors, gets back to life
            if game_state[x, y] == 0 and n_neigh == 3:
                new_game_state[x, y] = 1

            # Rule #2: One cell alive, dies if it has less than 2 alive
            # neighbors (loneliness) or if it has more than 3 alive neighbors
            # (overpopulation)
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
                pygame.draw.polygon(screen, (256, 256, 256), poly, 0)

    # Updating the state of the game
    game_state = np.copy(new_game_state)

    pygame.display.flip()
