#!/usr/bin/env python3

def distinct_characters(L):
    result = {}
    for entry in L:
        result[entry] = len(''.join(set(entry)))
    return result

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
