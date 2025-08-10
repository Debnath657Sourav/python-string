def diagonalSum(N, M):
    return sum(M[i][i] for i in range(N))


M = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(diagonalSum(3, M))  
