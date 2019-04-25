from matplotlib.pyplot import imread
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

# cat = imread('cat.jpg')
# cat = np.matrix(cat, dtype=np.int32)

peacock = imread('peacock.png')
# peacock = np.matrix(peacock, dtype=np.int32)
plt.imshow(peacock, cmap="Greys_r", vmin=0)
plt.title("Original Pea")
plt.show()


def brightAdjust(image, c):
    # mcolors.rgb_to_hsv(image)
    brightened = image.copy()
    color = image[::]

    color += c

    val = int(c)
    if val > 0:
        print("BRIGHT:", color)
    elif val < 0:
        print("Dark:", color)

    np.clip(image, 0, 255)
    return image


bright_cat = brightAdjust(peacock, 100)
plt.imshow(bright_cat)
plt.title("Bright Cat")
plt.show()
