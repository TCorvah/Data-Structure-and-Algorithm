#!/usr/bin/env python3

"""! @brief A sorting Algorithm, that repeated swap adjacent elements
that are out of order.
The sorting algorithm has the worst case runtime of O(n^2) as it makes two n passes for comparison
"""

def bubble_sort(A):
    for i in range(0,len(A)-1):
        k = i + 1
        for j in range(k, len(A)):
            if A[j] < A[i - 1]:
                A[i-1],A[j] = A[j], A[i-1]
    return A
        


s = [5,4,1,8,7,2,6,3]
print(bubble_sort(s))