#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import random

def subfigures(a):
    fig, ax = plt.subplots(1,2)
    ax[0].plot(a[:, 0], a[:, 1])
    ax[1].scatter(a[:, 0], a[:, 1], c=a[:, 2], s=a[:, 3])
    plt.show()

def main():
    l = []
    for i in range(100):
        temp = []
        for j in range(4):
            temp.append(random.randint(1, 101))
        l.append(temp)
    subfigures(np.array(l))

if __name__ == "__main__":
    main()
