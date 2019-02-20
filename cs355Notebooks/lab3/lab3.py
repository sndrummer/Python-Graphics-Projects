from imageio import imread
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import statistics
import math
from scipy import ndimage


def toHSB(image):
    from matplotlib import colors
    temp = 255 * colors.rgb_to_hsv(image / 255.0)
    return temp.astype(np.int32)


def toRGB(image):
    from matplotlib import colors
    temp = 255 * colors.hsv_to_rgb(image / 255.0)
    return temp.astype(np.int32)


def plotImage(image, title=""):
    im = np.array(image, dtype=np.uint8)
    plt.imshow(im, vmin=0, vmax=255)
    plt.title(title)
    plt.show()


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


def brightAdjust(image, c):
    """
    Takes in a color image and returns the brightened version of that image according to a passed in
    parameter. Use a max image value of 255.
    :param image:
    :param c:
    :return:
    """
    im = toHSB(image)

    im = np.array(im, dtype=np.int32)
    im[..., 2] = np.minimum(im[..., 2] + c, 255)
    im[..., 2] = np.maximum(im[..., 2], 0)
    im = np.array(im, dtype=np.uint8)
    # print("After222: ", im[..., :])
    # Your code here
    return toRGB(im)


def contrastAdjust(image, c):
    """
    Takes in a color image and returns the contrasted version of that image according to a passed in
    parameter. Use a max image value of 255.

    Also, rather than a straight linear operation, we will use a mapping similar to what Photoshop
    does. In particular, the contrast will be in the range [-100,100] where 0 denotes no change,
    -100 denotes complete loss of contrast, and 100 denotes maximum enhancement (8x multiplier).
    If c is the contrast parameter, then the level operation applied is:
        𝑠 = ((𝑐+100)/100)^4(𝑟−128)+128

    :param image:
    :param c:
    :return:
    """
    im = toHSB(image)

    im = np.array(im, dtype=np.int32)
    im[..., 2] = np.minimum((((c + 100.0) / 100.0) ** 4) * (im[..., 2] - 128.0) + 128.0, 255)
    im[..., 2] = np.maximum(im[..., 2], 0)
    im = np.array(im, dtype=np.uint8)

    return toRGB(im)


def alphaBlend(image1, image2, alpha=.5):
    """
    Takes in 2 color images of the same size. Given an alpha value it returns the blended image
    according to the alpha value. Note that your alpha value can be a single number or a mask image
     of the same size. The alpha values will be between 0 and 1.
    """
    return image1 * (1.0 - alpha) + image2 * alpha


def crossDissolve(image1, image2, numsteps=10):
    """
    Takes in 2 color images of the same size. Returns an array of alpha blend of those two images,
    where the first picture is an alpha value of 1, the last picture is an alpha value of 0, and the
    middle pictures slowly decrease until reaching zero. Allow the user to specify the number of
    steps in the cross dissolve. You can then feed this array into our animation function to view
    the cross dissolve.
    :param image1:
    :param image2:
    :param numsteps:
    :return: an array of alpha blends
    """

    res = np.zeros(image1.shape, dtype=np.int32)
    ims = []
    for i in range(numsteps - 1, -1, -1):
        # 0 - 9 is the list, 9 = 1, 0=0
        alpha = i / 9.0
        ab = alphaBlend(image1, image2, alpha)
        ims.append(ab)
    return ims


def blur(image, size=3):
    """
    Takes in a grayscale image and returns a corresponding result that has been blurred
    (spatially filtered) using a uniform averaging. Allow the user to specify the size of the kernel
    (ex. size=3 would give a 3x3 kernel). You can ignore the edge pixels.
    (Hint: np.sum() may be useful)
    :param image: input image
    :param size: kernel size
    :return:
    """
    # Create a result buffer so that you don't affect the original image
    result = np.zeros(image.shape)
    rows, cols = result.shape
    k = size // 2
    for i in range(k, rows - k):
        for j in range(k, cols - k):
            section = image[i - k:i + k + 1, j - k:j + k + 1]
            result[i, j] = np.sum(section) / (size * size)
    return result


def medianFilter(image, size=3):
    """
    Takes in a grayscale image and returns a corresponding result that has been median filtered.
    Allow the user to specify the size of the kernel (ex. size=3 would give a 3x3 kernel).
     You can ignore the edge pixels.
    :param image:
    :param size:
    :return:
    """
    result = np.zeros(image.shape)
    rows, cols = result.shape
    k = size // 2
    for i in range(k, rows - k):
        for j in range(k, cols - k):
            section = image[i - k:i + k + 1, j - k:j + k + 1]
            med_list = section.ravel().tolist()
            med_list.sort()
            median = statistics.median(med_list)
            result[i, j] = median
    return result


