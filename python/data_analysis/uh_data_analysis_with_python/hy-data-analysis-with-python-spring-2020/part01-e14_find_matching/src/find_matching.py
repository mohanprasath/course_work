#!/usr/bin/env python3

def find_matching(L, pattern):
    result = []
    for counter, entry in enumerate(L):
        if pattern in entry:
            result.append(counter)
    return result

def main():
    find_matching(["sensitive", "engine", "rubbish", "comment"], "en")

if __name__ == "__main__":
    main()
