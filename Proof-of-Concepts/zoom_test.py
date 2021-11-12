import numpy as np
import mandelbrot as mand
from matplotlib import pyplot as plt
#https://stackoverflow.com/questions/67922408/zooming-in-on-mandelbrot-set


def new_matrix(a_1, b_1):
    M = np.zeros((a_1.shape[0], b_1.shape[0]))
    for i, number1 in enumerate(a_1):
        for j, number2 in enumerate(b_1):
            M[i, j] = mand.test_point((complex(number1,number2)))
    return M


a = np.arange(-2, 2, 0.01)
b = np.arange(-2, 2, 0.01)

M_new = new_matrix(a, b)
plt.imshow(M_new, cmap='gray', extent=(-2, 2, -2, 2))
plt.show()

a_2 = np.arange(0.1, 0.5, 0.01)
b_2 = np.arange(0.1, 0.5, 0.01)

M_new_2 = new_matrix(a_2, b_2)
plt.imshow(M_new_2, cmap='gray', extent=(0.1, 0.5, 0.1, 0.5))
plt.show()