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
    for y in range(0, cells_x):
        for x in range(0, cells_y):

            # Calculating close neighbors
            n_neigh = (
                    gameState[(x - 1) % cells_x, (y - 1) % cells_y]
                    + gameState[x % cells_x, (y - 1) % cells_y]
                    + gameState[(x + 1) % cells_x, (y - 1) % cells_y]
                    + gameState[(x - 1) % cells_x, y % cells_y]
                    + gameState[(x + 1) % cells_x, y % cells_y]
                    + gameState[(x - 1) % cells_x, (y + 1) % cells_y]
                    + gameState[x % cells_x, (y + 1) % cells_y]
                    + gameState[(x + 1) % cells_x, (y + 1) % cells_y]

            # Creates the polygon of every drawing cell
            poly = [(x*dim_x, y*dim_y),
                    ((x+1)*dim_x, y*dim_y),
                    ((x+1)*dim_x, (y+1)*dim_y),
                    (x*dim_x, (y+1)*dim_y)]

            pygame.draw.polygon(screen, (128, 128, 128), poly, 1)

    pygame.display.flip()
