import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import math


# Set Matrix in this order: TRS
# 1. T for translation with ones always
# 2. R for rotation matrix:
#       a. Counterclockwise: cos -sin, sin cos
#       b. Clockwise: sin cos, -sin cos
# 3. S for scaling


def get_rotation_matrix(degrees_rotation):
    radians = math.radians(degrees_rotation)
    c, s = np.cos(radians), np.sin(radians)
    rot_matrix = np.matrix([[c, s, 0],
                            [-s, c, 0],
                            [0, 0, 1]])
    return rot_matrix


def get_transformation_matrix(offset_x, offset_y):
    return np.matrix([[1, 0, offset_x],
                      [0, 1, offset_y],
                      [0, 0, 1]])


def get_scaling_matrix(scale_x, scale_y):
    return np.matrix([[scale_x, 0, 0],
                      [0, scale_y, 0],
                      [0, 0, 1]])


def test_compose(image, offset_x, offset_y, degrees_rotation, scale_x, scale_y):
    t = get_transformation_matrix(offset_x, offset_y)
    r = get_rotation_matrix(degrees_rotation)
    s = get_scaling_matrix(scale_x, scale_y)
    return t * r * s * image


def compose(frame, image, offset_x, offset_y, degrees_rotation, scale_x, scale_y):
    width, height = frame.size
    t = get_transformation_matrix(offset_x, offset_y)
    r = get_rotation_matrix(degrees_rotation)
    s = get_scaling_matrix(scale_x, scale_y)

    transformation = t * r * s
    # Invert matrix for compose function, grab values for Affine Transform
    t = np.linalg.inv(transformation)
    a = t[0, 0]
    b = t[0, 1]
    c = t[0, 2]
    d = t[1, 0]
    e = t[1, 1]
    f = t[1, 2]

    image = image.transform((width, height), Image.AFFINE, (a, b, c, d, e, f), Image.BILINEAR)

    im = np.sum(np.asarray(image), -1)
    print("image:", image)
    vals = 255.0 * (im > 0)
    mask = Image.fromarray(vals).convert("1")
    # Composite images together
    result = Image.composite(image, frame, mask)

    return result


# test
my_image = np.matrix([[280],
                      [312],
                      [1]])
print("Solution:\n", test_compose(my_image, 300, 400, 30, .25, .25))

# Open the two images
filename = "PictureFrameCollage.png"
frame = Image.open(filename).convert("RGB")

filename0 = "Bird0.png"
im = Image.open(filename0).convert("RGB")

filename1 = "Bird1.png"
im1 = Image.open(filename1).convert("RGB")

filename2 = "Bird2.png"
im2 = Image.open(filename2).convert("RGB")

filename3 = "Bird3.png"
im3 = Image.open(filename3).convert("RGB")

filename4 = "Bird4.png"
im4 = Image.open(filename4).convert("RGB")

filename5 = "Bird5.png"
im5 = Image.open(filename5).convert("RGB")

filename6 = "Bird6.png"
im6 = Image.open(filename6).convert("RGB")

filename7 = "Bird7.png"
im7 = Image.open(filename7).convert("RGB")

filename8 = "Bird8.png"
im8 = Image.open(filename8).convert("RGB")

filename9 = "Bird9.png"
im9 = Image.open(filename9).convert("RGB")

filename10 = "Bird10.png"
im10 = Image.open(filename10).convert("RGB")

filename11 = "Bird11.png"
im11 = Image.open(filename11).convert("RGB")

# Define the transformation to the first picture frame
transformation = np.matrix([[1, 0, 619],
                            [0, 1, 433],
                            [0, 0, 1]])

# Compose the two images together
result0 = compose(frame, im, 619, 433, 0, 1, 1)
result1 = compose(result0, im1, 308, 463, 0, .736, .736)
result2 = compose(result1, im2, 385, 379, 45, 1, 1)
result3 = compose(result2, im3, 46, 354, 15, 1.21, 1.21)
result4 = compose(result3, im4, 305, 358, -45, 0.389, 0.389)
result5 = compose(result4, im5, 350, 138, -45, 1, 1)
result6 = compose(result5, im6, 41, 30, 0, 1.21, 1.21)
result7 = compose(result6, im7, 283, 46, 0, 0.389, 0.389)
result8 = compose(result7, im8, 633, 228, 15, 0.736, 0.736)
result9 = compose(result8, im9, 419, 87, 30, 1, 1)
result10 = compose(result9, im10, 514, 225, 0, 0.389, 0.389)
result11 = compose(result10, im10, 673, 37, -15, 0.653, 0.653)
# Show the result

plt.imshow(result11)


plt.show()

# Uncomment this line if you want to save the image
# result.save("Output.png")
