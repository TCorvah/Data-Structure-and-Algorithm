import math
import sys
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
    for j in range(m + 1): 
        q = 0 
        for i in range(j):
            q = max(q, (price[i] + revenue[j - i - 1]))
        revenue[j] = q
    return revenue[m]

price = [1,5,8,9,10,17,17,20,24,30]
m = len(price)
v = rod_cut(price, 4)
print(v)






def extended_rod_cut(price,n): 
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
    """  
    s = [0 for j in range(n + 1)] 
    (r,s) = extended_rod_cut(price,n)
    while n > 0:
        print(s[n], end = " ")
        n = n - s[n]  
 
       

p = [1,5,8,9,10,17,17,20,24,30]
x = print_cut_rodSolution(p,7)
print(x)



