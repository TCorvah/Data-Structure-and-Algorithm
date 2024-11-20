import math
import sys
"""
    The following code uses dynamic programming to solve the rod-cutting problem.
    It utilizes a bottom-up approach to find the optimal way to cut a rod of length n into smaller pieces.
    Each subproblem is solved by building up from smaller problems, storing the maximum revenue for each length.
    The complexity of the solution is O(n^2), since each subproblem is computed in a nested loop.
"""

# @file bottom_up_cut_rod.py
def bottom_up_cut_rod(p,n):
    """ 
    Solves the rod cutting problem using dynamic programming. 
    Computes the maximum revenue for a rod of length n by considering all possible ways to cut the rod.
    
    Parameters:
        p (list): List containing the price for each rod length.
        n (int): The length of the rod to cut.

    Returns:
        int: The maximum revenue achievable for a rod of length n.
        
    Time Complexity: O(n^2), due to the nested loop that iterates over all subproblem lengths.
    """
    # Ensure the price array has at least n elements
    if len(p) < n:
        raise ValueError("Price array must have at least n elements.")
    
    # Initialize a list to store the maximum revenue for each length
    revenue = [0 for i in range(n+1)]
    
    revenue[0] = 0
    
    # Loop over all possible lengths from 1 to n
    for j in range(n+1):
        q = 0
        # For each length j, check all possible first cuts
        for i in range(j):
            q = max(q, p[i] + revenue[j-i-1])
            
        revenue[j] = q
        
    return revenue[n]


def reconstruction_rod_cut(price,n): 
    """
    Extended bottom-up implementation of the rod cutting problem. 
    Computes the optimal sizes of pieces to cut from the rod for maximum revenue.
    
    Parameters:
        price (list): List containing the price for each rod length.
        n (int): The length of the rod to cut.

    Returns:
        tuple: 
            - List containing the maximum revenue for each length (revenue).
            - List containing the size of the first piece to cut for each length (size).
    
    Time Complexity: O(n^2), as it iterates over all subproblem lengths and possible cuts.
    """
    # Initialize lists for storing revenue and the size of the first piece to cut
    revenue = [0 for i in range(n + 1)]
    size = [0 for j in range(n + 1)]
    revenue[0] = 0
    # Loop to compute the maximum revenue for each rod length
    for j in range(n + 1): 
        q = 0
        for i in range(j):
            if q < price[i] + revenue[j- i - 1]:
                q = price[i] + revenue[j - i - 1]
                size[j] = i + 1  # Record the size of the first piece to cut
        revenue[j] = q
    return revenue, size


        
def print_cut_rodSolution(price, n):
    """
    Prints the optimal decomposition of the rod for maximum revenue by recursively 
    determining the cuts from the size list.
    
    Parameters:
        price (list): List containing the price for each rod length.
        n (int): The length of the rod to cut.
    
    Returns:
        None, but prints the sizes of the cuts corresponding to the optimal revenue.
    
    Time Complexity: O(n), as it prints the cuts based on the stored sizes.
    """
    # Get the revenue and size lists from the reconstruction function
    (revenue,size) = reconstruction_rod_cut(price,n)
    while n > 0:
        print(size[n], end = " ")
        n = n - size[n] 
      
 
p = [1,5,8,9,10,17,17,20,24,30]
n = 7
x = print_cut_rodSolution(p, n)
print(x)