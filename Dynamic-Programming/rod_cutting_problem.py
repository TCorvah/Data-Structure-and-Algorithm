import math
"""_summary_ The following uses dynamic programming to solve the rod-cutting
    problem. The code utilizes a bottom up method that enforces ordering
"""

def rod_cut(price, m): 
    """! a bottom up implementation of the rod cutting problem 
        that enforces natural ordering on each subproblem.
        the runtime of this code snippet is O(n)^2 as it iterates twice
        for each i,j in n.
        @param the price and length of the array n 
        @return The value of an optimal solution
    """    
    revenue = [0 for i in range(m + 1)]
    revenue[0] = 0
    for j in range(1,m + 1): 
        q = 0   
        for i in range(j):
            q = max(q, (price[i] + revenue[j - i]))
        revenue[j] = q
    return revenue[m]

price = [1,5,8,9,10,17,17,20,24,30]
m = len(price)
v = rod_cut(price, 4)
print(v)


def extended_rod_cut(price,n): 
    n = len(price) 
    if n == 0:
        return 0
    negative_infinity = -math.inf 
    revenue = [0 for i in range(n)]
    size = [0 for j in range(n)]
    revenue[0] = 0
    for j in range(n-1): 
        q = 0
        for i in range(1,n):
            if q < price[i] + revenue[j-i]:
                q = price[i] + revenue[j - i]
                size[j] = i
        revenue[j] = q
    return revenue, size


def print_cut_rodSolution(price, n):
    (r,s) = extended_rod_cut(price,n)
    while n > 0:
        print(s[n])
        n = n - s[n]

p = [1,5,8,9,10,17,17,20,24,30]



