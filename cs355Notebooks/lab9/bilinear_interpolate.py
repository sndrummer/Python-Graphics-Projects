from scipy.ndimage import imread
import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import imsave
import math


class Point:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.rgb = value

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'Point({self.x}, {self.y})'


# Your bilinear interpolation function
def interpolate(points, x, y):
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


filename = "test.png"
image = imread(filename)
h, w, _ = image.shape

print("H: ", h, "w: ", w)
result = np.zeros((int(2.3 * h), (int(2.3 * w)), 3), dtype="uint8")

result[0:h, 0:w, :] = image  # Temporary line, you can delete it

plt.imshow(result, vmin=0)
plt.show()

result = resize_image(image, int(2.3 * h), int(2.3 * w))

plt.imshow(result, vmin=0)
plt.show()
