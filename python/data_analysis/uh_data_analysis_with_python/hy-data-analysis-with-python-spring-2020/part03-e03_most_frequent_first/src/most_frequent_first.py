#!/usr/bin/env python3

import numpy as np
import collections
from collections import Counter

def unique(sequence):
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))]

def most_frequent_first(a, c):
    values = {}
    temp = []
    for row in range(np.shape(a)[0]):
        value = a[row, c]
        if value in values:
            existing = values[value]
            existing.append(row)
            values[value] = existing
        else:
            temp_existing = [row]
            values[value] = temp_existing
        temp.append(value)
    counts = collections.Counter(temp)
    new_list = sorted(temp, key=lambda x: -counts[x])
    result = []
    for entry in unique(new_list):
        rows = values[entry]
        for r in rows:
            result.append(a[r,:])
    return np.array(result)

def main():
    a = np.array([[8, 9, 3, 8, 8],
[0, 5, 3, 9, 9],
[5, 7, 6, 0, 4],
[7, 8, 1, 6, 2],
[2, 1, 3, 5, 8]])
    print(most_frequent_first(a, -1))

if __name__ == "__main__":
    main()
