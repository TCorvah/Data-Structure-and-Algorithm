import sys
def rod_cut(price, m):   
    revenue = [0 for i in range(m + 1)]
    revenue[0] = -1
    q = sys.maxsize
    p = sorted(price)
    for i in range(m + 1):      
        for j in range(i):
            q = min(q, (price[j] + revenue[i - j - 1]))
        revenue[i] = q
    return revenue[m]

arr = [5,6,1,4,2]
size = len(arr)
v = rod_cut(arr, size)
print(v)

