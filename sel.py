import math_tools
import classes

def showMatrix(m):
    for row in m:
        for cell in row:
            print(cell, end="  ")
        print()

def showKs(Ks):
        for K in Ks:
            print("K del elemento")
            showMatrix(K)
            print("*********************")

def showVector(v):
    print("[")
    for item in v:
        print(item)
    print("]")

def showBs(Bs):
    for B in Bs:
        print("B del elemento")
        showVector(B)
        print("*********************")

def calculateLocalD(ind, mesh):
    D = 0.0
    a = 0.0
    b = 0.0
    c = 0.0
    d = 0.0
    e = 0.0
    f = 0.0
    g = 0.0
    h = 0.0
    i = 0.0

    element = mesh.getElement(ind)

    node1 = mesh.getNode(element.getNode1()-1)
    node2 = mesh.getNode(element.getNode2()-1)
    node3 = mesh.getNode(element.getNode3()-1)
    node4 = mesh.getNode(element.getNode4()-1)

    a = node2.getX() - node1.getX()
    b = node2.getY() - node1.getY()
    c = node2.getZ() - node1.getZ()
    d = node3.getX() - node1.getX()
    e = node3.getY() - node1.getY()
    f = node3.getZ() - node1.getZ()
    g = node4.getX() - node1.getX()
    h = node4.getY() - node1.getY()
    i = node4.getZ() - node1.getZ()

    #Se calcula el determinante de esta matriz utilizando
    #la Regla de Sarrus.
    D = a*e*i+d*h*c+g*b*f-g*e*c-a*h*f-d*b*i
    return D

def calculateLocalVolume(ind, mesh):
    #Se utiliza la siguiente fórmula:
    #      Dados los 4 puntos vértices del tetrahedro A, B, C, D.
    #      Nos anclamos en A y calculamos los 3 vectores:
    #              V1 = B - A
    #              V2 = C - A
    #              V3 = D - A
    #      Luego el volumen es:
    #              V = (1/6)*det(  [ V1' ; V2' ; V3' ]  )
    V = 0.0
    a = 0.0
    b = 0.0
    c = 0.0
    d = 0.0
    e = 0.0
    f = 0.0
    g = 0.0
    h = 0.0
    i = 0.0

    element = mesh.getElement(ind)

    node1 = mesh.getNode(element.getNode1()-1)
    node2 = mesh.getNode(element.getNode2()-1)
    node3 = mesh.getNode(element.getNode3()-1)
    node4 = mesh.getNode(element.getNode4()-1)

    a = node2.getX() - node1.getX()
    b = node2.getY() - node1.getY()
    c = node2.getZ() - node1.getZ()
    d = node3.getX() - node1.getX()
    e = node3.getY() - node1.getY()
    f = node3.getZ() - node1.getZ()
    g = node4.getX() - node1.getX()
    h = node4.getY() - node1.getY()
    i = node4.getZ() - node1.getZ()

    #Para el determinante se usa la Regla de Sarrus.
    V = (1.0/6.0) * (a*e*i+d*h*c+g*b*f-g*e*c-a*h*f-d*b*i)
    return V

def ab_ij(ai,aj,a1,bi,bj,b1):
    return (ai - a1)*(bj - b1) - (aj - a1)*(bi - b1)

def createLocalc1(x1, x2):
    return 1/pow(x2-x1,2)

def createLocalc2(x1, x2, x8):
    return (1/(x2-x1))*(4*x1+4*x2-8*x8)

def calculateA(i,mesh): #matriz a por referencia
    element = mesh.getElement(i)
    n1 = mesh.getNode(element.getNode1()-1)
    n2 = mesh.getNode(element.getNode2()-1)
    n8 = mesh.getNode(element.getNode8()-1)
    c1 = createLocalc1(n1.getX(), n2.getX())
    c2 = createLocalc2(n1.getX(), n2.getX(), n8.getX())

    return (-1/pow(c2,2)*192)*pow(4*c1-c2, 4) - (1/c2*24)*pow(4*c1-c2, 3) - (1/pow(c2,3)*3840)*pow(4*c1-c2, 5) + (1/pow(c2,3)*3840)*pow(4*c1+3*c2, 5)



