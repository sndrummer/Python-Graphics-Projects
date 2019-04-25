import math
import numpy as np


# this is R NEGATIVE!!!!
def rotate_clockwise(xy, s, radians, offsetx=0, offsety=0):
    """Use numpy to build a rotation matrix and take the dot product."""
    x, y = xy
    z = 1
    xy_matrix = np.matrix([[x * s],
                           [y * s],
                           [z]])
    print("xy matrix", xy_matrix)
    c, s = np.cos(radians), np.sin(radians)
    j = np.matrix([[c, s, offsetx],
                   [-s, c, offsety],
                   [0, 0, 1]])
    m = np.dot(j, xy_matrix)

    print("Inverse CORRECT: ", np.linalg.inv(m))
    return m


def rotate_inverse_clockwise(xy, s, radians, offsetx=0, offsety=0):
    """Use numpy to build a rotation matrix and take the dot product."""
    x, y = xy
    z = 1
    xy_matrix = np.matrix([[x],
                           [y],
                           [z]])

    scalar_matrix = np.identity(3) * s
    # print("scalar matrix\n", scalar_matrix)

    inverse_scalar = np.linalg.inv(scalar_matrix)
    # print("inv scalar matrix --> \n", inverse_scalar)

    c, s = np.cos(radians), np.sin(radians)
    j = np.matrix([[c, s, offsetx],
                   [-s, c, offsety],
                   [0, 0, 1]])
    inverse_j = np.linalg.inv(j)
    # print("inverse cos matrix -->\n", inverse_j)
    m = np.dot(inverse_scalar, inverse_j)
    print("m Version:--> \n", m)
    return np.dot(m, xy_matrix)


# This is the default R rotation!!!!
def rotate_counter_clockwise(xy, radians):
    """Use numpy to build a rotation matrix and take the dot product."""
    x, y = xy
    xy_matrix = np.matrix([[x],
                           [y]])
    c, s = np.cos(radians), np.sin(radians)
    j = np.matrix([[c, -s],
                   [s, c]])
    m = np.dot(j, xy_matrix)

    return m


def inverse(matrix):
    return np.linalg.inv(matrix)


def scale(matrix, s):
    """ s is scaling factor"""
    x, y = matrix.shape
    print(matrix.shape)

    print(np.ones(matrix.shape))
    # b = np.ones(x, y)
    # print("ones:", b)
    return np.kron(a, np.ones((x, y)))


def shearing_x(matrix, x_factor):
    return None


def shearing_y(matrix, y_factor):
    return None


def shear3(a, strength=1, shift_axis=0, increase_axis=1):
    if shift_axis > increase_axis:
        shift_axis -= 1
    res = np.empty_like(a)
    index = np.index_exp[:] * increase_axis
    roll = np.roll
    for i in range(0, a.shape[increase_axis]):
        index_i = index + (i,)
        res[index_i] = roll(a[index_i], -i * strength, shift_axis)
    return res


def test_shear():
    a = np.array([[1, 0],
                  [3, 1]])

    b = np.array([[10],
                  [20]])
    return np.dot(a, b)


def compositition_at_index(og_xy, s, radians, indices, rotation="counter"):
    size_x, size_y = og_xy

    scaled = s * np.identity(size_y)
    print("scaled", scaled)

    x, y = indices
    # ind_x, ind_y = out_xy
    # _x, _y = scaled[ind_x][ind_y], scaled[ind_x][ind_y]
    if rotation == "counter":
        return scaled[x][y] * rotate_counter_clockwise(indices)
    else:
        rotate_clockwise(indices)


def sample_problem(xy, s, radians, offsetx=0, offsety=0):
    scalar_matrix = np.matrix([[4, 0, 0],
                               [0, 4, 0],
                               [0, 0, 4]])

    x, y = xy
    z = 1

    xy_matrix = np.matrix([[x, y, z]])

    res = np.dot(xy_matrix, scalar_matrix)
    print(res)
    # print("xy matrix", xy_matrix)
    c, s = np.cos(radians), np.sin(radians)
    j = np.matrix([[c, -s, 0],
                   [s, c, 0],
                   [offsetx, offsety, 1]])
    m = np.dot(res, j)

    return m



# Rotation
# ===============================================
# theta = math.radians(30)
# point = (10, 20)
# print(rotate_counter_clockwise(point, theta))
# print(rotate_clockwise(point, theta))
a = np.array([[1, 2, 1],
              [2, 4, 2],
              [1, 2, 1]])

# print(test_shear())

# TODO YOU NEED TO ADD THE THIRD DIMENSION TO MAKE IT WORK!!!!
og = (1024, 1024)
s = 1 / 4
theta = math.radians(30)  # pi/6 radians
indices = (280, 312)
print(rotate_clockwise(indices, s, theta, 300, 400))

print(sample_problem(indices, s, theta, 300, 400))
