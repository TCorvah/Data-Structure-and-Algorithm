#!/usr/bin/env python3
"""! @brief A Randomize Algorithm
The following algorithmn randomly permute an array by mapping an array to a priority
and returning a new list of the one to one mapping of two arrays, with one containing priorities as keys 
and the other array as values . The procedure produces a uniform random permutaion, as each random generated numbers are
equally likely to be a priority.
total runtime is O(N)
"""
import math
import random
# @file permute_by_sorting.py
def permute_by_sorting(A):
    n = len(A)
    p = [0 for i in range(n)]
    assert len(A) == len(p)
    map_index = {}
    permutaion_lst= []
    for i in range(n):
        p[i] = random.randrange(i, n**3 - 1)
        map_index[p[i]] = A[i]
        
    sorted_lst = sorted(map_index.items())
    for i,j in sorted_lst:
        permutaion_lst.append(j)   
        
    return sorted_lst, permutaion_lst
        
          
        
A = [1,2,3,4]
c = permute_by_sorting(A)
print(c)