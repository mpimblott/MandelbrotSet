import pygame
import time
import mandelbrot as mand
import convert
import parameters as params
import numpy as np
from matplotlib import pyplot as plt

#Initialise
DARK_BLUE = (3,   5,  54)
WHITE = (255, 255, 255)
colour_increment = 225 / params.max_iterate_count
window_surface = pygame.HWSURFACE|pygame.DOUBLEBUF

pygame.init()
window = pygame.display.set_mode((params.window_dimension, params.window_dimension))
pygame.display.set_caption("Mandelbrot Set")
# Create canvas for drawing
canvas = pygame.Surface((params.window_dimension, params.window_dimension))


def gen_matrix(real_axis, imaginary_axis):
    M = np.zeros((real_axis.shape[0], imaginary_axis.shape[0]))
    for i, number1 in enumerate(real_axis):
        for j, number2 in enumerate(imaginary_axis):
            M[i, j] = colour_increment * mand.test_point((complex(number1, number2)))
    return M


def render(matrix):
    pygame.surfarray.blit_array(window, matrix)
    pygame.display.flip()


# Initialisation
clock = pygame.time.Clock()
run = True
z = 0
while True:
    zoom_centre = (0, 1) # (real, imag)
    zoom_radius = params.graph_radius-z
    # Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    real_view_line = np.linspace(zoom_centre[0] - zoom_radius, zoom_centre[0] + zoom_radius, params.window_dimension)
    imaginary_view_line = np.linspace(zoom_centre[1] - zoom_radius, zoom_centre[1] + zoom_radius, params.window_dimension)
    M_new = gen_matrix(real_view_line, imaginary_view_line)
    # update window and draw
    render(M_new) #, display_surface
    # Clamp FPS
    z += 0.1
    clock.tick_busy_loop(60)
