# If an element in an MxN matrix is 0, the entire row and column are set to 0

# initial solution - store the zero rows and columns in a separate list 

def zero_matrix(matrix):
    
    M, N = len(matrix), len(matrix[0])
    zero_row = []
    zero_col = []

    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 0:
                zero_row.append(i)
                zero_col.append(j)

    for i in zero_row:
        for col in range(N):
            matrix[i][col] = 0

    for j in zero_col:
        for row in range(M):
            matrix[row][j] = 0

    return matrix

# my_matrix = [[1,2,3],[4,0,6],[7,8,9]]
# print(zero_matrix(my_matrix))

# While this solution works, it take O(m+n) space

# Below is the optimized solution for O(1) space

def zero_matrix_optimized(matrix):

    if not matrix or not matrix[0]:
        return
    
    M, N = len(matrix), len(matrix[0])
    first_row_zero = any(matrix[0][j]==0 for j in range(N))
    first_col_zero = any(matrix[i][0]==0 for i in range(M))

    # mark matrix using 1st row & column
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    # all the rows that have zero on the first col - set to zero
    for i in range(1, M):
        if matrix[i][0] == 0:
            for j in range(N):
                matrix[i][j] = 0

    # same but with columsn
    for j in range(1, N):
        if matrix[0][j] == 0:
            for i in range(M):
                matrix[i][j] = 0

    # zero 1st row if needed
    if first_row_zero:
        for j in range(N):
            matrix[0][j] = 0

    # zero 1st column if needed
    if first_col_zero:
        for i in range(M):
            matrix[i][0] = 0

    return matrix

my_matrix = [[1,2,3],[4,0,6],[7,8,9]]
print(zero_matrix_optimized(my_matrix))
