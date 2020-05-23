#!/usr/bin/env python3

import numpy as np

def multiplication_table(n):
    # My Solution
    _ = np.arange(3)
    result = np.zeros(shape=(n,n))
    for i in range(n):
        for j in range(n):
            result[i][j] = i * j
    # return result
    # Model Solution
    a=np.arange(n)
    return a[:, np.newaxis] * a[np.newaxis, :]

def main():
    print(multiplication_table(4))

if __name__ == "__main__":
    main()
