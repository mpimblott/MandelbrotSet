import pygame
import mandelbrot as mand
import parameters as params
import display as disp
import numpy as np
import time
import random

# Default to the mandlebrot set
current_algorithm = mand.Algorithm.MANDELBROT

# Define start and end complex bounds of the set
start = None
end = None

# zooming
zooming = False
recording = False


# Wrapper to update the matrix and then render
def update_matrix_and_render():
    mand.update_matrix(current_algorithm, start, end)
    disp.render()


# Work out the new complex number range for the plot based on the location
# the user clicked.  Then update the matrix and render
def handle_mouse_click(pos):
    global start, end

    print("Redrawing...", pos)
    start_time = time.time()
    # Calculate the new start and end complex numbers based on the click position
    click_position_as_complex_number = mand.calculate_position_as_complex(start, end, pos[0], pos[1])

    cdiff = end - start

    # Zoom in to a quarter of the view by default
    scale_offset = cdiff * 0.25

    start = click_position_as_complex_number - scale_offset
    end = click_position_as_complex_number + scale_offset

    # Generate the plot and redraw
    update_matrix_and_render()
    end_time = time.time()
    print("Done...", end_time-start_time)
    return start, end


def infinite_zoom(rate, complex_centre=0+1j):
    global start, end
    start_time = time.time()
    cdiff = end - start
    scale_offset = cdiff * rate

    start = complex_centre - scale_offset
    end = complex_centre + scale_offset
    # Generate the plot and redraw
    update_matrix_and_render()
    end_time = time.time()
    print("Done...", end_time-start_time)
    return start, end


# Main game loop - keep looping until the user exits
def main_loop():
    global current_algorithm, zooming

    # Render the original Matrix
    update_matrix_and_render()

    run = True
    while run:
        # Handle Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    print("Changing palette")
                    disp.build_and_set_palette(random.randrange(255))
                elif event.key == pygame.K_b:
                    print("Blue monochrome palette")
                    disp.set_monochrome_palette()
                elif event.key == pygame.K_k:
                    print("Continuous palette")
                    disp.set_continuous_palette()
                elif event.key == pygame.K_r:
                    print("Resetting")
                    reset_coordinates()
                    update_matrix_and_render()
                elif event.key == pygame.K_m:
                    print("Using Mandlebrot set")
                    reset_coordinates()
                    current_algorithm = mand.Algorithm.MANDLEBROT
                    update_matrix_and_render()
                elif event.key == pygame.K_j:
                    print("Using Julia set")
                    reset_coordinates()
                    current_algorithm = mand.Algorithm.JULIA
                    update_matrix_and_render()
                elif event.key == pygame.K_z:
                    zooming = not zooming
                    print("Zooming: " + str(zooming))
                elif event.key == pygame.K_w:
                    zooming = not zooming
                    disp.recording = not recording
                    print("Zooming: " + str(zooming))
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                handle_mouse_click(pos)
        if zooming:
            infinite_zoom(0.5)

        clock.tick(15)


def reset_coordinates():
    global start, end
    start = -2.0 + -1.0j
    end = 1.0 + 1.0j


# Initialisation
clock = pygame.time.Clock()
disp.init_display()
reset_coordinates()

# enter the main loop until I click close
main_loop()