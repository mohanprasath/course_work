# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 21:57:08 2019

@author: Krisna
"""
#import math
#
for i in range(1, 20):
    m = i
    n = i
    print(math.factorial(m+n)/(math.factorial(m)* math.factorial(n)) - m*n)
    
#def factorial(n):
#    result = 1
#    for i in range(1, n + 1):
#        result *= i
#    return result
#
#def paths(w, h):
#    return factorial(w + h) / (factorial(w) * factorial(h))

#missing = [
#  [0, 1],
#  [0, 0],
#  [0, 0],
#]
#
#def paths_helper(x, y, path_grid, missing):
#  if path_grid[x][y] is not None:
#    return path_grid[x][y]
#
#  if missing[x][y]:
#    path_grid[x][y] = 0
#    return 0
#  elif x < 0 or y < 0:
#    return 0
#  else:
#    path_count = (paths_helper(x - 1, y, path_grid, missing) +
#                  paths_helper(x, y - 1, path_grid, missing))
#    path_grid[x][y] = path_count
#    return path_count
#
#def paths(missing):
#  arr = [[None] * w for _ in range(h)]
#  w = len(missing[0])
#  h = len(missing)
#  return paths_helper(w, h, arr, missing)
#
#print paths()

from math import factorial, pow
for grid in range(1, 20):
    print(int(factorial(2 * grid) / pow(factorial(grid), 2))- grid * grid)