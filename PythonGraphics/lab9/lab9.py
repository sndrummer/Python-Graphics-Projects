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
    # print("Checking point: (", x, " ", y, ")")

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
                result[y][x] = rgb

    return result


#  ***** Excercise 2 *****
# filename = "test.png"
# im = imread(filename)
# h, w, _ = im.shape
# transform = np.matrix([[cos(45 * pi / 180), -sin(45 * pi / 180), w / 2],
#                        [sin(45 * pi / 180), cos(45 * pi / 180), -h / 5],
#                        [0, 0, 1]])
#
# result = backmap1(im, transform)
#
# plt.imshow(result, vmin=0)
# plt.show()


#  ***** Excercise 3 *****
# Part 3: Homographies
# Now that we have the two specific functions that we need,
# let's start looking at some more interesting image warping. In class, we discussed how we can use
# homographies to warp images nonlinearly. In this lab, we have provided the homography generating
# code for you.
# We want to be able to get a new image into the tv set in the image shown below. Note that not all
# pixels will need to be backward mapped. For this reason, we also need to specify a list of points
# that we are considering. This is provided in the getScreen function definined above.
#
# Rewrite your backmap function to allow for two images of different sizes and a specific set of
# points that need to be mapped.

def getHomography(s0, s1, s2, s3, t0, t1, t2, t3):
    x0s = s0.x
    y0s = s0.y
    x0t = t0.x
    y0t = t0.y

    x1s = s1.x
    y1s = s1.y
    x1t = t1.x
    y1t = t1.y

    x2s = s2.x
    y2s = s2.y
    x2t = t2.x
    y2t = t2.y

    x3s = s3.x
    y3s = s3.y
    x3t = t3.x
    y3t = t3.y

    # Solve for the homography matrix
    A = np.matrix([
        [x0s, y0s, 1, 0, 0, 0, -x0t * x0s, -x0t * y0s],
        [0, 0, 0, x0s, y0s, 1, -y0t * x0s, -y0t * y0s],
        [x1s, y1s, 1, 0, 0, 0, -x1t * x1s, -x1t * y1s],
        [0, 0, 0, x1s, y1s, 1, -y1t * x1s, -y1t * y1s],
        [x2s, y2s, 1, 0, 0, 0, -x2t * x2s, -x2t * y2s],
        [0, 0, 0, x2s, y2s, 1, -y2t * x2s, -y2t * y2s],
        [x3s, y3s, 1, 0, 0, 0, -x3t * x3s, -x3t * y3s],
        [0, 0, 0, x3s, y3s, 1, -y3t * x3s, -y3t * y3s]
    ])

    b = np.matrix([
        [x0t],
        [y0t],
        [x1t],
        [y1t],
        [x2t],
        [y2t],
        [x3t],
        [y3t]
    ])

    # The homorgraphy solutions a-h
    solutions = np.linalg.solve(A, b)

    solutions = np.append(solutions, [[1.0]], axis=0)

    # Reshape the homography into the appropriate 3x3 matrix
    homography = np.reshape(solutions, (3, 3))

    return homography


def getScreen():
    result = []
    screen = np.loadtxt("screen.txt")
    for line in screen:
        result.append(Point(int(line[0]), int(line[1])))
    return result


def backmap2(source, target, transform, points):
    h, w, _ = source.shape
    t = np.linalg.inv(transform)
    # backmap only the points
    for point in points:
        new_pt = t * point.get_as_vector()
        transformed_point = Point(new_pt.item(0), new_pt.item(1))
        points = get_close_points(source, transformed_point)
        if points != None:
            rgb = interpolate(points, transformed_point.x, transformed_point.y)
            target[point.y][point.x] = rgb

    return target


filename = "test.png"
im = imread(filename)

h, w, _ = im.shape

s0 = Point(0, 0)
s1 = Point(w - 1, 0)
s2 = Point(w - 1, h - 1)
s3 = Point(0, h - 1)

t0 = Point(245, 152)
t1 = Point(349, 150)
t2 = Point(349, 253)
t3 = Point(246, 261)

tv = imread('tv.jpg')
plt.imshow(tv, vmin=0)
plt.show()

transform = getHomography(s0, s1, s2, s3, t0, t1, t2, t3)

screen = getScreen()

# source is the bird and target is the tv
result = backmap2(im, tv, transform, screen)

plt.imshow(result, vmin=0)
plt.show()