def convolution(image, kernel):
    """
    Now that you have written a couple of different kernels, write a general convolution function
    that takes in an image and kernel (stored as a numpy matrix), and performs the appropriate
    convolution. You can assume the kernel is 3x3 if you would like, but it is not much harder to do
    a general size kernel as well.
    :param image:
    :param kernel:
    :return:
    """

    # THIS IS THE BETTER WAY !!!!!!!!!!! MUCH FASTER!@!!!!!
    flipped = np.flip(kernel)
    krows, kcols = kernel.shape
    result = np.zeros(image.shape)
    rows, cols = result.shape
    ki = krows // 2
    kj = kcols // 2
    for i in range(ki, rows - ki):
        for j in range(kj, cols - kj):
            section = image[(i - ki):(i + ki + 1), (j - kj):(j + kj + 1)]
            value = np.asarray(flipped).flatten() * section.flatten()
            result[i, j] = value.sum()
    return result


#
def convolution2(image, kernel):
    """
    Now that you have written a couple of different kernels, write a general convolution function
    that takes in an image and kernel (stored as a numpy matrix), and performs the appropriate
    convolution. You can assume the kernel is 3x3 if you would like, but it is not much harder to do
    a general size kernel as well.
    :param image:
    :param kernel:
    :return:
    """
    flipped = np.flip(kernel)
    krows, kcols = kernel.shape
    result = np.zeros(image.shape)
    rows, cols = result.shape
    ki = krows // 2
    kj = kcols // 2
    for i in range(ki, rows - ki):
        for j in range(kj, cols - kj):
            val = 0
            for k in range(krows):
                for l in range(kcols):
                    val += (flipped[k, l] * image[i - ki + k, j - kj + l])
            result[i, j] = val
    return result


def sharpen(image):
    """
    Takes in a grayscale image and returns a corresponding result that has been sharpened using an
    unsharp masking kernel that has a 6 in the middle and -1s for the four-connected neighbors.
    You can use your general convolution function. You can ignore the edge pixels. Don't forget to
    normalize your results.

    :param image:
    :return:
    """
    # Don't DIVIDE BY TWO!!!
    kernel = np.matrix([[0, -1, 0],
                        [-1, 6, -1],
                        [0, -1, 0]])

    krows, kcols = kernel.shape
    result = np.zeros(image.shape)
    rows, cols = result.shape
    ki = krows // 2
    kj = kcols // 2

    for i in range(ki, rows - ki):
        for j in range(kj, cols - kj):
            section = image[(i - ki):(i + ki + 1), (j - kj):(j + kj + 1)]
            value = np.asarray(kernel).flatten() * section.flatten()
            result[i, j] = value.sum() / 2
    return result


def get_sobel_kernels(image):
    xmask = np.array([[-1, 0, 1],
                      [-2, 0, 2],
                      [-1, 0, 1]])

    ymask = np.array([[-1, -2, -1],
                      [0, 0, 0],
                      [1, 2, 1]])

    xresult = np.zeros(image.shape)
    yresult = np.zeros(image.shape)
    rows, cols = xresult.shape

    krows, kcols = xmask.shape
    ki = krows // 2
    kj = kcols // 2
    for i in range(ki, rows - ki):
        for j in range(kj, cols - kj):
            section = image[(i - ki):(i + ki + 1), (j - kj):(j + kj + 1)]
            xval = np.asarray(xmask).flatten() * section.flatten()
            yval = np.asarray(ymask).flatten() * section.flatten()
            xresult[i, j] = xval.sum() / 8
            yresult[i, j] = yval.sum() / 8
    return xresult, yresult


def edgeDetect(image):
    xsobel, ysobel = get_sobel_kernels(image)
    result = np.zeros(image.shape)
    result = np.zeros(image.shape)
    rows, cols = xsobel.shape
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            val = math.sqrt((xsobel[i, j] ** 2) + (ysobel[i, j] ** 2))
            result[i, j] = val
    return result


############################## FUNCTION ONE ####################################
racoon = imread('racoon.jpg')
racoon = np.array(racoon, dtype=np.int32)
plotImage(racoon)
#
# # Test Case
# gray_racoon = toGrayScale(racoon)
#
# plt.imshow(gray_racoon, cmap="Greys_r", vmin=0, vmax=255)
# plt.title("Grayscale Racoon")
# plt.show()
####################################################################

