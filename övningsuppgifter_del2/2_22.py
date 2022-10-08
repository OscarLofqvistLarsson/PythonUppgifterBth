from numpy import append


def matrix_transporter(matrix):
    transported_matrix = []
    for _ in matrix[0]:
            transported_matrix.append([])
    for x in range(len(matrix)):
        for z in range(len(matrix[0])):
            transported_matrix[z].append(matrix[x][z])

    return print(transported_matrix)



matrix_transporter([[1, 2, 3], [4, 5, 6]])