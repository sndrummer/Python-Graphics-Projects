import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

a = np.array([[0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0],
              [0, 1, 2, 1, 0],
              [0, 0, 3, 0, 0],
              [0, 0, 0, 0, 0]])

kernel = np.array([[1, 2, 1],
                   [2, 4, 2],
                   [1, 2, 1]])

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
    return flipped



def convolve(img, mask, dim):
    half = dim // 2
    pad_img = apply_zero_padding(img, 1)
    res_img = img.copy()
    # step 1 flip the mask
    f_mask = flip_mask(mask)
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
                    val += (f_mask[ki, kj] * pad_img[i - half + ki, j - half + kj])
            res_img[i - 1, j - 1] = val

    return res_img


print()
print("TEST:")
print(convolve(a, kernel, 3))
print()
print("CORRECT")
image = ndimage.convolve(a, kernel, mode='constant', cval=0.0)
print(image)
