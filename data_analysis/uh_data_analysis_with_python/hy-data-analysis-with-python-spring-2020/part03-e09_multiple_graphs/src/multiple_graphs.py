#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def main():
    plt.plot(np.array([2, 4, 6, 7]), np.array([4, 3, 5, 1]))
    plt.plot(np.array([1, 2, 3, 4]), np.array([4, 2, 3, 1]))
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('title')
    plt.show()

if __name__ == "__main__":
    main()
