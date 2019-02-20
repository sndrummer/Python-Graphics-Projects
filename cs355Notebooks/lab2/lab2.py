from matplotlib.pyplot import imread
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

cat = imread('cat.jpg')
cat = np.matrix(cat, dtype=np.int32)
plt.imshow(cat, cmap="Greys_r", vmin=0)
plt.show()


# peacock = imread('peacock.png')
# # peacock = np.matrix(peacock, dtype=np.int32)
# plt.imshow(peacock, cmap="Greys_r", vmin=0)
# plt.show()

# Takes in a grayscale image and returns the brightened version of that image according to a
# passed in parameter. Use a max image value of 255.

# new_image = (old_image) × (contrast/127 + 1) - contrast + brightness
def brightAdjust(image, c):
    newImg = image.copy()
    print("OG: ", image)
    image = image + c
    return np.clip(image, 0, 255)


def test_bright():
    bright_cat = brightAdjust(cat, 100)
    print("BRIGHT CAT -->:", bright_cat)

    plt.imshow(bright_cat, cmap="Greys_r", vmin=0, vmax=255)
    plt.title("Bright Cat")
    plt.show()
    dark_cat = brightAdjust(cat, -100)
    print("DARK CAT -->:", dark_cat)
    plt.imshow(dark_cat, cmap="Greys_r", vmin=0, vmax=255)
    plt.title("Dark Cat")
    plt.show()


# s = ((((c + 100)/ 100) ** 4) * (r - 128)) + 128
# REMEMBER THAT 'r' is THE OLD IMAGE
def contrastAdjust(image, c):
    newImg = image.copy()
    contrast = c
    if contrast < -100:
        contrast = -100
    if contrast > 100:
        contrast = 100

    newImg = ((((contrast + 100) / 100) ** 4) * (newImg - 128)) + 128
    return np.clip(newImg, 0, 255)


def print_original(cat):
    plt.imshow(cat, cmap="Greys_r", vmin=0)
    plt.title("Original")
    plt.show()


# Function 2: Contrast Adjustment
def test_contrast():
    high_contrast_cat = contrastAdjust(cat, 50)
    plt.imshow(high_contrast_cat, cmap="Greys_r", vmin=0, vmax=255);
    plt.title("High Contrast Cat");
    plt.show()
    low_contrast_cat = contrastAdjust(cat, -50)
    plt.imshow(low_contrast_cat, cmap="Greys_r", vmin=0, vmax=255);
    plt.title("Low Contrast Cat");
    plt.show()

    maxChangeCat = contrastAdjust(cat, 100)
    plt.imshow(maxChangeCat, cmap="Greys_r", vmin=0, vmax=255);
    plt.title("Max Change Cat");
    plt.show()

    overChangeCat = contrastAdjust(cat, 10000)
    plt.imshow(overChangeCat, cmap="Greys_r", vmin=0, vmax=255);
    plt.title("Past Max Change Cat");
    plt.show()

    minChangeCat = contrastAdjust(cat, -100)
    plt.imshow(minChangeCat, cmap="Greys_r", vmin=0, vmax=255);
    plt.title("Min Change Cat");
    plt.show()


# Function 3: Thresholding
# Takes in a grayscale image and returns the thresholded version of the image according to a passed in
# parameter. Every pixel that is higher than or equal to the parameter is 255, everything below is
# zero. (Hint: Use np.where)
def thresholder(image, c):
    new_img = image.copy()
    new_img[np.where(new_img < c)] = 0
    new_img[np.where(new_img >= c)] = 255
    return new_img


def test_threshold():
    thresholded_cat = thresholder(cat, 80)
    plt.imshow(thresholded_cat, cmap="Greys_r", vmin=0, vmax=255);
    plt.title("Thresholded Cat");
    plt.show()
    return None


# Function 4: Cropping
def cropper(image, width, height, x=0, y=0):
    """
    Takes in a grayscale image, an x and y of a topleft pixel, a width,
    and a height and returns a cropped version of
    that image according to those parameters.

    :param image:
    :param width:
    :param height:
    :param x:
    :param y:
    :return:
    """
    new_img = image.copy()
    return new_img[y:y + height, x:x + width]


def test_cropper():
    # This should show just the ear of the cat
    cropped_cat1 = cropper(cat, 100, 100)
    print("Dimensions of Cropped: ", cropped_cat1.shape)
    plt.imshow(cropped_cat1, cmap="Greys_r", vmin=0, vmax=255);
    plt.title("Cropped Cat 1");
    plt.show()
    # This should show just the eyes of the cat
    cropped_cat2 = cropper(cat, 120, 75, 90, 80)
    print("Dimensions of Cropped: ", cropped_cat2.shape)
    plt.imshow(cropped_cat2, cmap="Greys_r", vmin=0, vmax=255);
    plt.title("Cropped Cat 2");
    plt.show()


def scaler(image):
    new_image = image.copy()
    y, x = new_image.shape
    new_image = new_image[::2, ::2]
    return new_image


def test_scalar():
    scaled_cat = scaler(cat)

    fig = plt.figure()
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.imshow(cat, cmap="Greys_r", vmin=0, vmax=255);
    ax1.set_title("Original")
    ax2 = fig.add_subplot(1, 2, 2)
    ax2.imshow(scaled_cat, cmap="Greys_r", vmin=0, vmax=255);
    ax2.set_title("Scaled")
    plt.show()


# test_bright()
# print_original(cat)
# test_contrast()
# print_original(cat)
# test_threshold()
# print_original(cat)
# test_cropper()
# print_original(cat)
test_scalar()
print_original(cat)
