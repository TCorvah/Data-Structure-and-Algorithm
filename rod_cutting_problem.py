import math
"""_summary_ The following uses dynamic programming to solve the rod-cutting
    problem.
"""

def rod_cut(price, m):   
    revenue = [0 for i in range(m + 1)]
    revenue[0] = 0
    for j in range(m + 1): 
        q = 0   
        for i in range(j):
            q = max(q, (price[i] + revenue[i - j - 1]))
        revenue[j] = q
    return revenue[m]

arr = [5,6,1,4]
size = len(arr)
v = rod_cut(arr, size)
print(v)




