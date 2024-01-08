import random
import numpy as np
from numpy import random
import math
from collections import defaultdict
#!/usr/bin/env python3
"""! @brief A Randomize Probabilistic Hiring Problem Algorithm
The following algorithm implements a uniform random permutation with rank ordering.
In the hiring problem, candidates names are given in a list,randomly shuffle. 
The rank of each candidate is map to the names of candidates after the interview, with initial status 
being "not hired".
The function returns a list of hired candidates with their names, ranks and hiring status
total runtime is O(nlgn)

"""
# @file  hire_assistant.py
def hire_assistant(names, n):
    arr = random.permutation(names)
    interview = []
    for i in range(len(arr)):
        rank = i + 3
        interview.append((rank, arr[i])) 
    hired = interview[n:]    
    print(len(interview), "sat interview, selection were based on ranks\n")
    print(len(hired), "were successful with ranks in decreasing order\n")  
    print("\n")
    return hired[::-1]
  
x =  ["Jill", "Sally", "Jane", "john", "Albert", "William", "Sam", "Tully"]
n = 4
s = hire_assistant(x, n)
print(s)



        
        
        
        
        
        
        
        
        
        
        
        
    
         
      
        
        
        
        
        
    
    





    
    

