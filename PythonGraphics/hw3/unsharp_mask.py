import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from imageio import imread


# enhanced image = original + amount * (original - blurred)
# Formula is  I' = 1/A (AI, + 5(I - *I*))
# I is original, *I* is blurred input image

a = np.array([[10, 11, 9, 25, 22],
              [8, 10, 9, 26, 28],
              [9, 8, 9, 24, 25],
              [11, 11, 12, 23, 22],
              [10, 11, 9, 22, 25]])

kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])

mask2 = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])


def apply_zero_padding(image, amt):
    new_image = np.array(image)

    for x in range(amt):
        # Add padding to sides
        new_image = np.insert(new_image, 0, 0, axis=1)
        numcols = new_image.shape[1]
        new_image = np.insert(new_image, numcols, 0, axis=1)

        # Add padding to top and bottom
        new_image = np.insert(new_image, 0, 0, axis=0)
        numrows = new_image.shape[0]
        new_image = np.insert(new_image, numrows, 0, axis=0)

    return new_image


def flip_mask(mask):
    flipped = mask[:, ::-1]
    flipped = flipped.transpose(1, 0)
    flipped = flipped[:, ::-1]
    flipped = flipped.transpose(1, 0)
    print("FLIPPED:\n", flipped)
    return flipped


def unsharp(img, mask, dim, A):
    half = dim // 2
    pad_img = apply_zero_padding(img, 1)
    res_img = img.copy()
    # step 1 do not flip the mask for unsharp i think
    f_mask = mask
    k_rows = f_mask.shape[0]
    k_cols = f_mask.shape[1]
    # now overlay mask on top of the image !!!
    image_rows = pad_img.shape[0]
    image_cols = pad_img.shape[1]
    for i in range(1, image_rows - 1):
        for j in range(1, image_cols - 1):
            val = 0
            for ki in range(k_rows):
                for kj in range(k_cols):
                    val += (f_mask[ki, kj] * pad_img[i - half + ki, j - half + kj]) / A
            res_img[i - 1, j - 1] = val

    return res_img

def toGrayScale(image):
    """
       Takes in a color image and returns a grayscale image using the following formula:
       Gray = (0.299 Red + 0.587 Green + 0.114 Blue)
       :param image: an image to convert to grayscale
       :return: gray scale image
       """
    gray_scale = image.copy()
    gray2 = (image[:, :, 0] * .299) + (0.587 * image[:, :, 1]) + (0.114 * image[:, :, 2])
    # important thing to remember here is that the dot product is EQUIVALENT TO THE ABOVE!!
    gray = np.dot(image[..., :], [0.299, 0.587, 0.114])

    return gray

print()
print("TEST:")
print(unsharp(a, kernel, 3, 1))
print()
print("CORRECT")
image = ndimage.convolve(a, kernel, mode='constant', cval=0.0)
print(image)
# if A = 1 then we have (AI, + 5(I - *I*))

my_kernel = np.matrix([[0, -1, 0],
                       [-1, 6, -1],
                       [0, -1, 0]])

racoon = imread('racoon.jpg')
racoon = np.array(racoon, dtype=np.int32)
gray_racoon = toGrayScale(racoon)
# sharpen_racoon = unsharp(gray_racoon)

print(unsharp(gray_racoon, my_kernel, 3, 2))
