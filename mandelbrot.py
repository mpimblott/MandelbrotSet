import numpy
import parameters


def test_point(c):
    z = 0
    count = 0
    while count <= parameters.max_iterate_count:
        z = pow(z, 2) + c
        if abs(z) > 2:
            return count
            break
        elif count == parameters.max_iterate_count:
            return count

        count += 1






