#!/usr/bin/env python3
"""! @brief A divide and conquer algorithm that uses subroutine merge to as a helper for merge sort"""
    
## 
#  @mainpage  subroutine merges two sorted sub array into one using linear time O(n)
#
#  @section mergeSort sorts the recursively sorts the element in the  subarray
#  @section notes_main runtime O(nlgn)
#  -  Runs in nlgn time for worst and best case.

##
# @file merge_sort.py
def mergeSort(A):
    """! Sorts the elements in an array in a bottom up fashion 
    there are two recursive calls made in merge sort 0(lgn)
    @param A  The unsorted sequence of integers in the array
    
    @return  a sorted output using merge subroutine in O(nlgn) time complexity
    """
    if len(A) <= 1:
        return A
    mid = len(A)//2
    sub1 = A[0:mid]
    sub2 = A[mid:len(A)]
    x = mergeSort(sub1)
    y = mergeSort(sub2)
    return merge(x,y)


def merge(L,R):
    """! The merge subroutine makes  comparison between the two subarray and 
         copies the smaller element in the list
    @param A  The unsorted sequence of integers in the array
    
    @return  a merge output of the two subarray in O(n) time complexity, 
    
    """  
    arr = []
    i = 0
    j = 0
    while i != len(L) and j != len(R):
        if L[i] <=  R[j]:
            arr.append(L[i])
            i += 1
        else:      
            arr.append(R[j])
            j += 1
    for k in range(i, len(L)):
        arr.append(L[k])
        
    for k in range(j, len(R)):
        arr.append(R[k])
    return arr


def main():
    """!    Main program entry. """

    A = [5,4,1,8,7,2,6,3]
    print(mergeSort(A))
    
if __name__ == "__main__":
     # The `main()` function is the entry point of the program. It is called when the script is run. In
    # this case, it calls the `merge_sort()` function with a list `x` and 
    #  then prints the result in sorted order.
    main()  


