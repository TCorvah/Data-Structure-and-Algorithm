import math

def karatsuba(x, y):
    """The following is an implementation of the 
    Karatsuba multiplication algorithm using divide and conquer.
    The length of x and y is assumed to be a power of 2.
    this implemetation uses array indexing to extract x and y and components

    Args:
        x (list): the first integers to be multiply
        y (list): The second integers

    Returns:
        int: The product of x and y
        
    Runtime:
        O(n^log(3))  which is approximately O(n^1.585)
    """
    n = len(x)
    # Base case: when x or y is a single digit, multiply directly
    if n == 1:
        return x[0] * y[0]


    # Divide the numbers into two halves
    m = n // 2
    
    # partition the numbers using array indexing
    a = x[:m]  # The first half of x
    b = x[m:]  # The second half of x
    c = y[:m]  # The first half of y
    d = y[m:]  # The second half of y
    
     # Recursive calls to compute ac, bd, and ad + bc
    ac = karatsuba(a, c)  # Multiply the "high" parts
    bd = karatsuba(b, d)  # Multiply the "low" parts
    
     # Compute ad + bc using the distributive property
    ab = [a[i] + b[i] for i in range(len(a))]
    cd = [c[i] + d[i] for i in range(len(c))]
    
    adbc = karatsuba(ab, cd) - ac - bd  # (a + b)(c + d) - ac - bd
    
     # Combine the results: ac * 10^(2m) + ad + bc * 10^m + bd
    return ac * (10 ** (2 * m)) + adbc * (10 ** m) + bd


# Test case
x = [5,6,7,8]
y = [1,2,3,4]
result = karatsuba(x, y)
print(result)  # Expected output: 7006652 (5678 * 1234)