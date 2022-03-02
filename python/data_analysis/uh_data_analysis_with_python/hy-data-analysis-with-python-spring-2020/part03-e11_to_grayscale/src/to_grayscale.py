#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def to_grayscale(array_3d):
    '''
    Converts the given 3D numpy array of an image into a grayscale image

    '''
    temp = np.dot(array_3d[...,:3], [0.2126, 0.7152, 0.0722])
    return temp

def to_red(array_3d):
    temp = array_3d.copy()
    return temp * np.array([1, 0, 0])

def to_green(array_3d):
    temp = array_3d.copy()
    return temp * np.array([0, 1, 0])

def to_blue(array_3d):
    temp = array_3d.copy()
    return temp * np.array([0, 0, 1])

def main():
    image = plt.imread("src/painting.png")
    gray = to_grayscale(image)
    plt.imshow(gray, cmap="gray")
    plt.show()

    red_scale = to_red(image)
    green_scale = to_green(image)
    blue_scale = to_blue(image)

    fig, ax = plt.subplots(3, 1)
    ax[0].imshow(red_scale)
    ax[1].imshow(green_scale)
    ax[2].imshow(blue_scale)
    plt.show()

if __name__ == "__main__":
    main()
