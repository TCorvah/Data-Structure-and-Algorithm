def LCSEQ(A,B):
    # m and n are the lengths of the two input sequences A and B
    m = len(A)
    n = len(B)
    # Initialize a list to store matching indices of A and B
    lst = []

    # Create a 2D array 'arr' to store the lengths of the longest common subsequence (LCS)
    # The array dimensions are (m+1) x (n+1) to accommodate the 0th row and column (base case)
    arr = [[0] * (n + 1) for _ in range(m + 1)]

    # Loop through both sequences A and B to compute the LCS
    for i in range(m):
        for j in range(n):
            # If characters match, the value is the previous diagonal value + 1
            if A[i] == B[j]:
                arr[i][j] = arr[i - 1][j - 1] + 1
                # Add matching indices to the list if the distance between indices is 0 or 1
                # This condition tries to focus on nearby matches
                if abs(i - j) == 0 or abs(i - j) == 1:
                    lst.append((i, j))     
            else:
                # Otherwise, take the maximum value from the left or top cell
                arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])

    # Print characters that match (according to the indices stored in 'lst')
    for i, j in lst:
        print(A[i], B[j])                  

    # Return the list of matching index pairs and the number of matches
    return lst, len(lst)


x = ["A", "B", "C", "B","D","A", "B"]
y = ["B", "D", "C", "A", "B", "A"]
a = LCSEQ(x,y)
print(a)