#!/usr/bin/env python3
"""! @brief A divide and conquer algorithm
The maximum subarray problem uses a divide and conqueur technique.
To find a maximum subarray in an array, we divide the subarray into two subarray,
with the claim that the maximum subarray must lie in the left half of the array,
the right half of the array or the point that crosses divide the leftv and right half.
The conquer step recursively solves two subproblem on len(n/2) of maximum sum. 
the indices lies in either the left or right half or the mid point crossing.
"""

##
#  @mainpage  subroutine max_crossing subarray,takes an input array, with indices of
# low, mid and high and returns a sublist that contains the maximum array and the sum. 
# this implementation uses linear time O(n)
#
#  @section find_maximum_subarray returns a tuple that demarcates the maximum a maximum subarray
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
    """
          
    if len(A) <= 1:
        return A
    low = 0
    high = len(A)
    mid = int(math.floor(low + high)/2) 
    sub1 = A[0:mid]
    sub2 = A[mid:len(A)]
    cross_mid = A[low:high//2]
    left =  find_maximum_subarray(sub1)
    right = find_maximum_subarray(sub2) 
    cross =  find_max_crossing_subarray(A, low, mid, high) 
    left_sum  = sum(sub1)
    righ_sum = sum(sub2)
    cross_sum = sum(cross_mid)
    if left_sum >= righ_sum and left_sum >= cross_sum:
        return (left, left_sum)
    elif righ_sum >= left_sum and righ_sum >= cross_sum:
        return (right, righ_sum)
    else:
        return (cross, cross_sum)
    

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
        max_left = mid - low 
        for i in range(max_left, low):
            sum += A[i]
            if sum  > left_sum:
                left_sum = sum
                max_left = i 
        right_sum = -1
        sum = 1
        max_right = max_left
        for  j in range(max_left, high):
            sum += A[j]
            if sum > right_sum:
                right_sum = sum
                max_right = j 
        return (A[max_left: max_right + 1], left_sum + right_sum) 




A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
high = len(A)
x = find_maximum_subarray(A)
print(x)