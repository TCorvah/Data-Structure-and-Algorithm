import math
from merge_sort import mergeSort


def select_median(A, i):
    #base case
    p = 0
    r = len(A)
    if p == r:
        return A[p]
    pivot = choose_pivot(A)
    k = pivot - p + 1
    p1 = A[p:pivot]
    p2 = A[pivot+1:r]
    if k == i:
        return A[k]
    elif k > i:
        return select_median(p1, i)
    else:
        return select_median(p2, i - k - 1)   
    
    
def getPartition(A, mid):
    #use binary search stragety
    #search for median and all number greater than median on right of j
    #less than median on left of j
    # return mid index
    p = 0
    r = len(A) - 1
    j = 0
    while j <= r:
        if A[j] < mid:
            A[p], A[j] = A[j], A[p]
            p += 1
            j += 1
        elif A[j] > mid:
            A[j], A[r] = A[r], A[j]
            r = r - 1
        else:
            j += 1
    return p 
   

          
    
def divide_n_Sortlst(A):
    #return lst of lst of 5, as sorted(mergesort)
    group_five = [A[i:i+5] for  i in range(0, len(A), 5)]
    median_lst = [mergeSort(a)[len(a)//2] for a in group_five]
    return median_lst


        
def choose_pivot(A):
    p = 0
    idx = 0
    r = len(A)//2
    x = divide_n_Sortlst(A)
    mid = x[len(x)//2]
    for i in range(0,len(A)):
        if A[i] == mid:
            idx = i 
        A[r], A[idx], =  A[idx], A[r]       
    return getPartition(A,r)



#A = [25,21,98,100,76,22,43,60,89,87]
A = [2, 8, 13, 10, 4, 1, 16, 11, 3, 18, 5, 17, 7, 14, 12]
n = 4
h = select_median(A, n)
print(h)



