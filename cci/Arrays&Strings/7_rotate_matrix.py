def rotate_matrix(matrix):
    if not matrix:
        return ""
    
    n = len(matrix)

    for i in range(0, n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()

    return matrix

my_matrix = [[1,2,3],
             [4,5,6],
             [7,8,9]]

print(rotate_matrix(my_matrix))