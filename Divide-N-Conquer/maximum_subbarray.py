import math
import sys   
def find_max_crossing_subarray(A, low, mid, high):
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
    for  j in range(max_left, high):
        sum += A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j 
    return (A[max_left: max_right + 1], left_sum + right_sum)


def find_maximum_subarray(A, low, high):      
    if high == low:
        return A
    mid = int(math.floor(low + high)/2) 
    left_sum = sum(A[low:mid])
    right_sum = sum(A[mid + 1: len(A)])
    cross_sum = sum(A[low:len(A)])
    
    left_low, left_high, left_sum =  find_maximum_subarray(A, low, mid)
    (right_low, right_high, right_sum)  = find_maximum_subarray(A, mid + 1, high)
    (cross_low, cross_high, cross_sum1, cross_sum2)  = find_max_crossing_subarray(A, low, mid, len(A))
    
    if left_sum >= right_sum and left_sum >= cross_sum1:
        return (left_low,left_high,left_sum)
    elif right_sum >= left_sum and right_sum >= cross_sum2:
        return right_low, right_high, right_sum + 1
    else:
        return cross_low, cross_high, cross_sum1 + cross_sum2


A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
high = len(A)
low = 0
mid = A[low:high//2]
x = find_maximum_subarray(A, low, high)
print(x)