def calculateB(i, mesh):
    element = mesh.getElement(i)
    n1 = mesh.getNode(element.getNode1()-1)
    n2 = mesh.getNode(element.getNode2()-1)
    n8 = mesh.getNode(element.getNode8()-1)
    c1 = createLocalc1(n1.getX(), n2.getX())
    c2 = createLocalc2(n1.getX(), n2.getX(), n8.getX())

    return (-1/pow(c2,2)*192)*pow(4*c1+c2, 4) + (1/c2*24)*pow(4*c1+c2, 3) + (1/pow(c2,3)*3840)*pow(4*c1+c2, 5) - (1/pow(c2,3)*3840)*pow(4*c1-3*c2, 5)

def calculateC(i, mesh):
    element = mesh.getElement(i)
    n1 = mesh.getNode(element.getNode1()-1)
    n2 = mesh.getNode(element.getNode2()-1)
    n8 = mesh.getNode(element.getNode8()-1)
    c2 = createLocalc2(n1.getX(), n2.getX(), n8.getX())

    return (4/15)*pow(c2,2)

def calculateD(i, mesh):
    element = mesh.getElement(i)
    n1 = mesh.getNode(element.getNode1()-1)
    n2 = mesh.getNode(element.getNode2()-1)
    n8 = mesh.getNode(element.getNode8()-1)
    c1 = createLocalc1(n1.getX(), n2.getX())
    c2 = createLocalc2(n1.getX(), n2.getX(), n8.getX())

    return (1/pow(c2,2)*192)*pow(4*c2-c1, 4) - (1/pow(c2,3)*3840)*pow(4*c2-c1, 5) + (1/pow(c2,3)*7680)*pow(4*c2+8*c1, 5) - (7/pow(c2,3)*7680)*pow(4*c2-8*c1, 5) + (1/pow(c2,3)*768)*pow(-8*c1,5) - (c1/pow(c2,3)*96)*pow(4*c2-8*c1,4) + ((2*c1-1)/pow(c2,3)*192)*pow(-8*c1,4)

def calculateE(i, mesh):
    element = mesh.getElement(i)
    n1 = mesh.getNode(element.getNode1()-1)
    n2 = mesh.getNode(element.getNode2()-1)
    n8 = mesh.getNode(element.getNode8()-1)
    c1 = createLocalc1(n1.getX(), n2.getX())
    c2 = createLocalc2(n1.getX(), n2.getX(), n8.getX())

    return (8/3)*pow(c1,2) + (1/30)*pow(c2,2)

def calculateF(i, mesh):
    element = mesh.getElement(i)
    n1 = mesh.getNode(element.getNode1()-1)
    n2 = mesh.getNode(element.getNode2()-1)
    n8 = mesh.getNode(element.getNode8()-1)
    c1 = createLocalc1(n1.getX(), n2.getX())
    c2 = createLocalc2(n1.getX(), n2.getX(), n8.getX())

    return (2/3)*c1*c2 - (1/30)*pow(c2,2)

def calculateG(i, mesh):
    element = mesh.getElement(i)
    n1 = mesh.getNode(element.getNode1()-1)
    n2 = mesh.getNode(element.getNode2()-1)
    n8 = mesh.getNode(element.getNode8()-1)
    c1 = createLocalc1(n1.getX(), n2.getX())
    c2 = createLocalc2(n1.getX(), n2.getX(), n8.getX())

    return (-16/3)*pow(c1,2) - (4/3)*c1*c2 - (2/15)*pow(c2,2)

def calculateH(i, mesh):
    element = mesh.getElement(i)
    n1 = mesh.getNode(element.getNode1()-1)
    n2 = mesh.getNode(element.getNode2()-1)
    n8 = mesh.getNode(element.getNode8()-1)
    c1 = createLocalc1(n1.getX(), n2.getX())
    c2 = createLocalc2(n1.getX(), n2.getX(), n8.getX())

    return (2/3)*c1*c2 + (1/30)*pow(c2,2)

def calculateI(i, mesh):
    element = mesh.getElement(i)
    n1 = mesh.getNode(element.getNode1()-1)
    n2 = mesh.getNode(element.getNode2()-1)
    n8 = mesh.getNode(element.getNode8()-1)
    c1 = createLocalc1(n1.getX(), n2.getX())
    c2 = createLocalc2(n1.getX(), n2.getX(), n8.getX())

    return (-16/3)*pow(c1,2) - (2/3)*pow(c2,2)

