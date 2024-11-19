import math
import random


# @file quick_sort.py
def quicksort_median(A, p, r):   
    if p < r:
        i = choose_pivot(A, p,r)
        quicksort_median(A, p, i - 1 )
        quicksort_median(A, i + 1, r) 
        
        
def choose_pivot(A, p, r):
    """! 
    @param A and it's left and right endpoints
    @return an index of a uniformly random pivot
    """ 
    mid = int(math.floor(( p + r) /2))
    A[p], A[mid], =  A[mid], A[p]
    return partition(A, p, r)
        
   

# @file subroutine partition.py 
def partition(A, p, r):
    """! partitions subarray elements around the last element as pivot
    @param A,p,r distinct array with it's left and right indices as endpoints.
    @return  an index of the pivot element.
    """  
    x = A[p]
    i = p + 1
    for j in range(p+1, r): 
        if A[j] < x:
            A[j],A[i] = A[i],A[j]
            i += 1
    A[i - 1], A[p] = A[p], A[i - 1]         
    return i - 1
            
        
            
            
        




        
A = [5,4,1,8,7,2,6,3]
n = len(A)
quicksort_median(A, 0, n - 1)
print(A)