#!/usr/bin/env python3
import re

def integers_in_brackets(s):
    nums = re.findall(r"\[[\s]*([+|-]{0,1}\d+)[\s]*\]", s)
    result = []
    return [int(num) for num  in nums]

def main():
    print(integers_in_brackets("  afd [asd] [12 ] [a34]  [ -43 ]tt [+12]xxx"))

if __name__ == "__main__":
    main()
