#!/usr/bin/env python3
"""! @brief A divide and conquer algorithm
The karatsuba divide and conquer algorithm uses three recursive calls for 
integer multiplication.
input is a list positive integers, x and y.
output the product of x,y using recursion
the len(x,y) is assume to be a power of 2.

"""
import math
# @file karatsuba.py
def karatsuba(x,y):
    # initialize the len of x, assume x is even
    n = len(x)
    # base case if n== 1
    if n == 1:
        return x[0] * y[0]
    # initialize variable p-list 
    p = [] 
    # initialize variable p-list 
    q = []
    #divides x,y into n/2 elements each, a,b,c,d
    a = [int(str(x[0]) + str(x[1]))]
    b = [int(str(x[2]) + str(x[3]))]
    c = [int(str(y[0])+ str(y[1]))]
    d = [int(str(y[2]) + str(y[3]))]
    # makes two calls to sum, ab and cd
    t = sum(a + b)
    m = sum(c + d)
    # makes two append, constant time
    p.append(t)
    q.append(m)
    #three recursive calls for each n/2 pair to perform n^2 multiplication
    ac = karatsuba(a,c)
    bd = karatsuba(b,d)
    pq = karatsuba(p,q)
    #variable for subtracting the sums
    adbc = pq - ac - bd
    #T(n) = 3T((n/2) + n^2)
    ans = math.floor((math.pow(10,4) * ac) + ((math.pow(10,2)) * adbc) + bd)
    return ans

r = [5,6,7,8]
i = [1,2,3,4]
w = karatsuba(r,i)
print(w)

