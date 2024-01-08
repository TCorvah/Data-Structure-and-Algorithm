#!/usr/bin/env python3
"""! @brief Strassen Matrix multiplication using Divide and Conquer
Strassen devise a stragety to limit the number of multiplication of
matrices from 8 to 7,  by carefully choosing columns , rows to add or subtract.
7 recursive calls are made for the dot product and result added to the return C matrix

Inputs are two matrices with even lengths, and return a runtime of O(N^log2^7)
"""
import math
import numpy as np


 # @file  strassen_matrix_multiplication.py   
def strassen_matrix_multiplication(a,b): 
    """! partition each matrix by blocks of 4 and uses 
    7 mathematical operation instead of 8.
    @param two 2^n matrices 
    @return a block matrice C, with a runtime of 0(N^2.8)
    """  
    n = a.shape[0]
    if n == 1:
        return np.dot(a, b)
     
    #a matrice partition into 4 
    row, col = a.shape
    x,y = row//2, col//2  
    a11  = a[:x,:y]
    a12 =  a[:x, y:]
    a21 =  a[x:, :y]
    a22 =  a[x:, y:]
    
    #b matrice partition into 4 
    brow, bcol = b.shape
    c,w = brow//2, bcol//2
    b11 =  b[:c, :w]  
    b12 =  b[:c, w:]
    b21 =  b[c:, :w]
    b22 =  b[c:, w:]
    
    # matrice product of a,b 
    p1 = strassen_matrix_multiplication(np.add(a11,a22),np.add(b11,b22))
    p2 = strassen_matrix_multiplication(np.add(a21,a22),b11) 
    p3 = strassen_matrix_multiplication(a11, np.subtract(b12,b22))
    p4 = strassen_matrix_multiplication(a22,np.subtract(b21,b11))
    p5 = strassen_matrix_multiplication(np.add(a11,a12),b22) 
    p6 = strassen_matrix_multiplication(np.subtract(a21,a11),np.add(b11,b12))
    p7 = strassen_matrix_multiplication(np.subtract(a12,a22), np.add(b21,b22))
    
    # blocks of c matrix
    c11 = p1 + p4 - p5 + p7
    c12 = p3 + p5
    c21  = p2 + p4
    c22 = p1 - p2 + p3 + p6
    C = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22)))) 
    return C
    

A = np.array([
     [1,1,1,1],
     [2,2,2,2],
     [3,3,3,3],
     [2,2,2,2]
     ])
B = np.array(
    [
        [1,1,1,1],
        [2,2,2,2],
        [3,3,3,3],
        [2,2,2,2]
     ])


x = strassen_matrix_multiplication(A,B)
print(x)
