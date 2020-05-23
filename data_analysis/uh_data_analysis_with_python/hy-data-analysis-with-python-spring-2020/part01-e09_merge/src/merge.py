#!/usr/bin/env python3

def merge(L1, L2):
    temp = []
    for list_entry in [L1, L2]:
        for entry in list_entry:
            temp.append(entry)
    sorted_temp = []
    while len(temp) > 0:
        min_item = min(temp)
        temp.remove(min_item)
        sorted_temp.append(min_item)
    return sorted_temp

def main():
    merge([1, 2, 3], [4, 5])

if __name__ == "__main__":
    main()
