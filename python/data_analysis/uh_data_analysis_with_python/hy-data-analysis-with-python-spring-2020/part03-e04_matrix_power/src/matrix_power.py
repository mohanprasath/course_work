#!/usr/bin/env python3
import numpy as np
from functools import reduce

def array_raised_to_power_of_n(a, n, inverse=False):
    for num in range(1, n+1):
        yield (np.linalg.inv(a) if inverse else a)

def matrix_power(a, n):
    if n == 0:
        return np.eye(a.shape[0])
    elif n == 1: 
        return a
    else:
        if n > 0:
            return reduce(np.matmul, array_raised_to_power_of_n(a, n))
        else:
            return reduce(np.matmul, array_raised_to_power_of_n(a, abs(n), inverse=True)) 

def main():
    print(matrix_power(np.array([[1, 2, 3,], [4, 5, 6], [7, 8, 9]]), 3))

if __name__ == "__main__":
    main()
