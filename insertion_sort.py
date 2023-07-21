#special credit to Introduction to Algorithms 3rd Edition
# this algorithm uses a key, value for the sort. It's run timeis n^2
# the key satrts at index 1 and the value being compare starts at index 0
def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] >  key:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key
    return arr 
        



arr = [5,2, 4, 6, 1, 3]
output = insertion_sort(arr)
print(output)



