import numpy as np
import matplotlib.pyplot as plt
import math

a = np.array([[10., 11., 9., 25., 22.],
              [8., 10., 9., 26., 28.],
              [9., 8., 9., 24., 25.],
              [11., 11., 12., 23., 22.],
              [10., 11., 9., 22., 25.]])

xmask = np.array([[-1, 0, 1],
                  [-2, 0, 2],
                  [-1, 0, 1]])

ymask = np.array([[-1, -2, -1],
                  [0, 0, 0],
                  [1, 2, 1]])


def sobel(img, mask, dim):
    half = dim // 2
    og_img = img.copy()
    res_img = img.copy()
    res_img.astype(float)
    # print(res_img)
    # step 1 do not flip the mask for unsharp i think
    f_mask = mask
    k_rows = f_mask.shape[0]
    k_cols = f_mask.shape[1]
    # now overlay mask on top of the image !!!
    image_rows = og_img.shape[0]
    image_cols = og_img.shape[1]
    for i in range(1, image_rows - 1):
        for j in range(1, image_cols - 1):
            val = 0
            for ki in range(k_rows):
                for kj in range(k_cols):
                   # print("Adding ", f_mask[ki, kj], " * ", og_img[i - half + ki, j - half + kj])
                    val += (f_mask[ki, kj] * og_img[i - half + ki, j - half + kj])
            div8 = val / 8
            # print("Val: ", val, " val/8 is ", div8, "rounded", round(div8, 1))
            res_img[i, j] = round(div8, 1)  # divide by 8

    return res_img


def get_gradient_magnitude(xsob, ysob, img):
    new_image = img.copy()
    image_rows = x_sob.shape[0]
    image_cols = x_sob.shape[1]
    for i in range(1, image_rows - 1):
        for j in range(1, image_cols - 1):
            val = round(math.sqrt((xsob[i, j] ** 2) + (y_sob[i, j] ** 2)), 1)
            new_image[i, j] = val
    return new_image


x_sob = sobel(a, xmask, 3)
y_sob = sobel(a, ymask, 3)

print(get_gradient_magnitude(x_sob, y_sob, a))


