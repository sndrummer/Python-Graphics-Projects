import numpy as np
import matplotlib.pyplot as plt

a = [[10, 11, 9, 25, 22],
     [8, 10, 9, 26, 28],
     [9, 99, 9, 24, 25],
     [11, 11, 12, 23, 22],
     [10, 11, 9, 22, 25]]


def add_empty_pure(image, amt):
    new_image = image.copy()
    for x in range(amt):
        new_image = [[0] + x for x in new_image]
        new_image = [x + [0] for x in new_image]
        numcols = len(new_image[0])
        print("numcols: ", numcols)
        new_image.append(numcols * [0])
    # new_image.
    return new_image


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


def avg_gen(kernel_size, i, j, og_img, new_img):
    r = kernel_size / 2
    i = i - r
    j = j - r

    np.sum(og_img, axis=1)
    for k in range(kernel_size / 2):
        for l in range(kernel_size / 2):
            og_img[i + k, j + l]
    return None


def avg_3x3(i, j, og_img, new_img):
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
    # get pixel
    pixel = og_img[i, j]
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
    sum = (pixel + tl + top + tr + left + right + bl + bottom + br)
    s = np.sum(og_img, axis=1)
    print("Sum1: ", s)
    avg = (pixel + tl + top + tr + left + right + bl + bottom + br) / 9
    avg = int(round(avg))
    new_img[i, j] = avg


def mean_filter_helper(img):
    # print("OG image:\n", img)
    new_image = img.copy()
    rows = new_image.shape[0]
    cols = new_image.shape[1]
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            avg_3x3(i, j, img, new_image)
    return new_image


def mean_filter(img):
    test = np.array(img)
    print("OG image:\n", img)
    #res = test[1::2, 1::2]

    row_idx = np.array([0, 1])
    col_idx = np.array([0, 1])
    print(test[row_idx[:, None], col_idx])

    padded_img = apply_zero_padding(img, 1)
    filtered_img = mean_filter_helper(padded_img)

    # print(filtered_img)
    return filtered_img


image = mean_filter(a)
print("new image:\n", image)

# nd_a = np.array(image)

# print(image)
