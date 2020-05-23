#!/usr/bin/env python3
import sys
import os
import re

def read_file(filename):
	with open(filename, 'r') as infile:
		return infile.readlines()

def file_count(filename):
	"""
	for each file given we are to count the number of lines, words, and characters in the file
	"""
	characters = []
	words = []
	lines = read_file(filename)
	for line in lines:
		characters.append(len(line))
		words.append(len(line.split()))
	return (len(lines), sum(words), sum(characters))

def main():
    files =  sys.argv[1:]
    for file in files:
        linecount, wordcount, charcount = file_count(file)
        print("{}\t{}\t{}\t{}".format(linecount, wordcount, charcount, file))

if __name__ == "__main__":
    main()
