#!/usr/bin/env python3

import numpy as np
import numpy.linalg as la
from numpy import (array, dot, arccos, clip)
from numpy.linalg import norm

def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def vector_angles(X, Y):
    result = np.empty(X.shape[0])
    for i in range(X.shape[0]):
        v1 = X[i,:]
        v2 = Y[i,:]
        print(v1, v2)
        u = v1
        v = v2
        c = dot(u,v)/norm(u)/norm(v) # -> cosine of the angle
        angle = arccos(clip(c, -1, 1))
        v1_u = unit_vector(v1)
        v2_u = unit_vector(v2)
        print(np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0)), angle)
        result[i] = np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))
        result[i] = np.rad2deg(angle)
    return result
    
def main():
    A=np.array([[0,0,1], [-1,1,0]])
    B=np.array([[0,1,0], [1,1,0]])
    print(vector_angles(A, B))

if __name__ == "__main__":
    main()
