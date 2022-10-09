def det(matrix):
    res = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return res

M = ((3, 1), (5, 2))
print(det(M))