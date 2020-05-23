#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
    m, twom = a.shape
    print(twom/2)
    half = int(twom/2)
    return a[np.sum(a[:,0:half], axis=1) > np.sum(a[:,half:], axis=1)]

def main():
    print(first_half_second_half(np.array([[1, 3, 4, 2],
[2, 2, 1, 2]])))

if __name__ == "__main__":
    main()
