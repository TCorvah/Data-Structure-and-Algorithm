import math



def find_maximum_subarray(A):      
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