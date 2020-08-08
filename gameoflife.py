import pygame
import numpy as np

pygame.init()


# Creating a dark screen
height, width = 1000, 1000
screen = pygame.display.set_mode((height, width))
background = (25, 25, 25)
screen.fill(background)

# Dividing the screen on cells
cells_x, cells_y = 25, 25
dim_x = width/cells_x
dim_y = height/cells_y

# Execution loop
while True:
    for y in range(0, cells_x):
        for x in range(0, cells_y):
            poly = [(x*dim_x, y*dim_y),
                    ((x+1)*dim_x, y*dim_y),
                    ((x+1)*dim_x, (y+1)*dim_y),
                    (x*dim_x, (y+1)*dim_y)
                    ]
            pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
    pygame.display.flip()
