#!/usr/bin/env python3
"""! 
@brief Hadamard Matrix product using Divide and Conquer.

This script generates an \( n \times n \) Hadamard matrix, where elements 
are either \( 1 \) or \( -1 \). The Hadamard matrix is constructed recursively 
using the divide-and-conquer approach. 

- The input is assumed to define the size of the matrix as a power of 2.
- The base cases handle matrices of size \( 1 \times 1 \) and \( 2 \times 2 \).
- Total runtime is \( O(n \log n) \).

Usage:
    Call the `hadamard` function with the size or a vector representing the desired matrix order.
"""

import numpy as np

# @file hadamard
def hadamard(v):
    """!
    Constructs a Hadamard matrix using a divide-and-conquer approach.
    
    Args:
        v (list): Input vector defining the matrix order. 
                                The length must be a power of 2.

    Returns:
        numpy.ndarray: An \( n \times n \) Hadamard matrix.
        
    Space  Complexity:
        O(N^2) due to the storage of the matrix
    
    Time Complexity:
        O(nlogn) due to the recursive division and merging of submatrices.
    
    """
    # I use a vector as input, this was my own way of implemenatation as I could not find it in a book
    n = len(v)

    a = [0,1]
    
    #the following was my own implemtation to understand the array 
    a1 = a[1] * a[0] + a[1]
    a2 = a[1] * a[1] + a[0]
    a3 = a[1] * a[1] - a[0]
    a4 = a[1] * a[0] - a[1] 
      
    H0 = np.array([[a1,a2],[a3,a4]])

    # Ensure the input length is a power of 2
    # hadarman matrix works on only power of two, n not
    if not (n and (n & (n - 1)) == 0):
        raise ValueError("Length of the input vector must be a power of 2.")
    
    # Base cases
    if n == 1:
        return np.array([[1]])  # 1x1 matrix with a single element
    
    if n == 2:
        return H0 # 2x2 Hadamard matrix
    
     # Recursive step: split into quadrants
    mid = n // 2
    top_left = hadamard(v[:mid])
    top_right = top_left  # Identical to top_left
    bottom_left = top_left  # Identical to top_left
    bottom_right = -top_left  # Negated top_left
    
    # Combine quadrants into a full matrix
    top = np.hstack((top_left, top_right))
    bottom = np.hstack((bottom_left, bottom_right))
    return np.vstack((top, bottom))


# Example usage
if __name__ == "__main__":
    # Define the input as a vector with length being a power of 2
    a = [1, 2,3,4]  # Length of this vector defines the matrix order
    # Generate the Hadamard matrix
    result = hadamard(a)
    print(result)
 
