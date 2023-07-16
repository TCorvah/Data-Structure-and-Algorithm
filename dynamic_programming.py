import sys
def rod_cut(price, m):   
    revenue = [0 for i in range(m + 1)]
    q = 0
    p = sorted(price)
    for i in range(m + 1):      
        for j in range(i):
            q = max(q, (p[j] + revenue[i - j - 1]))
        revenue[i] = q
    return revenue[m]

arr = [5,6,1,4]
size = len(arr)
v = rod_cut(arr, size)
print(v)

def CutRod(A, num):
    if num == 0:
        return 0
    q = 0
    for i in range(1, num):
        q = max(q,A[i] + CutRod(A, num - i))
    return q


A = [1,5,8,9, 10, 17, 17, 20, 24, 30]
num = 2
print(CutRod(A, num))



