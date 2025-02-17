import numpy as np

def Hadarmard_matrix(b):
    """!
    Constructs the base Hadamard matrix H0 from a binary vector with 0, 1.

    Args:
        a (list): Binary input vector of length n (must be power of 2).

    Returns:
        numpy.ndarray: nxn Hadamard matrix with  H0 being the base matrix of 2 by 2.
    """
   
    
    n = len(b)  # Use vector length to determine matrix size
    
    # Ensure input length is a power of 2
    if n < 1 or (n & (n - 1)) != 0:
        raise ValueError("Length of input vector must be a power of 2.")
    
    # Initialize base 2x2 Hadamard matrix from binary vector
    a = [0,1]
    a1 = a[0] + a[1]
    a2 = a1 - a[0]
    a3 = a[1] + a[0]
    a4 = a[0] - a[1]
    
    H0 = np.array([[a1, a2], [a3, a4]])
    # Base cases
    if n == 1:
        return np.array([[1]])  # 1x1 matrix with a single element
    
    if n == 2:
        return H0 # 2x2 Hadamard matrix

    # Grow the matrix iteratively based on n
    H = H0
    while H.shape[0] < n:
        H = np.block([
            [H, H],
            [H, -H]
        ])
    
    return H

# Example usage
if __name__ == "__main__":
    a = [5, 1, 1, 0]  # Input vector of length 4 (power of 2)
    result = Hadarmard_matrix(a)
    print(result)






