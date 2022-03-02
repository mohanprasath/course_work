#!/usr/bin/env python3
import sys
import os
import re

def read_file(filename):
    lines = []
    new_file_name_and_path = os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)
    with open(filename, 'r') as infile:
        return infile.read()

def count_words(lines):
    words = []
    count = {}
    for word in re.split(r'\s', lines)[0:-2]:
        words.append(word.strip("""!"#$%&'()*,-./:;?@[]_""").strip('"[],.:?!').rstrip(",").rstrip("."))
    for word in words:
        if word in count.keys():
            val = count[word]
            val += 1
            count[word] = val
        else:
            count[word] = 1
    return count
    

def word_frequencies(filename):
    lines = read_file(filename)
    count = count_words(lines)
    return count

def main():
    word_frequencies("alice.txt")

if __name__ == "__main__":
    main()
