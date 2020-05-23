#!/usr/bin/env python3

def interleave(*lists):
    combined = []
    for entry in zip(*lists):
        combined.extend(list(entry))
    return combined

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
