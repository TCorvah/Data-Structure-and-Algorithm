from random import randrange
def permute_by_sorting(A):
    n = len(A)
    p = [i for i in range(n)]
    b = []
    c = []
    for i in range(n):
        p[i] = randrange(0, n ** n)
        b.append((p[i],A[i]))
    x = sorted(b)
    for t,j in x:
        c.append(j)
    return b, c
        
          
        
A = [1,2,3,4]
c = permute_by_sorting(A)
print(c)