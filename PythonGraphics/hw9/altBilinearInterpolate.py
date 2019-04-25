import math
import numpy as np



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_as_3Dvector(self):
        return np.array([self.x, self.y, 0])

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'Point({self.x}, {self.y})'


def bilinear_interpolate(points, height, pos):

    # st1, st2 opposite, surrounding corners Points
    st1x = math.floor(pos.x - 0.5) + 0.5
    st1y = math.floor(pos.y - 0.5) + 0.5
    st1 = Point(st1x, st1y)

    st2x = st1.x + 1
    st2y = st1.y + 1
    st2 = Point(st2x, st2y)

    # Point t: interpolating factors
    tx = pos.x - st1.x
    ty = pos.y - st1.y
    t = Point(tx, ty)
