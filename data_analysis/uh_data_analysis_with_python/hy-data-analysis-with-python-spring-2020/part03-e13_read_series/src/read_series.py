#!/usr/bin/env python3
import pandas as pd
import re

def read_series():
    print("Enter the index followed by the data(whitespace separator):")
    data = {}
    while(True):
        line = input("Enter the index followed by the data(whitespace separator):")
        if line == "":
            break
        try:
            key, value = line.split()
            data[key] = value
        except ValueError:
            continue
    return pd.Series(pd.Series(list(data.values()), index=list(data.keys())))

def main():
    read_series()

if __name__ == "__main__":
    main()
