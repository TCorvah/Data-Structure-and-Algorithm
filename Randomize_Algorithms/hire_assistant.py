import random
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
def hire_assistant(candidate, names):
    random.shuffle(names)
    hired =  defaultdict(list)
    interview = defaultdict(list)
    mid = len(candidate)//2
    best_candidates = candidate[0:mid]
    for i in range(len(names)):
        interview[candidate[i]] = names[i]       
    for k,v in interview.items():
        if k in best_candidates:
            hired["rank", k] = "hired", v
    print(interview)
    print("\n")
    print(hired)
            
    chance = int((len(names) - math.log(len(names),2))) * 10
    print(len(interview), "sat interview, selection were based on ranks\n")
    print(len(hired), "were successful with ranks in decreasing order\n")  
    print("chance of a candidate being hired is ", chance,"percent\n")
    print("\n")
    return hired
    

Q = [10,9,8,7,6,5,4,3]
x =  ["Jill", "Sally", "Jane", "john", "Albert", "William", "Sam", "Tully"]
s = hire_assistant(Q,x)
print(s)

    
    

