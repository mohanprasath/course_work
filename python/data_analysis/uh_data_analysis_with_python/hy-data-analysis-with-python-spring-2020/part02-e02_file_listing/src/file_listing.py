#!/usr/bin/env python3

import re
import os
import sys
import calendar

def file_listing(filename="src/listing.txt"):
    """

    Required Output: (25399, "Nov", 2, 21, 25, "exception_hierarchy.pdf")
    """
    result = []
    path = os.path.dirname(os.path.realpath(__file__))
    with open(path[:-3]  + filename, 'r') as infile:
        for line in infile:
            # -rwxr-xr-x 1 jttoivon hyad-all    2356 Dec 11 11:50 add_colab_link.py
            # file_access, count, user_name, group, file_size, month, date, time, file_name = line.split(" ")
            months = "|".join(calendar.month_abbr[1:])
            parts = re.findall(r"hyad-all\s+(\d+)\s+(%s)\s+(\d+)\s+(\d{2}):(\d{2}) (.+)" % months, line)[0]
            result.append(tuple(int(part) if part.isdigit() else part for part in parts))
    return result

def main():
    print(file_listing())

if __name__ == "__main__":
    main()