############################## FUNCTION TWO ####################################
# Test Case
# bright_racoon = brightAdjust(racoon, 100)
# plotImage(bright_racoon, "Bright Racoon")
# dark_racoon = brightAdjust(racoon, -100)
# plotImage(dark_racoon, "Dark Racoon")

####################################################################

############################## FUNCTION THREE Contrast Adjustment ####################################
# Test Case
# contrast_racoon = contrastAdjust(racoon, 30)
# plotImage(contrast_racoon, "High Contrast Racoon")

####################################################################


############################## FUNCTION FOUR ALPHA BLEND ####################################
# out = image1 * (1.0 - alpha) + image2 * alpha
# Test Cases
# man = imread("man.jpg")
# city = imread("city.jpg")
# blended = alphaBlend(man, city, .7)
# plotImage(blended, "Alpha Blend with Single Value")
#
# mask1 = imread("alphamask1.jpg") / 255.0
# blended1 = alphaBlend(man, city, mask1)
# plotImage(blended1, "Alpha Blend with Mask 1")
#
# beach = imread("beach.jpg")
# boat = imread("boat.jpg")
# mask2 = imread("alphamask2.jpg") / 255.0
# blended2 = alphaBlend(boat, beach, mask2)
# plotImage(blended2, "Alpha Blend with Mask 2")

####################################################################

############################## FUNCTION FIVE Cross Dissolve ####################################
# Test Case

# beach = imread("beach.jpg")
# boat = imread("boat.jpg")
# dis = crossDissolve(beach, boat)
#
#
# fig = plt.figure()
# ims = []
# for im in dis:
#     im = np.array(im, dtype=np.uint8)
#     result = plt.imshow(im, vmin=0, vmax=255, animated=True)
#     ims.append([result])
#
# ani = animation.ArtistAnimation(fig, ims, interval=500, blit=True)
# plt.show()

####################################################################
############################## FUNCTION SIX UNIFORM BLURRING ####################################
# Test Case
# gray_racoon = toGrayScale(racoon)
# blur_racoon = blur(gray_racoon)
# plt.imshow(blur_racoon, cmap="Greys_r", vmin=0, vmax=255)
# plt.title("Uniform Blurring")
# plt.show()
#
# blur_racoon2 = blur(gray_racoon, 7)
# plt.imshow(blur_racoon2, cmap="Greys_r", vmin=0, vmax=255)
# plt.title("Uniform Blurring (7x7)")
# plt.show()

####################################################################
############################## FUNCTION SEVEN Median Filter ####################################
# Test Case
# gray_racoon = toGrayScale(racoon)
# median_racoon = medianFilter(gray_racoon)
# plt.imshow(median_racoon, cmap="Greys_r", vmin=0, vmax=255);
# plt.title("Median Blurring")
# plt.show()
#
# median_racoon2 = medianFilter(gray_racoon, 7)
# plt.imshow(median_racoon2, cmap="Greys_r", vmin=0, vmax=255);
# plt.title("Median Blurring (7x7)")
# plt.show()

####################################################################

############################## FUNCTION EIGHT General Convolution ####################################
# Test Case
# gray_racoon = toGrayScale(racoon)
#
# blur_kernel = np.matrix([[1, 1, 1],
#                          [1, 1, 1],
#                          [1, 1, 1]])
#
# poop_kernel = np.matrix([[1, 2, 1],
#                          [1, 2, 1],
#                          [1, 1, 2]])
#
# print("CONVOLVE CORRECT")
# image = ndimage.convolve(gray_racoon, blur_kernel, mode='constant', cval=0.0)
# print(image)
# blur_racoon2 = convolution2(gray_racoon, blur_kernel) / 9.0
# print("My convolve", blur_racoon2 * 9)
# plt.imshow(blur_racoon2, cmap="Greys_r", vmin=0, vmax=255);
# plt.title("Uniform Bluring")
# plt.show()

############################### Function 9 Unsharp #####################################
# Test Cases
# gray_racoon = toGrayScale(racoon)
# sharpen_racoon = sharpen(gray_racoon)
# print("SHARP", sharpen_racoon)
# plt.imshow(sharpen_racoon, cmap="Greys_r", vmin=0, vmax=255);
# plt.title("Sharpened")
# plt.show()
############################## FUNCTION 10 EDGE ####################################
# Test Case
# Test Cases
gray_racoon = toGrayScale(racoon)
edge_racoon = edgeDetect(gray_racoon)
plt.imshow(edge_racoon, cmap="Greys_r", vmin=0, vmax=255);
plt.title("Edge Detection")
plt.show()

####################################################################
