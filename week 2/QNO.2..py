def rotate_anticlockwise(mat):
    n = len(mat)
    for i in range(n):
        for j in range(i+1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j] 
    mat.reverse() 


mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rotate_anticlockwise(mat)
print(mat)

