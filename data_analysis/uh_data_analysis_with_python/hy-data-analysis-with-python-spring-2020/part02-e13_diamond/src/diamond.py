#!/usr/bin/env python3

import numpy as np

def diamond(n):
    temp = np.eye(n, dtype=int)
    fliped = np.fliplr(temp)
    concat = np.concatenate((np.fliplr(temp), temp), axis=1)
    concat = np.delete(concat, n, 1)
    reverse_flipped=  np.flip(concat)
    return np.concatenate((concat, np.flip(concat)[1:,]))   

def main():
    pass

if __name__ == "__main__":
    main()
