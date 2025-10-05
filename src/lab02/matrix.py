def transpose(mat):
    if not mat:
        return []

    row_len = len(mat[0])
    for row in mat:
        if len(row) != row_len:
            raise ValueError("рваная матрица")
    return [[mat[i][j] for i in range(len(mat))] for j in range(row_len)]

def row_sums(mat):
    if not mat:
        return []

    row_len = len(mat[0])
    for row in mat:
        if len(row) != row_len:
            raise ValueError("рваная матрица")
    return [sum(row) for row in mat]

def col_sums(mat):
    if not mat:
        return []

    row_len = len(mat[0])
    for row in mat:
        if len(row) != row_len:
            raise ValueError("рваная матрица")
    return [sum(mat[i][j] for i in range(len(mat))) for j in range(row_len)]

print("transpose:")
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))

print("row_sums:")
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))

print("col_sums:")
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
