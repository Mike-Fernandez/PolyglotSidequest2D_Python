
def zeroes(rows, columns):
    m = []
    for i in range(rows):
        row = []
        for j in range(columns):
            cell = 0
            row.append(cell)
        m.append(row)
    return m

def printMatrix2(m):
    for row in m:
        for cell in row:
            print(cell, end=" ")
        print()

def transpose(M):
    """
    Returns a transpose of a matrix.
        :param M: The matrix to be transposed
 
        :return: The transpose of the given matrix
    """
    # Section 1: if a 1D array, convert to a 2D array = matrix
 #   if not isinstance(M[0],list):
 #       M = [M]
 
    # Section 2: Get dimensions
    rows = len(M)
    cols = len(M[0])
 
    # Section 3: MT is zeros matrix with transposed dimensions
    MT = zeroes(cols, rows)
 
    # Section 4: Copy values from M to it's transpose MT
    for i in range(rows):
        for j in range(cols):
            MT[j][i] = M[i][j]
 
    return MT

matrix = zeroes(3, 3)
matrix[2][1] = 1
printMatrix2(matrix)
print("break")
mat2 = transpose(matrix)
printMatrix2(mat2)