import pygame
import time
import mandelbrot as mand
import parameters as params

window_surface = pygame.HWSURFACE | pygame.HWPALETTE

window = None
drawing_surface = None
recording = False
step = 0
n = 0


def init_display():
    global window
    global drawing_surface

    # all the initialisation code that used to be in main
    pygame.init()
    window = pygame.display.set_mode((params.window_dimension, params.window_dimension), window_surface)
    pygame.display.set_caption("Mandelbrot Set")

    # Create canvas for drawing
    drawing_surface = pygame.Surface((params.window_dimension, params.window_dimension), depth=8)


# The routine was reused from code by Pete Shinners
def build_palette(step):
    # "build a palette. that is a list with 256 RGB triplets"
    loop = range(256)

    # first we create a 256-element array. it goes from 0, to 255, and back to 0
    ramp = [abs((x+step*3) % 511-255) for x in loop]

    # using the previous ramp and some other crude math, we make some different
    # values for each R, G, and B color planes
    return [(ramp[x], ramp[(x+32) % 256], (x+step) % 256) for x in loop]


def build_fancy_palette(step):
    # "build a palette. that is a list with 256 RGB triplets"
    loop = range(256)

    # first we create a 256-element array. it goes from 0, to 255, and back to 0
    ramp = [abs((x+step*3) % 511-255) for x in loop]

    # using the previous ramp and some other crude math, we make some different
    # values for each R, G, and B color planes
    return [(ramp[x], ramp[(x+32) % 256], (x+step) % 256) for x in loop]


# Utility function to set a new palette and redraw
def build_and_set_palette(value):
    palette = build_palette(value)
    drawing_surface.set_palette(palette)
    render()


# Set a blue monochrome traditional palette
def set_monochrome_palette():
    palette = [(0, 0, x) for x in range(256)]
    drawing_surface.set_palette(palette)
    render()


# continuously coloured palette
def set_continuous_palette():
    palette = [(0, 0, x) for x in range(256)]
    drawing_surface.set_palette(palette)
    render()


# We are taking advantage of the 8 bit depth of the surface
# this gives us colour from a single integer via the allocated colour palette
# Copy the matrix to the surface then draw the surface to the display screen
def render():
    global window
    global drawing_surface
    global n
    pygame.surfarray.blit_array(drawing_surface, mand.matrix)
    window.blit(drawing_surface, (0, 0))
    if recording:
        pygame.image.save(window, "screenshot" + str(n) + ".jpg")
        n+=1
        time.sleep(10)
    pygame.display.flip()

