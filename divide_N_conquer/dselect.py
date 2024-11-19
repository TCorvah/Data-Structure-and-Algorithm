import math

# @file subroutine hoare_partition.py
def hoare_partition(A, pvalue):
    """Partitions the array around the pivot value using two indices, i and j.
    
    The partition is done such that:
    - All elements less than the pivot are on the left side.
    - All elements greater than the pivot are on the right side.
    - The function returns an index `j` such that the pivot is positioned in its correct location.

    Args:
    A (list): The array to partition.
    pvalue (int): The pivot value around which to partition the array.

    Returns:
    int: The index `j` where the pivot is positioned after partitioning.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    
    low = 0 # start of the array
    high = len(A) - 1 # end of the array
    i = low - 1 # 'i' starts just left of the first element
    j = high + 1 # 'i' starts just right  of the last  element
    
    while True:
        # Increment `i` to find an element greater than or equal to the pivot
        i += 1
        while A[i] < pvalue: #Move `i` right until finding an element >= pivot
            i += 1
            
        # Decrement `j` to find an element smaller than or equal to the pivot
        j -= 1 
        while A[j] > pvalue:  #Move `j` left  until finding an element <= pivot
            j -= 1 
            
        # If `i` and `j` have crossed, partitioning is complete    
        if i >= j:  
            return j  # Return the index `j` where the partitioning is done
        A[i],A[j] = A[j], A[i] # Swap elements to partition around the pivot

 
           
def dselect(lst, i): 
    """ 
    A deterministic selection algorithm to find the ith smallest element in the list using the 'median of medians' approach.
    This method selects a pivot using the median of medians, which is the median of each group of 5 elements in the list.
    The partitioning process is done using Hoare's partitioning method, which efficiently sorts in-place.

    Args:
    lst (list): The input list from which the ith smallest element is to be selected.
    i (int): The index (0-based) of the order statistic to find. For example, i = 0 for the smallest element.

    Returns:
    int: The ith smallest element in the list, corresponding to the user's input index `i`.

    Time Complexity: O(n) - The time complexity is linear because each recursive call reduces the problem size significantly.
    Space Complexity: O(n) - The space complexity is O(n) due to the space used to store the sublists and medians.
    """

    if len(lst) <= 5:
        # If the list is small (5 or fewer elements), sort it and return the ith element.
        return sorted(lst)[i]
    
    # Step 1: Split the list into sublists of 5 elements each, and sort each sublist.
    sublists = [sorted(lst[j:j+5]) for j in range(0, len(lst),5)]
    print(f"sublist list: {sublists}")
    
     # Step 2: Find the median of each sorted sublist (this will serve as candidates for the pivot).
    medians = [sublist[len(sublist)//2] for sublist in sublists] 
    print(f"median list: {medians}")
    
    # Step 3: Recursively call dselect to find the pivot, which is the median of the medians.
    pivot = dselect(medians, len(medians)//2)
    print(f"Pivot found: {pivot}")
    
    # Step 4: Partition the original list around the pivot using Hoare's partition method.
    position = hoare_partition(lst, pivot)
    print(f"Partition index: {position}, List after partitioning: {lst}")
   
   # Step 5: Recurse into the left or right part based on the position of the pivot.
    if position == i:
        # If the pivot is at the desired position, return it.
        return lst[position]

    elif position >  i:
        # If the pivot's position is greater than `i`, the desired element is in the left part.
        return dselect(lst[0:position], i )
    else:
        # If the pivot's position is less than `i`, the desired element is in the right part.
        return dselect(lst[position + 1:], i - (position + 1 ))
        
  
            
            
    

A = [11, 6, 10, 2, 15, 8, 1, 7, 14, 3, 9, 12, 4, 5, 13]
i = 6
t = dselect(A,i)
print(t)


    




