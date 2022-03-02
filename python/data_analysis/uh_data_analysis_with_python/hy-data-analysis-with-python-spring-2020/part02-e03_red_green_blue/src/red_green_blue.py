#!/usr/bin/env python3

import os
import re

def red_green_blue(filename="src/rgb.txt"):
    path = os.path.dirname(os.path.realpath(__file__))
    result = []
    with open(path[:-3] + filename, 'r') as infile:
        first_line = infile.readline()
        for line in infile:
            values = list(re.findall(r"\A\s*(\d+)\s*(\d+)\s*(\d+)", line)[0])
            name = re.findall(r"\t\t(.+?)\n", line)
            result.append("\t".join(values+name))
    return result


def main():
    print(red_green_blue())

if __name__ == "__main__":
    main()
