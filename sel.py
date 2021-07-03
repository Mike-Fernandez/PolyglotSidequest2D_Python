import math_tools
def showMatrix(m):
    for row in m:
        for cell in row:
            print(cell, end=" ")
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

def calculateLocalA(i,matriz,mesh): #matriz a por referencia
    element = mesh.getElement(i)
    n1 = mesh.getNode(element.getNode1()-1)
    n2 = mesh.getNode(element.getNode2()-1)
    n3 = mesh.getNode(element.getNode3()-1)
    n4 = mesh.getNode(element.getNode4()-1)

    matriz[0][0] = ab_ij(n3.getY(),n4.getY(),n1.getY(),n3.getZ(),n4.getZ(),n1.getZ())
    matriz[0][1] = ab_ij(n4.getY(),n2.getY(),n1.getY(),n4.getZ(),n2.getZ(),n1.getZ())
    matriz[0][2] = ab_ij(n2.getY(),n3.getY(),n1.getY(),n2.getZ(),n3.getZ(),n1.getZ())
    matriz[1][0] = ab_ij(n4.getX(),n3.getX(),n1.getX(),n4.getZ(),n3.getZ(),n1.getZ())
    matriz[1][1] = ab_ij(n2.getX(),n4.getX(),n1.getX(),n2.getZ(),n4.getZ(),n1.getZ())
    matriz[1][2] = ab_ij(n3.getX(),n2.getX(),n1.getX(),n3.getZ(),n2.getZ(),n1.getZ())
    matriz[2][0] = ab_ij(n3.getX(),n4.getX(),n1.getX(),n3.getY(),n4.getY(),n1.getY())
    matriz[2][1] = ab_ij(n4.getX(),n2.getX(),n1.getX(),n4.getY(),n2.getY(),n1.getY())
    matriz[2][2] = ab_ij(n2.getX(),n3.getX(),n1.getX(),n2.getY(),n3.getY(),n1.getY())

def calculateB(matriz):
    matriz[0][0] = -1
    matriz[0][1] = 1
    matriz[0][2] = 0
    matriz[0][3] = 0
    
    matriz[1][0] = -1
    matriz[1][1] = 0
    matriz[1][2] = 1
    matriz[1][3] = 0

    matriz[2][0] = -1
    matriz[2][1] = 0
    matriz[2][2] = 0
    matriz[2][3] = 1

def calculateLocalJ(ind,mesh):
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

    element = mesh.getElement(ind)

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