#Insertion sort 
#Inputs a sequence of numbers from a array
#outputs a reordering of the numbers in increasing order.
#runtime is n^2
def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i > -1 and arr[i] >  key:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key
    return arr 
        



arr = [5,2, 4, 6, 1, 3]
output = insertion_sort(arr)
print(output)



