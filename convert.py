import parameters


def pixel_to_argand(point):
    x = point[0] * find_pixel_increment(parameters.graph_radius) - 2 + parameters.window_centre[0]
    y = (point[1] * find_pixel_increment(parameters.graph_radius) - 2) * -1 + parameters.window_centre[1]
    return x, y


def argand_to_pixel(point):
    print('hi')


def find_pixel_increment(r):
    increment = r / (parameters.window_dimension / 2)
    return increment


def translate(vector):
    x_centre = parameters.window_centre[0] + vector[0]
    y_centre = parameters.window_centre[1] + vector[1]
    parameters.window_centre = x_centre, y_centre


def find_translation_vector(end_point, start_point):
    x_difference = end_point[0] - start_point[0]
    y_difference = end_point[1] - start_point[1]
    return x_difference, y_difference


def zoom(scale):
    parameters.graph_radius = parameters.graph_radius * (1 / scale)
    #x_centre = parameters.window_centre[0] / 4
    #y_centre = parameters.window_centre[1] / 4
    #parameters.window_centre = x_centre, y_centre
