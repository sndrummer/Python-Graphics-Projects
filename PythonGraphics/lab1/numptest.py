# Functions 4: Working with Numpy
# Write the following three functions:
#
# 1. flip: Takes in a numpy array, flips it upside down and returns it. (Note: You don't need a for loop and you may not use np.flip)
# 2. green_channel: Takes in a 3-dimensional array and returns a 2-dimensional array containing only the green channel of the image.

import numpy as np
import matplotlib.pyplot as plt


def flip(image):
    return image[::-1, :]  # reverse the rows


def red_channel(image):
    redChannel = image[:, :, 0]

    return redChannel


def green_channel(image):
    green_ch = image[:, :, 1]
    return green_ch


def blue_channel(image):
    blueChannel = image[:, :, 2]
    print("AFTER:", blueChannel)
    return blueChannel


#
# a = np.array([[1, 2], [3, 4], [5, 6]])
#
# print("normal:\n", a)
# print("reversed:\n", flip(a))
# print()
#

#
# geese = plt.imread('geese.jpg')
# print(geese)
# print(geese[0, 0, :])
# green = green_channel(geese)
# print(green)
#
# s = 0
# for i in range(3):
# 	for j in range(3):
# 		print(s, green[i, j, :])
# 		s = s + 1

# plt.imshow(geese)
# plt.title("The Geese")
# plt.show()

# test1 = flip(geese)
# plt.imshow(test1);
# plt.title("Flipped");
# plt.show()

#
# test3 = green_channel(geese)
# plt.imshow(test3)
# plt.title("HUH?")
# plt.show()
#
#
# test2 = green_channel(geese)
# plt.imshow(test2, cmap="Greys_r");
# plt.title("The Grey Value of the Green Channel");
# plt.show()

a = [
    [[1, 2], [1, 2], [1, 2], [1, 2]],
    [[1, 2], [1, 2], [1, 2], [1, 2]],
    [[1, 2], [1, 2], [1, 2], [1, 2]]
]

print(np.shape(a))

print(a)
