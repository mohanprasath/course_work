#!/usr/bin/env python3

def reverse_dictionary(d):
    result = {}
    for key, value in d.items():
        for i in range(len(value)):
            if value[i] not in result.keys():
                result[value[i]] = [key]
            else:
                existing = result[value[i]]
                existing.append(key)
                result[value[i]] = existing
    return result

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))

if __name__ == "__main__":
    main()
