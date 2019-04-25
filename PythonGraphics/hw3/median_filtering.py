import numpy as np
import matplotlib.pyplot as plt
import statistics

a = [[10, 11, 9, 25, 22],
     [8, 10, 9, 26, 28],
     [9, 99, 9, 24, 25],
     [11, 11, 12, 23, 22],
     [10, 11, 9, 22, 25]]


def apply_zero_padding(img, amt):
    new_image = np.array(img)

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


def median_3x3(i, j, og_img, new_img):
    # get pixel
    pixel = og_img[i, j]
    # get top left
    tl = og_img[i - 1, j - 1]
    # print("Top Left of ", pixel, " is ", tl)
    # get top
    top = og_img[i - 1, j]
    # print("Top of ", pixel, " is ", top)
    # get top right
    tr = og_img[i - 1, j + 1]
    # print("Top right of ", pixel, " is ", tr)
    # get left
    left = og_img[i, j - 1]
    # print("Left of ", pixel, " is ", left)
    # get right
    right = og_img[i, j + 1]
    # print("Right of ", pixel, " is ", right)
    # get bottom left
    bl = og_img[i + 1, j - 1]
    # print("Bottom left of ", pixel, " is ", bl)
    # get bottom
    bottom = og_img[i + 1, j]
    # print("Bottom of ", pixel, " is ", bottom)
    # get bottom right
    br = og_img[i + 1, j + 1]
    # print("Bottom right of ", pixel, " is ", br)

    med_list = [pixel, tl, top, tr, left, right, bl, bottom, br]
    med_list.sort()
    median = statistics.median(med_list)
    print("List: ", med_list)
    print("Median is ", median)
    new_img[i, j] = median


def median_filter_helper(img):
    print("OG image:\n", img)
    new_image = img.copy()
    rows = new_image.shape[0]
    cols = new_image.shape[1]
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            median_3x3(i, j, img, new_image)
    return new_image


def median_filter(img):
    padded_img = apply_zero_padding(img, 1)
    filtered_img = median_filter_helper(padded_img)
    # print(filtered_img)
    return filtered_img


image = median_filter(a)

print("new image:\n", image)
