#!/usr/bin/env python3
"""! @brief A linear search algorithm that returns an index of a specified item """
    

## 
#  @mainpage   inputs a sequence of number from an array and, a value v
#
#  @section outputs an index i, if v = arra[i] or none if not found
#  @section notes_main runtime O(n)
#  -  Runs in Linear time

##
# @file Linear_Search.py
def Linear_search(arr, v):
    """! Searches the array for a specific item in linear time  
    @param arr  The sequence of integers in a list
    @param v     The item to be search for within the array elements
    
    @return  The index of the target variable in O(n)
    """
    index = 0
    for i in range(0,len(arr)):
        if v == arr[i]:
            index += i
      
    return index
def main():
    """!    Main program entry. """

    x = [1,2,3,8]
    d = Linear_search(x,3)
    print(d)
    
if __name__ == "__main__":
    # The `main()` function is the entry point of the program. It is called when the script is run. In
    # this case, it calls the `Linear_search()` function with a list `x` and the value `3` as
    # arguments, and then prints the result.
    main()


