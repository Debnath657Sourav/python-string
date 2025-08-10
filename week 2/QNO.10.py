def count_zeros(mat):
    n = len(mat)
    i, j = 0, n - 1 
    count = 0
    while i < n and j >= 0:
        if mat[i][j] == 0:
            count += j + 1  
            i += 1
        else:
            j -= 1
    return count


matrix = [
    [0, 0, 1],
    [0, 1, 1],
    [1, 1, 1]
]
print(count_zeros(matrix))  
