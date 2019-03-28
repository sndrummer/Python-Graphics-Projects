import math
import numpy as np


def create_array(x, y, z):
    return np.array([[x, y, z]])


def create_vector(x, y, z):
    return np.array([[x],
                     [y],
                     [z]])


a = np.matrix([[1, 0, 0, 2],
               [0, 1, 0, 3],
               [0, 0, 1, 0],
               [0, 0, 0, 1]])

b = np.matrix([[1, 0, 0, 2],
               [0, 1, 0, 3],
               [0, 0, 5, 0],
               [0, 0, 0, 5]])

c = a * b
print(c)
