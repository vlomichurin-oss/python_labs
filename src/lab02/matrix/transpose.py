def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return []

    if any(len(row) != len(mat[0]) for row in mat):
        raise ValueError
    return [list(column) for column in zip(*mat)]

print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))