#!/usr/bin/env python3

def transform(s1, s2):
    if len(s1) > 0 and len(s2)>0:
        zip_result = list(zip(s1.split(" "), s2.split(" ")))
        return list(map(lambda entry: int(entry[0]) * int(entry[1]), zip_result))
    return []

def main():
    pass

if __name__ == "__main__":
    main()
