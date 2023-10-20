from random import randrange
import random
def randomize_inplace(A):
    random.shuffle(A)
    candidate = A
    best = 0
    for i in range(1, len(candidate)):
        if i > best and candidate[i] > candidate[best]:
            best = i
            return candidate[i]
    return candidate[best]

A = [1,2,3,4]
c = randomize_inplace(A)
print(c)


