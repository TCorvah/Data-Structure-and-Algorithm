#!/usr/bin/env python3
"""! @brief A divide and conquer algorithm
The karatsuba divide and conquer algorithm uses three recursive calls for 
integer multiplication.
input is a list positive integers, x and y.
output the product of x,y using recursion
the len(x,y) is assume to be a power of 2.

"""
import math

def karatsuba(x,y):
    n = len(x)
    if n == 1:
        return x[0] * y[0]
    p = []
    q = []
    a = [int(str(x[0]) + str(x[1]))]
    b = [int(str(x[2]) + str(x[3]))]
    c = [int(str(y[0])+ str(y[1]))]
    d = [int(str(y[2]) + str(y[3]))]
    t = sum(a + b)
    m = sum(c + d)
    p.append(t)
    q.append(m)
    ac = karatsuba(a,c)
    bd = karatsuba(b,d)
    pq = karatsuba(p,q)
    adbc = pq - ac - bd
    ans = math.floor((math.pow(10,4) * ac) + ((math.pow(10,2)) * adbc) + bd)
    return ans

r = [5,6,7,8]
i = [1,2,3,4]
w = karatsuba(r,i)
print(w)

