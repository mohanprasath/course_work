#!/usr/bin/env python3
import numpy as np

def try_except_block(string):
    try:
        return int(string)
    except ValueError:
        try:
            return float(string)
        except ValueError:
            return None
    return None

def extract_numbers(s):
    result = []
    for string in s.split():
        temp = try_except_block(string)
        if temp:
            result.append(temp)
    return result

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
