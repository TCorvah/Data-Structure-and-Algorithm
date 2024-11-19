import math
import sys
"""_summary_ The following uses dynamic programming to solve the rod-cutting
    problem. The code utilizes a bottom up method that enforces ordering
"""
# @file bottom_up_cut_rod.py
def bottom_up_cut_rod(p,n):
    """! The  bottom up implementation of the rod cutting problem 
        uses a natural ordering on each subproblem of size j, i, with j > i.
        each subproblem size is save in an array revenue and returns when the input
        n matches the price of the rod.
        the runtime of this code snippet is O(n)^2 as it iterates twice
        for each i,j in n.
        @param the price p, and length of the rod n
        @return a the revenue price, given the input n, which is the length of the rod.
    """  
    r = [0 for i in range(n+1)]
    r[0] = 0
    for j in range(n+1):
        q = 0
        for i in range(j+1):
            q = max(q, p[i] + r[j-i-1])
        r[j] = q
    return r[n]


def reconstruction_rod_cut(price,n): 
    """! The extended bottom up implementation of the rod cutting problem 
        computes for each size j, not only the maximum revenue of r_j, but
        s_j, the optimal size for the first piecec to cut off.
        the runtime of this code snippet is O(n)^2 as it iterates twice
        for each i,j in n.
        @param the price and length of the array n 
        @return A list of rod sizes in an optimal decomposition of the length n
    """    
    n = len(price) 
    if n == 0:
        return 0
    revenue = [0 for i in range(n + 1)]
    size = [0 for j in range(n + 1)]
    revenue[0] = 0
    for j in range(n + 1): 
        q = 0
        for i in range(j):
            if q < price[i] + revenue[j- i - 1]:
                q = price[i] + revenue[j - i - 1]
                size[j] = i + 1
        revenue[j] = q
    return revenue, size


        
def print_cut_rodSolution(price, n):
    """! The print function prints an optimal solution for a specific revenue 
        @param the price and length of the array n 
        @return None, but prints cuts of revenue  corresponding to the first optimal
        decomposition
        run time is 0(n) as it prints the value in size,  coresponding to the revenue
    """  
    s = [0 for j in range(n + 1)] 
    (r,s) = reconstruction_rod_cut(price,n)
    while n > 0:
        print(s[n], end = " ")
        n = n - s[n] 
 
#p = [1,5,8,9,10,17,17,20,24,30]

