def LCSEQ(A, B):
    """
    A novel approach to finding the Longest Common Subsequence (LCS) by considering both 
    global and local matches while enforcing distance constraints.

    Unlike the traditional LCS, this method ensures that a match at index `i` in A and 
    `j` in B only persists if it satisfies a distance constraint, avoiding misplaced matches.

    The method tracks optimal matches dynamically, allowing for replacements when a 
    better alignment is found.
    
    Time Complexity: Approx. O(m * n) due to DP table filling.
    """
    # Get lengths of input sequences
    m = len(A)
    n = len(B)
    lst = []  # List to hold valid match pairs
    used_x = set()  # To track indices of A (x)
    best_match_for_b = {}     # Dictionary to track the best match in A for each index in B

    # Initialize DP table with correct size
    arr = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]: # Check if characters match (adjusting for 0-based index)
                arr[i][j] = arr[i - 1][j - 1] + 1  # Standard LCS update

                # Ensure the match respects the distance constraint:
                # The absolute difference between (i-1) and (j-1) should not exceed abs(m - n)
                if abs((i - 1) - (j - 1)) <= abs(m - n):
                    # If this position in B already has a match, check if the new match is better
                    if j - 1 in best_match_for_b:
                        prev_i = best_match_for_b[j - 1]
                        # If this match in A occurs later (closer to optimal alignment), replace the previous one
                        if i - 1 > prev_i:  
                            lst.remove((prev_i, j - 1))
                            lst.append((i - 1, j - 1))
                            used_x.remove(prev_i)
                            used_x.add(i - 1)
                            best_match_for_b[j - 1] = i - 1
                    else:
                        lst.append((i - 1, j - 1))
                        used_x.add(i - 1)
                        best_match_for_b[j - 1] = i - 1

    return lst, len(lst)  # Return matched pairs and LCS length

# Test with the given data
x = ["A", "C", "D", "E", "F"]
y = ["A", "B", "C", "D", "E", "F", "G"]
result = LCSEQ(x, y)
print(result)