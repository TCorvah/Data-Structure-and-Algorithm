# this binary search algorithm searches if a number is found in an array.
# it first search if the number is found in the left side and then right side
# returns none if not found
def binary_search(arr, n):
    low = 0
    high = len(arr) - 1
    mid = 0

    if low  > high :
       print("error, array must be sorted")
       
    while low <= high: 
         mid = (high + low) // 2                 
         if arr[mid] < n:
             low += 1
         elif arr[mid] > n:
             high = mid - 1                  
         else:           
              return mid 
    return None

# given two list a, b, this code finds the intersection of list a in b using binary search. 
# B has to be sorted and no duplicates allow from both list
def intersection(a, b):
    m = sorted(b)
    intersect = 0
    for x in a:
        result = binary_search(m,x)
        if result >= 0:
           print(x,"present at index", str(result))
        intersect += 1
    print("total item found", intersect)
    return intersect
    
a = [7,4,2,9]
b = [2,4,7,9]

x = intersection(a,b)
print(x)
