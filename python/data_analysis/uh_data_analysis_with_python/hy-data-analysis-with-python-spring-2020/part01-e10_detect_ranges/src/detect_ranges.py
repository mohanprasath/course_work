#!/usr/bin/env python3

def detect_ranges(L):
    result = []
    sorted_l = sorted(L.copy())
    from itertools import groupby
    from operator import itemgetter
    temp = []
    for k, g in groupby(enumerate(sorted_l), lambda ix : ix[0] - ix[1]):
        temp.append(list(map(itemgetter(1), g)))
        print(temp)
    for entry in temp:
        if len(entry) == 1:
            result.append(entry[0])
        else:
            result.append((entry[0], entry[-1]+1))
    return result

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
