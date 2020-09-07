def sum_diagonals(matrix):
    ans = 0
    n = len(matrix)
    if len(matrix[0]) == 0:
        return 0
    for i in range(n):
        ans += matrix[i][i] + matrix[i][n - i - 1]
    return ans
