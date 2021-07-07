#import sel

#def showMatrix(m):
#    for row in m:
#        for cell in row:
#            print(cell, end="  ")
#        print()

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

#Fills a vector of size n with 0
def vectorZeroes(v, n):
    for i in range(n):
        v.append(0)

#Returns a copy of the matrix provided
def copy_matrix(M):
    rows = len(M)
    cols = len(M[0])
    MC = zeroes(rows, cols)
    for i in range(rows):
        for j in range(cols):
            MC[i][j] = M[i][j] 

    return MC

#Metodo para calcular un miembro de una matriz
def calculateMember(i, j, r, A, B):
    member = 0
    for k in range(r):
        member += A[i][k]*B[k][j]
    return member

#Returns the result of multiplying two matrixes
def productMatrixMatrix(A, B, n, r, m):
    R = zeroes(n,m)

    for i in range(n):
        for j in range(m):
            R[i][j] = calculateMember(i,j,r,A,B)
    return R

#Calculates the result of multilying a mtrix and a vector
def productMatrixVector(A,v,R):
    for f in range(len(A)):
        cell = 0.0
        for c in range(len(v)):
            cell+=A[f][c]*v[c]
        R[f] =  R[f] + cell

#Multiply the values of a matrix with a scalar values that's given
def productRealMatrix(real, M, R):
    for i in range(len(M)):
        for j in range(len(M[0])):
            R[i][j] = real*M[i][j]

#Calcula un menor de la matriz
def getMatrixMinor(m,rows,columns):
    return [row[:columns] + row[columns+1:] for row in (m[:rows]+m[rows+1:])]

#Calcula el determinante de una matriz
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

#Calcula los cofactores de una matriz
def cofactors(M, cof):
    n = len(M)
    zeroes2(cof,n,n)
    for i in range(n):
        for j in range(len(M[0])):
            minor = copy_matrix(M)
            minor = getMatrixMinor(minor, i, j)
            cof[i][j] = pow(-1, i+j)*determinant(minor)


#Returns the identity matrix of size n
def identity_matrix(n):
    IdM = zeroes(n, n)
    for i in range(n):
        IdM[i][i] = 1.0
 
    return IdM

def printVector(v):
    for i in range(len(v)):
        print(v[i])

#Transpone una matriz
def transpose(M):
    rows = len(M)
    cols = len(M[0])
    MT = zeroes(cols, rows)
    for i in range(rows):
        for j in range(cols):
            MT[j][i] = M[i][j]
 
    return MT

#Encontramos este metodo de calcular la inversa de una matriz en el internet
#Este metodo tarda menos tiempo que el metodo de cofactores y adjunta, asi que hemos usado esta version de la funcion
def inverseMatrix(M):
    n = len(M)
    AM = copy_matrix(M)
    I = identity_matrix(n)
    IM = copy_matrix(I)
    indices = list(range(n))
    for fd in range(n):
        if(AM[fd][fd] == 0):
            fdScaler = 1/0.00000000000000001
        else:
            fdScaler = 1.0/AM[fd][fd]

        for j in range(n):
            AM[fd][j] *= fdScaler
            IM[fd][j] *= fdScaler
        
        for i in indices[0:fd] + indices[fd+1:]:
            crScaler = AM[i][fd]
            for p in range(n):
                AM[i][p] = AM[i][p] - crScaler*AM[fd][p]
                IM[i][p] = IM[i][p] - crScaler*IM[fd][p]
    return IM

#Aqui se encuentra el metodo de cofactores y adjunta, sabemos que funciona solo que se tarda muuuuuuuucho en calcular
#def inverseMatrix(M, Minv):
#    cof = []
#    adj = []
#    det = determinant(M)
#    if(det == 0):
#        print("ERROR")
#        return
#    cofactors(M,cof)
#    adj = transpose(cof)
#    productRealMatrix(1/det,adj,Minv)
