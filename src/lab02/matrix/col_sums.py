def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []

    if any(len(row) != len(mat[0]) for row in mat):
        raise ValueError
    return [(sum(column)) for column in zip(*mat)]

print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [-10, 10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))