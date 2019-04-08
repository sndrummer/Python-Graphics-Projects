from scipy.ndimage import imread
import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import imsave
import math
from math import sin, cos, pi


class Point:
    def __init__(self, x, y, value=0):
        self.x = x
        self.y = y
        self.rgb = value

    def get_as_vector(self):
        return np.array([[self.x],
                         [self.y],
                         [1]])

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'Point({self.x}, {self.y})'


# Your bilinear interpolation function
def interpolate(points, x, y):
    """
    Performs bilinear interpolation

    :param points: list of points to use for the interpolation
    :param x: x val of point you are interpolating
    :param y: y val of point you are interpolating
    :return: value attached with the points
    """
    #print("Checking point: (", x, " ", y, ")")

    point0 = points[0]
    point1 = points[1]
    point2 = points[2]
    point3 = points[3]

    x1, y1, q11 = point0.x, point0.y, point0.rgb
    _x1, y2, q12 = point1.x, point1.y, point1.rgb
    x2, _y1, q21 = point2.x, point2.y, point2.rgb
    _x2, _y2, q22 = point3.x, point3.y, point3.rgb

    if x1 != _x1 or x2 != _x2 or y1 != _y1 or y2 != _y2:
        raise ValueError('points do not form a rectangle')
    if not x1 <= x <= x2 or not y1 <= y <= y2:
        raise ValueError('(x, y) not within the rectangle')

    return (q11 * (x2 - x) * (y2 - y) +
            q21 * (x - x1) * (y2 - y) +
            q12 * (x2 - x) * (y - y1) +
            q22 * (x - x1) * (y - y1)
            ) / ((x2 - x1) * (y2 - y1) + 0.0)


def resize_image(image, height, width):
    new_image = np.zeros((int(height), (int(width)), 3), dtype="uint8")

    # Step 1 get the scalars of the image
    og_height, og_width, _ = image.shape
    scalar_y, scalar_x = round(height / og_height, 2), round(width / og_width, 2)

    for i in range(0, og_height):
        for j in range(0, og_width):
            y = i
            x = j

            if i == og_height - 1:
                y -= 1
            if j == og_width - 1:
                x -= 1

            a = Point(j * scalar_x, i * scalar_y, image[y][x])
            b = Point(j * scalar_x, (i + 1) * scalar_y, image[y + 1][x])
            c = Point((j + 1) * scalar_x, i * scalar_y, image[y, x + 1])
            d = Point((j + 1) * scalar_x, (i + 1) * scalar_y, image[y + 1][x + 1])
            points = [a, b, c, d]

            for k in range(math.ceil(scalar_y * i), math.floor(scalar_y * (i + 1)) + 1):
                for l in range(math.ceil(scalar_x * j), math.floor(scalar_x * (j + 1)) + 1):
                    if k < height and l < width:
                        rgb = interpolate(points, l, k)
                        new_image[k][l] = rgb

    return new_image


# *************************************************************************************************
#  ***** Excercise 1 *****
# filename = "test.png"
# image = imread(filename)
# h, w, _ = image.shape
#
# print("H: ", h, "w: ", w)
# result = np.zeros((int(2.3 * h), (int(2.3 * w)), 3), dtype="uint8")
#
# plt.imshow(result, vmin=0)
# plt.show()
#
# result = resize_image(image, int(2.3 * h), int(2.3 * w))
#
# plt.imshow(result, vmin=0)
# plt.show()

def get_four_corresponding_points(image, transform):
    # get the four corners coordinates
    source_points = []
    destination_pts = []
    h, w, _ = image.shape
    x1 = 0
    x2 = w - 1
    y1 = 0
    y2 = h - 1

    source_points.append(Point(x1, y1))
    source_points.append(Point(x2, y1))
    source_points.append(Point(x1, y2))
    source_points.append(Point(x2, y2))

    for point in source_points:
        transformed_coords = transform * point.get_as_vector()
        print("transformed coords: ", transformed_coords)

    print("h: ", h)
    print("w: ", w)
    return destination_pts


# *************************************************************************************************

# Part 2: Backwards Mapping
# Now that we have a interpolation function, we need a function that performs a backward mapping
# between a source and target image.
# Given a simple rotation transformation, write a function that performs a backwards mapping.
# This function should also call your interpolate function.
#
# For this example, the source and target image will be the same size, which means part of your
# rotated image will be cut off on the corners. You can assume that all pixels need to be backward
# mapped. Also, don't forget to invert the transform. This is really easy in numpy.


def get_close_points(image, point):
    h, w, _ = image.shape
    if point.x < 0 or point.y < 0 or point.x > w - 1 or point.y > h - 1:
        return None

    x = math.floor(point.x)
    y = math.floor(point.y)

    # check edge conditions
    if point.y == h - 1:
        print("lowering y")
        y -= 1
    if point.x == w - 1:
        print("lowering x")
        x -= 1

    a = Point(x, y, image[y][x])
    b = Point(x, (y + 1), image[y + 1][x])
    c = Point((x + 1), y, image[y, x + 1])
    d = Point((x + 1), (y + 1), image[y + 1][x + 1])
    points = [a, b, c, d]

    return points


def backmap1(image, transform):
    h, w, _ = image.shape
    result = np.zeros((h, w, 3), dtype="uint8")

    t = np.linalg.inv(transform)

    for y in range(0, h):
        for x in range(0, w):
            point = Point(x, y)
            new_pt = t * point.get_as_vector()  # Inverse transform on source pixel??
            transformed_point = Point(new_pt.item(0), new_pt.item(1))
            # get points for interpolation
            points = get_close_points(image, transformed_point)
            if points != None:
                rgb = interpolate(points, transformed_point.x, transformed_point.y)
                result[x][y] = rgb

    return result


#  ***** Excercise 2 *****
filename = "test.png"
im = imread(filename)
h, w, _ = im.shape
transform = np.matrix([[cos(45 * pi / 180), -sin(45 * pi / 180), w / 2],
                       [sin(45 * pi / 180), cos(45 * pi / 180), -h / 5],
                       [0, 0, 1]])

result = backmap1(im, transform)

plt.imshow(result, vmin=0)
plt.show()
















#  ***** Excercise 3 *****