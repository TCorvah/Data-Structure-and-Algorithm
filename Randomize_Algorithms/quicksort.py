#!/usr/bin/env python3
"""! @brief A divide and conquer randomize  algorithm
The partition subroutine, uses the last element in the array as the pivot and return the index
The random pivot subroutine uses uniform random distribution to choose the pivot and return the partition
subroutine as output.
The main algorithm quicksort, take in the array as input, makes a call to the random pivot
subroutine and recursively sorts the array based on the random pivot chosen.
Runs in O(nlgn) time for best case and O(n^2) for worst case.
"""
import random
# @file quick_sort.py
def quick_sort(A, p, r):   
    if p < r:
        j = random_pivot(A,p,r)
        quick_sort(A, p, j - 1 )
        quick_sort(A, j + 1, r) 
 
"""! The below subroutine randomize the pivot element in a uniform random fashion
the runtime for the following is O(n), as it retuns partition
"""       
def random_pivot(A, p, r):
    """! 
    @param A and it's left and right endpoints
    @return an index of a uniformly random pivot
    """  
    x = int(random.uniform(p,r))
    A[r], A[x] =  A[x], A[r]
    return partition(A, p, r)
    
  
# @file subroutine partition.py 
def partition(A, p, r):
    """! partitions subarray elements around the last element as pivot
    @param A,p,r distinct array with it's left and right indices as endpoints.
    @return  an index of the pivot element.
    """  
    x = A[r]
    i = p - 1
    for j in range(p, r - 1): 
        if A[j] <= x:
            i += 1
            A[i],A[j] = A[j],A[i]
            j += 1
    A[i + 1], A[r] = A[r], A[i + 1]         
    return i + 1
         
    

def main():
    """!    Main program entry. """
    A = [5,4,1,8,7,2,6,3]
    n = len(A)
    quick_sort(A,0, n - 1)
  

    
    


if __name__ == "__main__":
     # The `main()` function is the entry point of the program. It is called when the script is run. In
    # this case, it calls the `merge_sort()` function with a list `x` and
    #  then prints the result in sorted order.
    main()



