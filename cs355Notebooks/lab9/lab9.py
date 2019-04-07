from scipy.ndimage import imread
import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import imsave
import cv2
import math


class Point:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.rgb = value

    def get_as_3Dvector(self):
        return np.array([self.x, self.y, 0])

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'Point({self.x}, {self.y})'


# Your bilinear interpolation function
def interpolate(points, x, y):
    print("Interpolating x: ", x, " and y: ", y)
    point0 = points[0]
    point1 = points[1]
    point2 = points[2]
    point3 = points[3]

    print("point0: ", point0)
    print("point1: ", point1)
    print("point2: ", point2)
    print("point3: ", point3)

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


def interpolate_helper(point, diff, coord1, coord2):
    print("DIFF is: ", diff)
    val1 = coord1.rgb
    # print("VAL1: :", val1)
    val2 = coord2.rgb
    # print("VAL2: :", val2)
    # Get new RGB
    new_val = round(val1 + diff * (val2 - val1), 3)
    inter_coord = Point(coord1.x, point.y, new_val)
    return inter_coord


def bilinear_interpolate(point, quad):
    # step 1, interpolate the first two coordinates with same x value
    y = point.y
    x = point.x
    diff = round(y - quad[0].y, 2)  # neighbors.coord1[1]
    inter_coord1 = interpolate_helper(point, diff, quad[0],
                                      quad[1])  # coord are points coord[2] are values!!!!
    # step 2, interpolate the next two coordinates with the same x-value
    inter_coord2 = interpolate_helper(point, diff, quad[2], quad[3])
    diff = round(x - quad[0].x, 2)
    inter_coord3 = interpolate_helper(point, diff, inter_coord1, inter_coord2)
    return inter_coord3.rgb


def resize_image(image, height, width):
    new_image = np.zeros((int(height), (int(width)), 3), dtype="uint8")

    # Step 1 get the scalars of the image
    og_height, og_width, _ = image.shape
    scalar_y, scalar_x = round(height / og_height, 2), round(width / og_width, 2)

    # print("Scalar_y ", scalar_y)
    # print("Scalar_x ", scalar_x)

    # Step 1 get the 4 points of attack
    for i in range(0, og_height - 1):
        for j in range(0, og_width - 1):
            a = Point(j * scalar_x, i * scalar_y, image[i][j])
            b = Point(j * scalar_x, (i + 1) * scalar_y, image[i + 1][j])
            c = Point((j + 1) * scalar_x, i * scalar_y, image[i, j + 1])
            d = Point((j + 1) * scalar_x, (i + 1) * scalar_y, image[i + 1][j + 1])
            points = [a, b, c, d]

            print("Checking from x: ", int(scalar_x * j), " to ", int(scalar_x * (j + 1)))
            print("Checking from y: ", int(scalar_y * i), " to ", int(scalar_y * (i + 1)))
            math.floor(scalar_y * i)
            math.floor(scalar_y * (i + 1))
            math.floor(scalar_x * j)
            for k in range(math.ceil(scalar_y * i), math.floor(scalar_y * (i + 1))):
                for l in range(math.ceil(scalar_x * j), math.floor(scalar_x * (j + 1))):
                    rgb = interpolate(points, l, k)
                    new_image[k][l] = rgb
                    print("Added : ", rgb)

    return new_image


def example_solution(image):
    return None


8

# remember that this is how you get the RGB values
#  im[:, :, 2] = 0   --> this makes all the Blue disappear
# im[:, :, 0] = 0    --> this makes all the red disappear

filename = "test.png"
image = imread(filename)
h, w, _ = image.shape

print("H: ", h, "w: ", w)
result = np.zeros((int(2.3 * h), (int(2.3 * w)), 3), dtype="uint8")

# result[0:h, 0:w, :] = im  # Temporary line, you can delete it

result = resize_image(image, int(2.3 * h), int(2.3 * w))

# print("result: \n", result)
# Write code that scales the image by a factor of 2.3
# It should call interpolate.

# Your Code Here

width = int(2.3 * w)
height = int(2.3 * h)
# print("width: ", width, " and height: ", height)
# res = cv2.resize(image, dsize=(width, height))
# print(res.shape)

# plt.imshow(result, vmin=0)
plt.imshow(result, vmin=0)
plt.show()

# original_image = image
# height = image.shape[0]
# width = image.shape[1]
#
# gridSize = 5
# grid = []
# for i in range(0, width, gridSize):
#     for j in range(0, height, gridSize):
#         a = Point(i, j)
#         b = Point(i + gridSize, j)
#         c = Point(i + gridSize, j + gridSize)
#         d = Point(i, j + gridSize)
#         grid.append([a, b, c, d])
# # Your code here
# print("GRID: ", grid)
