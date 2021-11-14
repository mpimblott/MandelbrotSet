import numpy as np
import parameters as params
from enum import Enum


class Algorithm(Enum):
    MANDELBROT = 1
    JULIA = 2

# generate a matrix representing the screen
matrix = np.zeros((params.window_dimension, params.window_dimension))


# Run through all the points in the matrix representing the screen and update
# the colour to display.
def update_matrix(algorithm, start_coord, end_coord):
    width = params.window_dimension
    height = params.window_dimension

    for x in range(0, width):
        for y in range(0, height):

            # Convert pixel coordinate to complex number
            c = calculate_position_as_complex(start_coord, end_coord, x, y)

            # Compute the number of iterations
            if algorithm == Algorithm.MANDELBROT:
                m = mandelbrot_test_point(c)
            elif algorithm == Algorithm.JULIA:
                m = julia_set_test_point(c)

            # The color depends on the number of iterations
            colour = (255 - int(m * 255 / params.max_iterate_count) ) * m

            # Plot the point
            matrix[x, y] = colour
    return


# Calculate an x,y position in the range of the complex number
def calculate_position_as_complex(start_complex, end_complex, x, y):
    cdiff = end_complex - start_complex
    width_ratio = x / params.window_dimension
    height_ratio = y / params.window_dimension

    c = complex(start_complex.real + (width_ratio * cdiff.real),
                start_complex.imag + (height_ratio * cdiff.imag))
    return c


# Test the provided complex number and return a threshold value that can be
# used to return a colour
def mandelbrot_test_point(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < params.max_iterate_count:
        z = z * z + c
        n += 1
    return n


def julia_set_test_point(z):
    nit = 0
    zabs_max = 10
    c = complex(-0.1, 0.65)

    # Do the iterations
    while abs(z) <= zabs_max and nit < params.max_iterate_count:
        z = z ** 2 + c
        nit += 1
    # shade = 1 - np.sqrt(nit / params.max_iterate_count)
    ratio = nit / params.max_iterate_count
    return ratio