def calculateJ(i, mesh):
    element = mesh.getElement(i)
    n1 = mesh.getNode(element.getNode1()-1)
    n2 = mesh.getNode(element.getNode2()-1)
    n8 = mesh.getNode(element.getNode8()-1)
    c1 = createLocalc1(n1.getX(), n2.getX())
    c2 = createLocalc2(n1.getX(), n2.getX(), n8.getX())

    return (2/15)*pow(c2,2)

def calculateK(i, mesh):
    element = mesh.getElement(i)
    n1 = mesh.getNode(element.getNode1()-1)
    n2 = mesh.getNode(element.getNode2()-1)
    n8 = mesh.getNode(element.getNode8()-1)
    c1 = createLocalc1(n1.getX(), n2.getX())
    c2 = createLocalc2(n1.getX(), n2.getX(), n8.getX())

    return (-4/3)*c1*c2

def localMiu(i, mesh, miu):
    element = mesh.getElement(i)
    n1 = mesh.getNode(element.getNode1()-1)
    n2 = mesh.getNode(element.getNode2()-1)
    n8 = mesh.getNode(element.getNode8()-1)
    A = calculateA(i,mesh)
    B = calculateB(i,mesh)
    C = calculateC(i,mesh)
    D = calculateD(i,mesh)
    E = calculateE(i,mesh)
    F = calculateF(i,mesh)
    G = calculateG(i,mesh)
    H = calculateH(i,mesh)
    I = calculateI(i,mesh)
    J = calculateJ(i,mesh)
    K = calculateK(i,mesh)

    miu = math_tools.zeroes(10,10)

    miu[0][0] = A
    miu[0][1] = E
    miu[0][4] = -F
    miu[0][6] = -F
    miu[0][7] = G
    miu[0][8] = F
    miu[0][9] = F

    miu[1][0] = E
    miu[1][1] = B
    miu[1][4] = -H
    miu[1][6] = -H
    miu[1][7] = I
    miu[1][8] = H
    miu[1][9] = H

    miu[4][0] = -F
    miu[4][1] = -H
    miu[4][4] = C
    miu[4][6] = J
    miu[4][7] = -K
    miu[4][8] = -C
    miu[4][9] = -J

    miu[6][0] = -F
    miu[6][1] = -H
    miu[6][4] = J
    miu[6][6] = C
    miu[6][7] = -K
    miu[6][8] = -J
    miu[6][9] = -C

    miu[7][0] = G
    miu[7][1] = I
    miu[7][4] = -K
    miu[7][6] = -K
    miu[7][7] = D
    miu[7][8] = K
    miu[7][9] = K

    miu[8][0] = F
    miu[8][1] = H
    miu[8][4] = -C
    miu[8][6] = -J
    miu[8][7] = K
    miu[8][8] = C
    miu[8][9] = J

    miu[9][0] = F
    miu[9][1] = H
    miu[9][4] = -J
    miu[9][6] = -C
    miu[9][7] = K
    miu[9][8] = J
    miu[9][9] = C

def createLocalK(element, mesh, miu):
    J = calculateJacobiano(element, mesh)
    Ei = 166
    miu = []
    localMiu(element,mesh,miu)

    K = math_tools.zeroes(30,30)
    temp = math_tools.zeroes(30,30)

    h = 0
    for i in range(10):
        for j in range(10):
            temp[i+h][j+h] = miu[i][j]
    h = 10
    for i in range(10):
        for j in range(10):
            temp[i+h][j+h] = miu[i][j]
    h = 20
    for i in range(10):
        for j in range(10):
            temp[i+h][j+h] = miu[i][j]

    math_tools.productRealMatrix(Ei*J,temp, K)
    return K

