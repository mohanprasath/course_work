#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def center(a):
    return ((a.shape[0]-1)/2, (a.shape[1]-1)/2)   # note the order: (center_y, center_x)

def radial_distance(a):
    mid_points = center(a)
    distances = []
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
             distances.append(np.linalg.norm((j-mid_points[1], i-mid_points[0])))
    return np.asarray(distances).reshape((a.shape[0], a.shape[1]))

def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
[tmin,tmax]."""
    a_scaled = np.interp(a, (a.min(), a.max()), (tmin, tmax))
    return a_scaled

def radial_mask(a):
    a = scale(1 - radial_distance(a))
    return a

def radial_fade(a):
    a = a * radial_mask(a)[:,:, np.newaxis]
    return a

def main():
    image = plt.imread("src/painting.png").copy()
    f, ax = plt.subplots(3,1)
    ax[0].imshow(image)
    ax[1].imshow(radial_mask(image))
    ax[2].imshow(radial_fade(image))
    plt.show()

if __name__ == "__main__":
    main()
