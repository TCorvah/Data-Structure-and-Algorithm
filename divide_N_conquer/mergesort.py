#!/usr/bin/env python3
"""! @brief A divide and conquer algorithm
The Divide step in the algorithm evenly splits the array into two halves
which takes constant time.
The conquer step recursively solves two subproblem on len(n/2) which takes O(lgn)
The combine step uses the merge subroutine to combine the elements in increasing order in O(nlgn)"""

##
#  @mainpage  subroutine merges two sorted sub array into one using linear time O(n)
#
#  @section mergeSort sorts the recursively sorts the element in the  subarray
#  @section notes_main runtime O(nlgn)
#  -  Runs in nlgn time for worst and best case.

##
# @file merge_sort.py
def mergeSort(A):
    """! 
     Sorts an array using the Merge Sort algorithm.
    
    Args:
        A (list): The unsorted sequence of integers.

    Returns:
        list: A sorted array in ascending order.

    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    # test case if the list is empty 
    if len(A) <= 1:
        return A
    #divide into two for partititioning
    mid = len(A)//2
    
    #all items from begining of array up to the mid
    sub1 = A[0:mid]
    
    #all items from mid to the end of array
    sub2 = A[mid:len(A)]
    
    # sort the left side recursively
    left_side = mergeSort(sub1)
   
    # sort the right side recursively 
    right_side  = mergeSort(sub2)
    
    #return the merge array
    return merge(left_side,right_side)


def merge(L,R):
    """! Merges two sorted subarrays into one sorted array.
    
    Args:
        L (list): First sorted subarray.
        R (list): Second sorted subarray.

    Returns:
        list: A merged sorted array.
        
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    merged_arr = []
    i = j =  0
    while i < len(L) and j <  len(R):
        if L[i] <=  R[j]:
            merged_arr.append(L[i])
            i += 1
        else:
            merged_arr.append(R[j])
            j += 1
    # Append any remaining elements
    for k in range(i, len(L)):
        merged_arr.append(L[k])

    for k in range(j, len(R)):
        merged_arr.append(R[k])
    return merged_arr

def main():
   """Main function for testing the Merge Sort algorithm."""

   A = [5,4,1,8,7,2,6,3]
   print("Unsorted Array:", A)
   sorted_array = mergeSort(A)
   print("Sorted Array:", sorted_array)

if __name__ == "__main__":
     # The `main()` function is the entry point of the program. It is called when the script is run. In
    # this case, it calls the `merge_sort()` function with a list `x` and
    #  then prints the result in sorted order.
    main()