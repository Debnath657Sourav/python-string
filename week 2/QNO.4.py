def transpose_matrix(mat):
    n = len(mat)
    transposed = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            transposed[j][i] = mat[i][j]
    return transposed

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result = transpose_matrix(matrix)
for row in result:
    print(row)
