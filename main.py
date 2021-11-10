import pygame
import time
import mandelbrot as mand
import convert
import parameters as params
#Initialise
DARK_BLUE = (3,   5,  54)
WHITE = (255, 255, 255)
window_surface = pygame.HWSURFACE|pygame.DOUBLEBUF

pygame.init()
window = pygame.display.set_mode((params.window_dimension, params.window_dimension))
pygame.display.set_caption("Mandelbrot Set")

# Create canvas for drawing
canvas = pygame.Surface((params.window_dimension, params.window_dimension))
canvas.fill(DARK_BLUE)


def render(r, centre): #, surface
    x_pos = 0
    y_pos = 0
    increment = convert.find_pixel_increment(r)
    colour_increment = 225 / params.max_iterate_count
    z = complex(centre[0] - r, centre[1] + r)
    while y_pos <= params.window_dimension:
        while x_pos <= params.window_dimension:
            count = mand.test_point(z)
            pygame.draw.circle(canvas, (255 - colour_increment * count, 255 - colour_increment * count, 255 - (12.7 / params.max_iterate_count) * count), (x_pos, y_pos), 1)
            #pygame.draw.circle(canvas, (255,255,255),(x_pos,y_pos),1)
            z += increment + 0 * 1j
            x_pos += 1
        x_pos = 0
        z = complex(centre[0] - r, z.imag)
        z -= 0 + increment * 1j
        y_pos += 1
    window.blit(canvas, (0, 0))
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
    render(params.graph_radius, params.window_centre) #, display_surface
    # Clamp FPS
    clock.tick_busy_loop(30)
