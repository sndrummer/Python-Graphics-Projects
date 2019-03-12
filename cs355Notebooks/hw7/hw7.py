import math
import numpy as np

# 4d matrix for 3d
identity = np.matrix([[1, 0, 0, 0],
                      [0, 1, 0, 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1]])


def create_vector(x, y, z):
    return np.array([[x],
                     [y],
                     [z],
                     [1]])


def get_translation_matrix(x, y, z):
    return np.matrix([[1, 0, 0, x],
                      [0, 1, 0, y],
                      [0, 0, 1, z],
                      [0, 0, 0, 1]])


def get_scale_matrix(x_scalar, y_scalar, z_scalar):
    return np.matrix([[x_scalar, 0, 0, 0],
                      [0, y_scalar, 0, 0],
                      [0, 0, z_scalar, 0],
                      [0, 0, 0, 1]])


def get_yrot_matrix(degrees_rotation):
    radians = math.radians(degrees_rotation)
    c, s = np.cos(radians), np.sin(radians)
    return np.matrix([[c, 0, s, 0],
                      [0, 1, 0, 0],
                      [-s, 0, c, 0],
                      [0, 0, 0, 1]])


def get_clip_space_matrix(fov_degrees, aspect, f, n):
    radians = math.radians(fov_degrees)

    zoom = 1 / math.tan(radians / 2)
    y_zoom = zoom
    x_zoom = y_zoom / aspect
    a = (f + n) / (f - n)
    b = (-2 * n * f) / (f - n)

    return np.matrix([[x_zoom, 0, 0, 0],
                      [0, y_zoom, 0, 0],
                      [0, 0, a, b],
                      [0, 0, 1, 0]])


def get_screen_space(width, height):
    w = width / 2
    h = height / 2
    return np.matrix([[w, 0, w],
                      [0, -h, h],
                      [0, 0, 1]])


# problem 1
# 1. Expand the vector into the 4th dimension by adding a 1 as the w component:
vertex = create_vector(10, 15, 0)
# 2. Multiply the transformation matrix by the 4 dimensional vector above. The result will be another 4 dimensional vector:
# T * R * S * Vector = RESULT
# T
T = get_translation_matrix(30, 0, 40)
# R
R = get_yrot_matrix(45)
# S
S = identity

transformationMatrix = T * R * S

print(transformationMatrix)

t = transformationMatrix * vertex

print(t)
# y-axis rotation

# a = np.array([[25],
#               [40],
#               [25]])
#
# b = np.array([[25],
#               [20],
#               [5]])
#
# c = a - b
#
# print(c)


# Problem 2
print("Problem 2 part c")

print(1 / math.sqrt(2))

v = 1 / math.sqrt(2)
a = np.matrix([[-1, 0, 0, 0],
               [0, v, -v, 0],
               [0, v, v, 0],
               [0, 0, 0, 1]])

b = np.matrix([[1, 0, 0, -25],
               [0, 1, 0, -20],
               [0, 0, 1, -5],
               [0, 0, 0, 1]])

c = np.array([[5],
              [6],
              [7],
              [1]])

result = a * b * c
print("result: \n", result)
print("------------------------------------\n\n")

# ------------------------------------------------------
# Problem 3
print("Problem 2 part b")
R = get_yrot_matrix(30)
T = get_translation_matrix(-20, -5, 40)
point = np.array([[5],
                  [6],
                  [7],
                  [1]])

result3 = R * T * point

print(result3)
print("------------------------------------\n\n")
# ------------------------------------------------------
# Problem 3
print("Problem 4 part b THIS ONE !!!!!!!!!!!!!!!")
clip = get_clip_space_matrix(60, (16 / 9), 1000, 10)
print(clip)
point2 = np.array([[5],
                   [-5],
                   [50],
                   [1]])

print("HERE IS THE ANSWER")
result4 = clip * point2
print(result4)

print("Problem 4 part d")

canonical = result4 / 50
print(canonical)
print("!!!!!!!!!!!!!!!-----------------------------------")
# ------------------------------------------------------
print("Problem 4 part e")
screen = get_screen_space(1920, 1080)
print("Screen: \n", screen)

point3 = np.array([[canonical.item(0)],
                   [canonical.item(1)],
                   [1.0]])
print("point3: ", point3)
result5 = screen * point3

print("POINT Coordinate on screen: \n", result5)

x = np.array([[20],
              [20],
              [20]])


point4 = np.array([[0.99],
                   [0.99],
                   [1.0]])

result6 = screen * point4
print(result6)
