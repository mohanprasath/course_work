#!/usr/bin/env python3
import sys
import os
import numpy as np

def summary(filename):
    """
    Required Output:
    File: src/example.txt Sum: 51.400000 Average: 10.280000 Stddev: 8.904606
    """
    new_file_name_and_path = os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)
    values = []
    with open(filename, 'r') as infile:
        for line in infile:
            try:
                num = float(line)
                values.append(num)
            except:
                continue
    return (sum(values), np.average(values), np.std(values, ddof=1))

def main():
    files =  sys.argv[1:]
    for file in files:
        file_summary = summary(file)
        print("File: {} Sum: {:.6f} Average: {:.6f} Stddev: {:.6f}".format(file, file_summary[0], file_summary[1], file_summary[2]))

if __name__ == "__main__":
    main()
