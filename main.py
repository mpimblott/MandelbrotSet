import pygame
import time
import mandelbrot as mand
import convert
import parameters
from pygame.locals import *


def create_graph():
    print('hi')


def render(r, centre, surface):
    x_pos = 0
    y_pos = 0
    increment = convert.find_pixel_increment(r)
    colour_increment = 225 / parameters.max_iterate_count
    z = complex(centre[0] - r, centre[1] + r)
    while y_pos <= parameters.window_dimension:
        while x_pos <= parameters.window_dimension:
            count = mand.test_point(z)
            pygame.draw.circle(surface, (255 - colour_increment * count, 255 - colour_increment * count, 255 - (12.7 / parameters.max_iterate_count) * count), (x_pos, y_pos), 0)
            z += increment + 0 * 1j
            x_pos += 1
        x_pos = 0
        z = complex(centre[0] - r, z.imag)
        z -= 0 + increment * 1j
        y_pos += 1
        pygame.display.update()


class Main:
    pygame.init()
    display_surface = pygame.display.set_mode((parameters.window_dimension, parameters.window_dimension))
    render(parameters.graph_radius, parameters.window_centre, display_surface)

    while True:
        mouse_pos = convert.pixel_to_argand(pygame.mouse.get_pos())
        print('mouse: ' + str(mouse_pos))
        pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
        if pressed1:
            print('pressed')
            vector = convert.find_translation_vector(mouse_pos,parameters.window_centre)
            convert.translate(vector)
            convert.zoom(3)
            render(parameters.graph_radius, parameters.window_centre, display_surface)

        time.sleep(0.1)
        pygame.event.get()


Main

