#!/usr/bin/env python3
"""! @brief A divide and conquer algorithm
The Divide step partition the subarray using the last element
in the array as the pivot
which takes constant time with a pivot for comparison o(nlgn).
The conquer step recursively sorts the subarray through recursion
The combine step never combine anything but returns the sorted array"""

##
#  @mainpage  subroutine merges two sorted sub array into one using linear time O(n)
#
#  @section quicksort sorts recursively sorts the element in the  subarray
#  @section notes_main runtime O(nlgn)
#  -  Runs in O(nlgn) time for best case and O(n^2) for worst case.
from random import randrange
from random import sample

def quick_sort(A, p, r):   
    if p < r:
        j = random_pivot(A,p,r)
        quick_sort(A, p, j - 1 )
        quick_sort(A, j + 1, r) 
 
"""! helper function randomize the pivot with the following subroutine
the runtime for the following is O(n), as it retuns partition
"""       
def random_pivot(A, p, r):
    x = randrange(p,r)
    A[r], A[x], =  A[x], A[r]
    return partition(A, p, r)
    
  
  
def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r): 
        if A[j] <= x:
            i += 1
            A[i],A[j] = A[j],A[i]
            j += 1
    A[i + 1], A[r] = A[r], A[i + 1]         
    # The line `print(A[i + 1])` is printing the value of the pivot element after it has been placed in
    # its correct position in the array.
    return i + 1
         
    

def main():
    """!    Main program entry. """
    A = [5,4,1,8,7,2,6,3]
    n = len(A)
    quick_sort(A,0, n - 1)
    print(A)

if __name__ == "__main__":
     # The `main()` function is the entry point of the program. It is called when the script is run. In
    # this case, it calls the `merge_sort()` function with a list `x` and
    #  then prints the result in sorted order.
    main()


