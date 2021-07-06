#import sel

def showMatrix(m):
    for row in m:
        for cell in row:
            print(cell, end="  ")
        print()

def zeroes2(m, rows, columns):
    for i in range(rows):
        row = []
        for j in range(columns):
            cell = 0
            row.append(cell)
        m.append(row)


#Returns matrix filled with zeroes
def zeroes(rows, columns):
    m = []
    for i in range(rows):
        row = []
        for j in range(columns):
            cell = 0
            row.append(cell)
        m.append(row)
    return m

def vectorZeroes(v, n):
    for i in range(n):
        v.append(0)

def copy_matrix(M):
    rows = len(M)
    cols = len(M[0])
    MC = zeroes(rows, cols)
    for i in range(rows):
        for j in range(cols):
            MC[i][j] = M[i][j] 

    return MC

def calculateMember(i, j, r, A, B):
    member = 0
    for k in range(r):
        member += A[i][k]*B[k][j]
    return member

def productMatrixMatrix(A, B, n, r, m):
    R = zeroes(n,m)

    for i in range(n):
        for j in range(m):
            R[i][j] = calculateMember(i,j,r,A,B)
    return R

def productMatrixVector(A,v,R):
    for f in range(len(A)):
        cell = 0.0
        for c in range(len(v)):
            cell+=A[f][c]*v[c]
        R[f] =  R[f] + cell

def productRealMatrix(real, M, R):
    for i in range(len(M)):
        for j in range(len(M[0])):
            R[i][j] = real*M[i][j]

def getMatrixMinor(m,rows,columns):
    return [row[:columns] + row[columns+1:] for row in (m[:rows]+m[rows+1:])]

def determinant(M):
    if(len(M) == 1):
        return M[0][0]
    else:
        det = 0.0
        for i in range(len(M[0])):
            minor = []
            minor = copy_matrix(M)
            minor = getMatrixMinor(minor, 0, i)
            det += pow(-1,i)*M[0][i]*determinant(minor)
        return det;

def cofactors(M, cof):
    n = len(M)
    zeroes2(cof,n,n)
    for i in range(n):
        for j in range(len(M[0])):
            minor = copy_matrix(M)
            minor = getMatrixMinor(minor, i, j)
            cof[i][j] = pow(-1, i+j)*determinant(minor)




def printVector(v):
    for i in range(len(v)):
        print(v[i])

def transpose(M):
    rows = len(M)
    cols = len(M[0])
    MT = zeroes(cols, rows)
    for i in range(rows):
        for j in range(cols):
            MT[j][i] = M[i][j]
 
    return MT

def inverseMatrix(M, Minv):
    cof = []
    adj = []
    det = determinant(M)
    if(det == 0):
        print("ERROR")
        return
    cofactors(M,cof)
    adj = transpose(cof)
    productRealMatrix(1/det,adj,Minv)

#def borrarColumna(matrix, column):
#    for i in range(len(matrix)):
#        matrix[i].pop(column)

#matrix = zeroes(3, 3)
#matrix[2][1] = 1
#matrix[1][1] = 5
#matrix[0][2] = 2
#matrix[2][0] = 7
#showMatrix(matrix)
#print("hello from math_tools")
#for i in range(len(matrix)):
#    matrix[i].pop(0)
#showMatrix(matrix)
#det = determinant(matrix)
#vectorZeroes(resp, 3)
#cofactors(matrix, cof)
#print(len(multiplied))
#productMatrixVector(matrix, multiplied, resp)
#Minor = getMatrixMinor(matrix,1,0)
#sel.showMatrix(Minv)
#printVector(resp)
#print(det)