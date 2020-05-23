# Enter you module contents here
"""
Written as an exercise module for a UH Course
"""
import math

__author__ = "Author MPC"
__version__ = "0.1"

def hypothenuse(a, b):
	"""
	Returns hypothenuse of a right angled triangle given length of two sides.
	"""
	return math.sqrt(a ** 2 + b ** 2)

def area(a, b):
	"""
	Returns area of a right angled triangle given length of two sides.
	"""
	return a * b / 2