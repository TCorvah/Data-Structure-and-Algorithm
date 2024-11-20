#!/usr/bin/env python3
"""! @brief A divide and conquer algorithm
The maximum subarray problem uses a divide and conqueur technique.
To find a maximum subarray in an array, one of the follwing has to happen,
the maximum subarray is either in the subarray A[low..mid], so that low<=i<=j<=mid,
the maximum subarray is either in the subarray A[mid+1..high], so that mid<i<=j<=high,
the maximum subarray is either in the subarray A[low..high], which crosses the mnid point
"""

##
#  @mainpage  subroutine max_crossing subarray,takes an input array, with indices of
# low, mid and high and returns a sublist that contains the maximum subarray that crosses the midpoint. 
# this implementation uses linear time O(n)
#
#  @section find_maximum_subarray  returns a tuple that demarcates the maximum a maximum subarray
#  along with the sum of values in a maximum subarray.
#  @section notes_main runtime O(nlgn + n)
#  

##
# @file find_maximum_subarray.py
import math
def find_maximum_subarray(A):
    """! maximum_subarray uses a divide and conqueuer approach to
    find the indices that demarcates a maximum subarray
    when n = <= 1, the base case returns the list
    When n > 1, 
    The divide part is implemented in as mid, where we take the floor 
    of the lowest and highest index in the array.
    We create two subarray and recursively finding the left and right maximum 
    subarray.   
    @param A  the list containing the array to be divided.

    @return  a maximum subarray  with indices of the maxim sub in a array.
    
    Time Complexity: 
    O(nlogn)
    
    Space Complexity: 
    O(logn)
    """
    low = 0
    high = len(A) 
    
    if len(A) <= 1:
        return A 
    
    mid = high//2  
    left_array = A[low:mid] 
    right_array = A[mid+1:high] 
    cross_array = A[low:high]
    
    left = find_maximum_subarray(left_array)  
    right = find_maximum_subarray(right_array)      
    cross = find_max_crossing_subarray(A, low, mid-1, high-1)
  
    left_sum = sum(left_array)
    right_sum = sum(right_array)
    cross_sum = sum(cross_array)
    
    if left_sum >= right_sum and left_sum >= cross_sum:
        return (left)
    elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right)
    else:
            return (cross)
    

# @file find_max_crossing_subarray.py
def find_max_crossing_subarray(A, low, mid, high):
    """_summary_ The max crossing sub array finds a maximum crossing
        subarray that crosses the mid point in linear time.

    Args:
        A (_type_): _description_ The array of integers to find max crossing
        low (_type_): _description_ The lowest index of array A
        mid (_type_): _description_ the mid point of array A
        high (_type_): _description_ The highest index or total len of the array

    Returns:
        _type_: _description_ A subarray that contains the maximum subarray
                with the sum of the maximum elements.
    """
    left_sum = -1
    sum = 0
    max_left = mid 
    for i in range(mid, low - 1, -1):
        sum += A[i]
        if sum  > left_sum:
            left_sum = sum 
            max_left = i 
    right_sum = -1
    sum = 0
    max_right = mid + 1
    for  j in range(mid + 1, high + 1):
        sum += A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j 
    return (max_left, max_right, left_sum + right_sum)




A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
x = find_maximum_subarray(A)
#x = find_maximum_subarray(A)
print(x)