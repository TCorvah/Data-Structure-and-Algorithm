def LCSEQ(A, B):
    m = len(A)
    n = len(B)
    lst = []  # List to hold valid match pairs
    used_x = set()  # To track indices of A (x)

    # Initialize DP table with correct size
    arr = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:  # Adjust indexing to avoid out-of-bounds
                arr[i][j] = arr[i - 1][j - 1] + 1

                # Store match indices based on conditions
                if abs((i - 1) - (j - 1)) <= abs(m - n) and (i - 1) not in used_x:
                    lst.append((i - 1, j - 1))  # Store original indices
                    used_x.add(i - 1)

            #else:
            #    arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])


    # Return matched pairs and the LCS length
    return lst, arr[m][n]  # arr[m][n] holds the LCS length

# Test with the given data
x = ["A", "B", "C", "B", "D", "A", "B"]
y = ["B", "D", "C", "A", "B"]
result = LCSEQ(x, y)
print(result)