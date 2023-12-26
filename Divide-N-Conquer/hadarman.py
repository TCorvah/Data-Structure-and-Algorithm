#!/usr/bin/env python3
"""! @brief Hadarman  Matrix product using Divide and Conquer
The following is an nxn hadarman matrix using only 1 and -1
The input is a single vector of length n, and returns an nxn matrix
with  -1 at the last row, column for each length of the input vector and 1 everywhere.
The following is a divide and conquer implementation of hadarman.  Given an input vector
the matrices are partition into 4 equal sizes.
There are two base cases for when n is 1 or 2.
Total runtime is O(NlogN)
"""
import math
import numpy as np
# @file hadarman.py
def hadarman(v):
    """! The following is an implementation of the hadarman matrix where the elements 
    are mapped to the list [0,1] for the rows, columns of the matrix.
    @param v  A single vector of length n
    @return  a hadarman matrix of size nxn
    """
    n = len(v)
    a = [0,1]
    a1 = a[1] * a[0] + a[1]
    a2 = a[1] * a[1] + a[0]
    a3 = a[1] * a[1] - a[0]
    a4 = a[1] * a[0] - a[1] 
    H0 = np.array([[a1,a2],[a3,a4]])
    
    if n == 1:
        return np.array(a1)  
    if n == 2:  
       return H0
    row, col = n , n 
    C = [ [i for i in range(row)] for j in range(col)]    
    H = np.array(C)
    c,r = row//2, col//2 
    h11 =  H[:c, :r] 
    h12 =  H[:c, r:] 
    h21 =  H[c:, :r] 
    h22 =  H[c:, r:] 
    p1 = hadarman([a1,a2])
    p2 = hadarman([a3,a4])
    h11 = p1
    h12 = p2
    h21 = p1
    h22 = -1 * p1
    H = np.vstack((np.hstack((h11, h12)), np.hstack((h21, h22))))  
    return H

a = [1,8,4,6]
q = hadarman(a)
print(q)
