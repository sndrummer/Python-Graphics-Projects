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


class SquareNeighbors:
    def __init__(self, start_x, start_y):
        self.coord1 = [start_x, start_y, 3]
        self.coord2 = [start_x, start_y + 1, 4]
        self.coord3 = [start_x + 1, start_y, 6]
        self.coord4 = [start_x + 1, start_y + 1, 8]


def get_min_bounding_box(four_corners):
    x_min = math.inf
    x_max = -1
    y_min = math.inf
    y_max = -1

    for point in four_corners:
        if point.x < x_min:
            x_min = point.x
        if point.y < y_min:
            y_min = point.y
        if point.x > x_max:
            x_max = point.x
        if point.y > y_max:
            y_max = point.y

    point1 = Point(x_min, y_min)
    print("Point1: ", point1)
    point2 = Point(x_min, y_max)
    point3 = Point(x_max, y_min)
    point4 = Point(x_max, y_max)

    return point1, point2, point3, point4


def interpolate_helper(point, diff, coord1, coord2):
    val1 = coord1[2]
    val2 = coord2[2]
    inter_coord = [coord1[0], point.y, 0]
    new_val = round(val1 + diff * (val2 - val1), 3)
    print("new: ", new_val)
    inter_coord[2] = new_val
    print("MAYBE: ?? ", inter_coord)
    return inter_coord


def bilinear_interpolate(point, neighbors):
    # step 1, interpolate the first two coordinates with same x value
    y = point.y
    x = point.x
    diff = round(y - neighbors.coord1[1], 2)
    inter_coord1 = interpolate_helper(point, diff, neighbors.coord1, neighbors.coord2)
    # step 2, interpolate the next two coordinates with the same x-value
    inter_coord2 = interpolate_helper(point, diff, neighbors.coord3, neighbors.coord4)

    diff = round(x - neighbors.coord1[0], 2)

    inter_coord3 = interpolate_helper(point, diff, inter_coord1, inter_coord2)
    return inter_coord3[2]


def is_in_qauadrilateral(point, q1, q2, q3, q4):
    """ You must list the qs clockwise!!"""
    p = point.get_as_3Dvector()
    v1 = q1.get_as_3Dvector()
    v2 = q2.get_as_3Dvector()
    v3 = q3.get_as_3Dvector()
    v4 = q4.get_as_3Dvector()

    print("v2 - v1: ", v2 - v1)
    print("p - v1: ", p - v1)
    result1 = np.cross((v2 - v1), (p - v1))
    result2 = np.cross((v3 - v2), (p - v2))
    result3 = np.cross((v4 - v3), (p - v3))
    result4 = np.cross((v1 - v4), (p - v4))

    print("Result1: ", result1)
    print("Result2: ", result2)
    print("Result3: ", result3)
    print("Result4: ", result4)


# Answer to number 1:
neighbors = SquareNeighbors(10.0, 18.0)
point = Point(10.7, 18.2)
bilinear_interpolate(point, neighbors)

# Answer to number 2: min max the coordinates
quad_corners = [Point(14, 20), Point(15, 11), Point(20, 13), Point(18, 23)]

print("Min Bounding Box: ", get_min_bounding_box(quad_corners))
# Answer to 3 Show computationally whether the point p = (17, 16) is in the above quadrilateral.
print("----------------------------------------------")
point = Point(17, 16)
q1 = Point(14, 20)
q2 = Point(15, 11)
q3 = Point(20, 13)
q4 = Point(18, 23)

is_in_qauadrilateral(point, q1, q2, q3, q4)