def createLocalB(element, mesh):
    B = math_tools.vectorZeroes(30,1)
    f = mesh.getParameter(classes.parameters["HEAT_SOURCE"])
    J = calculateJacobiano(element, mesh)
    b_i = J/120
    T = []
    math_tools.vectorZeroes(T, 10)
    T[0] = 59
    T[1] = -1
    T[2] = -1
    T[3] = -1
    T[4] = 4
    T[5] = 4
    T[6] = 4
    T[7] = 4
    T[8] = 4
    T[9] = 4

    bMatrix = math_tools.zeroes(30,3)

    h = 0
    for i in range(10):
        bMatrix[i][h] = T[i]
    
    h = 1
    for i in range(10):
        bMatrix[i][h] = T[i]
    
    h = 2
    for i in range(10):
        bMatrix[i][h] = T[i]
    
    temp = math_tools.zeroes(30,3)
    math_tools.productRealMatrix(b_i,bMatrix,temp)
    math_tools.productMatrixVector(temp, f, B)
    return B


def calculateJacobiano(ind,mesh):
    J=0.0
    a=0.0
    b=0.0
    c=0.0
    d=0.0
    e=0.0
    f=0.0
    g=0.0
    h=0.0
    i=0.0

    el = mesh.getElement(ind)

    n1 = mesh.getNode(el.getNode1()-1)
    n2 = mesh.getNode(el.getNode2()-1)
    n3 = mesh.getNode(el.getNode3()-1)
    n4 = mesh.getNode(el.getNode4()-1)

    a=n2.getX()-n1.getX()
    b=n3.getX()-n1.getX()
    c=n4.getX()-n1.getX()
    d=n2.getY()-n1.getY()
    e=n3.getY()-n1.getY()
    f=n4.getY()-n1.getY()
    g=n2.getZ()-n1.getZ()
    h=n3.getZ()-n1.getZ()
    i=n4.getZ()-n1.getZ()
    #Se calcula el determinante de esta matriz utilizando
    #la Regla de Sarrus.
    J = a*e*i+d*h*c+g*b*f-g*e*c-a*h*f-d*b*i

    return J

def calculate(K,b,T):
    print("Iniciando calculo de respuesta...\n")
    Kinv = []
    print("Calculo de inversa...\n")
    math_tools.inverseMatrix(K,Kinv)
    print("Calculo de respuesta...\n")
    math_tools.productMatrixVector(Kinv,b,T)


#m = classes.mesh()
miu = math_tools.zeroes(10,10)

miu[0][0] = 'A'
miu[0][1] = 'E'
miu[0][4] = '-F'
miu[0][6] = '-F'
miu[0][7] = 'G'
miu[0][8] = 'F'
miu[0][9] = 'F'
miu[1][0] = 'E'
miu[1][1] = 'B'
miu[1][4] = '-H'
miu[1][6] = '-H'
miu[1][7] = 'I'
miu[1][8] = 'H'
miu[1][9] = 'H'
miu[4][0] = '-F'
miu[4][1] = '-H'
miu[4][4] = 'C'
miu[4][6] = 'J'
miu[4][7] = '-K'
miu[4][8] = '-C'
miu[4][9] = '-J'
miu[6][0] = '-F'
miu[6][1] = '-H'
miu[6][4] = 'J'
miu[6][6] = 'C'
miu[6][7] = '-K'
miu[6][8] = '-J'
miu[6][9] = '-C'
miu[7][0] = 'G'
miu[7][1] = 'I'
miu[7][4] = '-K'
miu[7][6] = '-K'
miu[7][7] = 'D'
miu[7][8] = 'K'
miu[7][9] = 'K'
miu[8][0] = 'F'
miu[8][1] = 'H'
miu[8][4] = '-C'
miu[8][6] = '-J'
miu[8][7] = 'K'
miu[8][8] = 'C'
miu[8][9] = 'J'
miu[9][0] = 'F'
miu[9][1] = 'H'
miu[9][4] = '-J'
miu[9][6] = '-C'
miu[9][7] = 'K'
miu[9][8] = 'J'
miu[9][9] = 'C'

K = math_tools.zeroes(30,30)
#for t in range(0,30,10):
#    for i in range(10):
#        for j in range(10):
#            K[i+t][j+t] = miu[i][j]

h = 0
for i in range(10):
    for j in range(10):
        K[i+h][j+h] = miu[i][j]
h = 10
for i in range(10):
    for j in range(10):
        K[i+h][j+h] = miu[i][j]
h = 20
for i in range(10):
    for j in range(10):
        K[i+h][j+h] = miu[i][j]
showMatrix(K)