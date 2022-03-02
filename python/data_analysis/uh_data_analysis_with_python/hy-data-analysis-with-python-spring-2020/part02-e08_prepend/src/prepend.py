#!/usr/bin/env python3

class Prepend(object):
    # Add the methods of the class here
	def __init__(self, some_string):
		self.text = some_string

	def write(self, new_string):
		print(self.text + new_string)

def main():
	p = Prepend("+++ ")
	p.write("Hello");

if __name__ == "__main__":
    main()
