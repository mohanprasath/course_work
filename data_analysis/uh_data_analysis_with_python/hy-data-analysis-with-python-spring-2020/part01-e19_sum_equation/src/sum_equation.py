#!/usr/bin/env python3

def sum_equation(L):
    length = len(L)
    if length == 0:
        return "0 = 0"
    else:
        total = sum(L)
        result = ""
        for counter, entry in enumerate(L):
            if counter < length-1:
                result += str(entry) + " + "
            else:
                result +=  str(L[-1]) + " = " + str(total)
        return result

def main():
    print(sum_equation([1,5,7]))

if __name__ == "__main__":
    main()
