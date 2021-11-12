import numpy as np
import pygame
import time
import mandelbrot as mand
import convert
import parameters as params
import random
#Initialise
DARK_BLUE = (3, 5, 54)
WHITE = (255, 255, 255)
increment = 0
window_surface = pygame.HWSURFACE|pygame.DOUBLEBUF

pygame.init()
window = pygame.display.set_mode((params.window_dimension, params.window_dimension))
pygame.display.set_caption("Mandelbrot Set")

# Create canvas for drawing
canvas = pygame.Surface((params.window_dimension, params.window_dimension))
canvas.fill(DARK_BLUE)
dim = params.window_dimension
pixel_array = np.zeros(dim * dim * 3).reshape([dim, dim, 3]) + 200


def create_pixel_array():
    while y_pos < params.window_dimension:
        while x_pos < params.window_dimension:
            print(pixel_array[x_pos][y_pos])
            x_pos += 1


def render(pixel_array, increment, r, centre):
    y_pos = 0
    x_pos = 0
    while y_pos < params.window_dimension:
        while x_pos < params.window_dimension:
            pixel_array[x_pos][y_pos] = (x_pos,y_pos,increment)
            x_pos += 1
        x_pos = 0
        y_pos += 1
    pygame.surfarray.blit_array(window, pixel_array)
    pygame.display.flip()


# Initialisation
clock = pygame.time.Clock()
run = True
while run:
    # Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # update window and draw
    if increment < 240:
        increment += 10
    else:
        increment = 0
    render(pixel_array, increment, params.graph_radius, params.window_centre) #, display_surface
    # Clamp FPS
    clock.tick_busy_loop(30)
