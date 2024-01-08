#!/usr/bin/env python3
"""! @brief A divide and conquer randomize  algorithm
The random pivot subroutine uses uniform random distribution to choose the pivot and return the partition
subroutine as output.
The main algorithm rselect, take in an input array and an interger i and return the ith order statistic of 
an array element chosen by the user.
Runs in O(n) time for best case and O(n^2) for worst case.
"""
from quicksort import random_pivot
import random

# @file rselect.py
def rselect(A,i):
    r = len(A)
    p = 0
    if p == r:
        return A[p]
    s = random_pivot(A,p,r-1)
    j =  s - p + 1
    s1 = A[p:s-1]
    s2 = A[s:r]
    if j == i:
        return A[s]
    elif j > i:
        return rselect(s1, i)
    else:  
        return rselect(s2,i-j)
    
    
A = [6,8,9,2]
i = 3
n = len(A)
print(rselect(A,i))

